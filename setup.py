#!/usr/bin/env python

from codecs import open
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-leader',
    version='0.0.39',
    description='Leader API',
    long_description=long_description,
    url='https://github.com/conanfanli/leader',
    packages=find_packages(exclude=['tests*']),
    install_requires=['yapf>=0.21'],
    python_requires='~=3.6',
    extras_require={'dev': ['ipython', 'mypy']},
    classifiers=[
        'Development Status :: 3 - Alpha', 'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='leader',
    author='Conan Li',
    author_email='conanlics@gmail.com',
    license='MIT',
)
