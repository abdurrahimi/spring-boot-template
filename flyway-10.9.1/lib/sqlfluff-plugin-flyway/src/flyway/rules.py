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

import os.path
from typing import List

from sqlfluff.core.config import ConfigLoader
from sqlfluff.core.plugin import hookimpl
from sqlfluff.core.rules.base import (
    BaseRule
)

from flyway.rule_flyway_l001 import Rule_Flyway_L001
from flyway.rule_flyway_l002 import Rule_Flyway_L002


@hookimpl
def get_rules() -> List[BaseRule]:
    return [Rule_Flyway_L001, Rule_Flyway_L002]


@hookimpl
def load_default_config() -> dict:
    return ConfigLoader.get_global().load_default_config_file(
        file_dir=os.path.dirname(__file__),
        file_name="plugin_default_config.cfg",
    )


@hookimpl
def get_configs_info() -> dict:
    return {}
