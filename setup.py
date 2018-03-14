#!/usr/bin/env python3.6

from setuptools import setup, find_packages

setup(
    name='Tower-of-Hanoi',
    version='1.0',
    description='Solving Tower of Hanoi using TensorFlow.',
    author='Tag',
    author_email='tagadvance+Tower-of-Hanoi@gmail.com',
    url='https://github.com/tagadvance/Tower-of-Hanoi',
    packages=find_packages(),
    install_requires=[
        'nose',
        'coverage'
    ]
)