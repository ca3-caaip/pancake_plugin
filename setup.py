from setuptools import setup, find_packages
from glob import glob

setup(
    name='pancake_plugin',
    version='0.0.3',
    license='mit',
    description='plugin for pancake',

    author='ca3-caaip',
    url='https://github.com/ca3-caaip/ca3-caaip',

    extras_require={
        "test": ["web3", "eth-event", "etherscan-python", "pytest", "pytest-cov", 'senkalib', 'python-dotenv']
    },

    packages=find_packages('src'),
    package_dir={'': 'src'}
)
