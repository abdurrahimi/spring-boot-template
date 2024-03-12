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

from setuptools import find_packages, setup

PLUGIN_LOGICAL_NAME = "flyway"
PLUGIN_ROOT_MODULE = "flyway"

setup(
    name="sqlfluff-plugin-{plugin_logical_name}".format(
        plugin_logical_name=PLUGIN_LOGICAL_NAME
    ),
    include_package_data=True,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires="sqlfluff==1.2.1",
    entry_points={
        "sqlfluff": [
            "{plugin_logical_name} = {plugin_root_module}.rules".format(
                plugin_logical_name=PLUGIN_LOGICAL_NAME,
                plugin_root_module=PLUGIN_ROOT_MODULE,
            )
        ]
    },
)
