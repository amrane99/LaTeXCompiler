from setuptools import setup, find_packages

setup(
    name='Convenient Latex Compiler',
    version='1.0',
    description='A program for compiling LaTeX files the convenient way.',
    url='https://github.com/amrane99/LaTeX-Compiler',
    keywords='python setuptools',
    packages=find_packages(include=['lc', 'lc.*']),
)