import os
import codecs
import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

LIBS_DIR = os.path.join(os.path.curdir, "libs")


def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


# This call to setup() does all the work
setup(
    name="genpylib",
    version=get_version("genpylib/__init__.py"),
    description="Easily generate and deploy python libraries to pypi.org",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/frankhart2018/genpylib",
    author="Siddhartha Dhar Choudhury",
    author_email="sdharchou@gmail.com",
    license="MIT",
    packages=find_packages(),
    entry_points={"console_scripts": ["genpylib = genpylib.run:run",]},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
    ],
    install_requires=["pipreqs", "twine", "simplpy", "setuptools"],
)
