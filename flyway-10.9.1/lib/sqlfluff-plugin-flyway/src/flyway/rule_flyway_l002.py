#
# Copyright (C) Red Gate Software Ltd 2010-2024
#
# INTERNAL RELEASE. ALL RIGHTS RESERVED.
#
# Must
# be
# exactly
# 13 lines
# to match
# community
# edition
# license
# length.
#

from sqlfluff.core.rules.base import (
    BaseRule,
    LintResult,
    RuleContext,
)


def get_created_table_name(create_table_segment):
    for segment in create_table_segment.segments:
        if segment.is_type("table_reference"):
            return segment.raw


def get_exec_function(execute_segment):
    return list(filter(lambda s: s.is_type("object_reference"), execute_segment.segments))[0].raw_upper.split(".")[-1]


def escape_tsql_string(s):
    return s.lstrip("N'").strip("'").strip("\"")


def get_exec_args(execute_segment):
    args = list(filter(lambda s: s.type == "raw" and not s.raw.startswith("@"), execute_segment.segments))
    return list(map(lambda a: escape_tsql_string(a.raw), args))


def adds_table_description(execute_segment):
    function = get_exec_function(execute_segment)
    args = get_exec_args(execute_segment)
    return (function == "SP_ADDEXTENDEDPROPERTY") \
        and args[0].upper() == "MS_DESCRIPTION" \
        and args[-2].upper() == "TABLE"


def get_described_table(execute_segment):
    # The name of the object getting the description should be the last arg
    return get_exec_args(execute_segment)[-1]


def get_tables_with_descriptions(parent_segment):
    tables_with_description = []
    for segment in parent_segment.segments:
        if segment.is_type("execute_script_statement") and adds_table_description(segment):
            tables_with_description.append(get_described_table(segment))
        else:
            tables_with_description += get_tables_with_descriptions(segment)
    return tables_with_description


class Rule_Flyway_L002(BaseRule):
    """Tables in SQLServer must have an 'MS_Description' extended attribute  (deprecated)"""

    groups = ("all",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tables_with_descriptions = []

    def _eval(self, context: RuleContext):
        if context.dialect.name == "tsql":
            if context.segment.is_type("file"):
                self.tables_with_descriptions = get_tables_with_descriptions(context.segment)
            if context.segment.is_type("create_table_statement"):
                table_name = get_created_table_name(context.segment)
                if table_name not in self.tables_with_descriptions:
                    return LintResult(
                        anchor=context.segment,
                        description="Table '" + 
                                    table_name +
                                    "' has been created, but no 'MS_Description' property added for it in this file"
                    )
