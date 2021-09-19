# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="youtube-dl-web-queue",
    version="0.1.0",
    description="Web interface for queueing youtube-dl downloads.",
    license="GPLv3",
    author="Carter Hay",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
    ]
)
