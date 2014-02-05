import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pybass",
    version = "0.55.0",
    author = "Wyliodrin",
    author_email = "office@wyliodrin.com",
    description = ("libbass functions"),
    license = "Apache License 2.0",
    keywords = "bass",
    url = "https://github.com/Wyliodrin/pybass",
    packages=['pybass'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache License",
    ],
)
