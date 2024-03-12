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


def has_primary_key_constraint(segments):
    for segment in segments:
        if segment.is_type("table_constraint") and len(segment.segments) > 0:
            if any(s.raw == "PRIMARY" for s in segment.segments):
                return True

        if has_primary_key_constraint(segment.segments):
            return True
    return False


class Rule_Flyway_L001(BaseRule):
    """CREATE TABLE statements must have a PRIMARY KEY constraint (deprecated)"""

    groups = ("all",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _eval(self, context: RuleContext):
        if context.segment.is_type("create_table_statement"):
            if not has_primary_key_constraint(context.segment.segments):
                return LintResult(
                    anchor=context.segment,
                    description=f"CREATE TABLE statement without a PRIMARY KEY constraint",
                )
