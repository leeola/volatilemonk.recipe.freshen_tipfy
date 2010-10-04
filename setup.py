# -*- coding: utf-8 -*-
"""
    tipfy.ext.upload_helper
    ~~~~~~~~~~~~~~~~~~~~~~~

    Provides a bin/script to extend the process of normal application uploading.

    :copyright: 2010 Lee Olayvar.
    :license: MIT, see LICENSE.txt for more details.
"""
from setuptools import setup


setup(
    name = 'freshen_tipfy',
    version = '0.0.0',
    license = 'MIT',
    url = '',
    description = ('Provides a bin/script to easily run a freshen bdd test'
                   'with nosegae.'),
    long_description = __doc__,
    author = 'Lee Olayvar',
    author_email = 'leeolayvar@gmail.com',
    zip_safe = False,
    packages = [],
    install_requires = [
        'zc.recipe.egg >= 1.2.2',
        'nose',
        'nosegae',
        'freshen',
    ],
    entry_points = {
        'zc.buildout': [
            'default = freshentipfy.recipes:Recipe',
            ],
        },
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)