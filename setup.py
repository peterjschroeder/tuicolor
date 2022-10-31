#!/usr/bin/env python3

from distutils.core import setup
from setuptools import setup, find_packages

setup(
        name='tuicolor', 
        version='0.1', 
        description='Shared library for handling color schemes in tuis', 
        author='Peter J. Schroeder', 
        author_email='peterjschroeder@gmail.com', 
        url='https://github.com/peterjschroeder/tuicolor',
        packages=['tuicolor'],
        install_requires=[]
)

