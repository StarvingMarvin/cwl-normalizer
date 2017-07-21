import io
import sys

from os.path import dirname
from setuptools import setup, find_packages
from pip.req import parse_requirements

sys.path.append(dirname(__file__))
from cwlnormalizer import __version__

install_reqs = parse_requirements('requirements.txt', session=False)
requires = [str(ir.req) for ir in install_reqs]

setup(
    name="cwlnormalize",
    version=__version__,
    packages=find_packages(),
    install_requires=requires,
    long_description=io.open('README.md').read(),
    description='CWL Normalizer',
    license='Apache V2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: Apache License Version 2.0'
    ]
)
