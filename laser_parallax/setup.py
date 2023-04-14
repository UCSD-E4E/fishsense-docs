"""Laser Parallax Model
"""
from setuptools import setup, find_packages

setup(
    name='laser_parallax_model',
    version='0.0.0.1',
    author='UCSD Engineers for Exploration',
    author_email='e4e@eng.ucsd.edu',
    entry_points={
    },
    packages=find_packages(),
    install_requires=[
        'jupyter',
        'matplotlib',
        'numpy',
        'torch'
    ],
    extras_require={
        'dev': [
            'pytest',
            'coverage',
            'pylint',
            'wheel',
        ]
    },
)