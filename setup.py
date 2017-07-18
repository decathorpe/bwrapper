"""
setuptools install script for bwrapper
"""

from setuptools import setup

NAME = "bwrapper"

setup(
    name="bwrapper",
    version=0.1,

    author="Fabio Valentini",
    author_email="decathorpe@gmail.com",

    description="python wrapper around the bubblewrap CLI",
    url="http://github.com/decathorpe/bwrapper",
    license="GPLv3",

    packages=["bwrapper"],
    install_requires=["psutil"],
    tests_require=["nose"],

    test_suite='nose.collector',

    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'Topic :: Security',
                 'Topic :: Software Development',
                 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.6'])
