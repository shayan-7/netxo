import re
from os.path import join, dirname

from setuptools import setup, find_packages


# reading package version (same way the sqlalchemy does)
with open(join(dirname(__file__), 'netxo', '__init__.py')) as v_file:
    package_version = re.compile('.*__version__ = \'(.*?)\'', re.S).\
        match(v_file.read()).group(1)


dependencies = ['easycli']


setup(
    name='netxo',
    version=package_version,
    author='Shayan Rok Rok',
    author_email='shayan.rokrok@gmail.com',
    packages=find_packages(),
    install_requires=dependencies,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'netxo = netxo:main'
        ]
    }
)

