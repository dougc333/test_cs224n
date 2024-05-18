

from setuptools import setup

with open("README.md", "r") as fh:
	long_description = fh.read()


setup(
	name='foo'
	version='0.0.1',
	description='foo',
	py_modules=['foo'],
	package_dir={'':'src'}
	classifiers=[
	"Programming Language:: Python ::3.9",
	"License:: OSI Approved :: GNU General Public LIcense v2 or lager",
	"Operating System :: OS Independent",

	],
	long_description = long_description,
	long_description_content_type = "text/markdown",
)
