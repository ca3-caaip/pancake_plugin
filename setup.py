# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = {"": "src"}

packages = ["pancake_plugin"]

package_data = {"": ["*"]}

install_requires = [
    "pandas>=1.4.2,<2.0.0",
    "senkalib @ "
    "git+https://github.com/ca3-caaip/senkalib.git@b4a41ab228f2532707f712eb11ae68da9aa1b378",
]

setup_kwargs = {
    "name": "pancake-plugin",
    "version": "0.1.0",
    "description": "plugin for PancakeSwap",
    "long_description": None,
    "author": "ca3-caaip",
    "author_email": None,
    "maintainer": None,
    "maintainer_email": None,
    "url": None,
    "package_dir": package_dir,
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "python_requires": ">=3.9,<4.0",
}


setup(**setup_kwargs)
