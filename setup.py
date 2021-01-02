#!/usr/bin/env python3
# Copyright 2020, Trail of Bits. All rights reserved.

import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.realpath(os.path.dirname(__file__)), "README.md")) as f:
    long_description = f.read()

# TODO(pag): Update this later with something like: version["__version__"],
version = "0.1"

setup(
    name="dds",
    version=version,
    license="Proprietary and confidential",
    author="Stefan Nagy, Peter Goodman",
    author_email="tech@trailofbits.com",
    description="Dr. Disassembler",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lifting-bits/dds",
    packages=find_packages(exclude=['examples']),
    platforms="any",
    python_requires=">=3.7",
    entry_points={
        'console_scripts': [
            'dds-analyze = dds.analyze:main'
        ]
    },
    install_requires=[
        "wheel",
        "capstone==4.0.2",
        "lief",
        "aenum==2.2.6",
        "typing_extensions"
    ],
    dependency_links=[
        "https://lief.quarkslab.com/packages/lief/"
    ],
    extras_require={
        "dev": [
            "mypy",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Disassemblers ",
    ],
)