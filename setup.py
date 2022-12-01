from distutils.core import setup
from setuptools import find_packages

setup(
    name='snowflake',
    version='0.1.0',    
    description='Homework 5 Python package',
    url='https://github.com/luis1230majo/dsss_hw5.git',
    author='Luis Cervantes',
    author_email='luis.b.cervantes@fau.de',
    license='Apache License 2.0',
    packages = find_packages(),
    install_requires=['turtles', 'numpy'],

)