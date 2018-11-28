import setuptools
from setuptools import setup, find_packages

setup(
    name='node2vec',
    version='1.0',
    description='Node2Vec',
    author='Aditya Grover and Jure Leskovec.',
    author_email='adityag@cs.stanford.edu ',
    url='https://github.com/aditya-grover/node2vec',
    packages=['node2vec'],
    package_dir={'node2vec': 'node2vec'},
    scripts=['node2vec/train_node2vec.py'])

