#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

from uberclicker import __version__

setup(
    name='uberclicker',
    version=__version__,
    author='Shane R. Spencer',
    author_email='shane@bogomip.com',
    packages=['uberclicker'],
    url='https://github.com/whardier/uberclicker',
    license='MIT',
    description='HTTP based keyboard/mouse input',
    long_description=open('README.md').read(),
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Planning',
        'Environment :: No Input/Output (Daemon)',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
    ],
    entry_points={
        'console_scripts': [
            'uberclicker = uberclicker.__main__:run',
        ],
    }

)


