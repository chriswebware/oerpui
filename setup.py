from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in oerpui/__init__.py
from oerpui import __version__ as version

setup(
	name='oerpui',
	version=version,
	description='UI for OERP',
	author='Chris',
	author_email='info@webware.om',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
