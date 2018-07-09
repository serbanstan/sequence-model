# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="sequential-model",
    version="1.0.0",
    description="A hyperparameter optimized implementation of a Keras Sequential NN",
    license="AGPL-3.0",
    author="Serban Stan/Hyunjun Choi",
    author_email="sstan@usc.edu",
    keywords='d3m_primitive',
    packages=find_packages(),
    url='https://github.com/serbanstan/sequential-model',
    download_url='https://github.com/serbanstan/sequential-model',
    install_requires=[],
    long_description=long_description,
    include_package_data = True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
    ], 
    entry_points = {
        'd3m.primitives': [
            'dsbox.SequentialModel = sequential_model:SequentialModel'
        ],
    }
)
