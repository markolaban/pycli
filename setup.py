import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pycli",
    version="1.0.0",
    description="Build your CLI with ease",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/markolaban/pycli",
    author="Marko Laban",
    author_email="makro.laban@l33tsystems.com",
    license="BSD",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "pycli=pycli.__main__:main",
        ]
    },
)