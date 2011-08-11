# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='geventserver',
    description='Script for launch any wsgi or django application over gevent wsgi server.',
    author='Andrei Antoukh',
    author_email='niwi@niwi.be',
    url='https://github.com/niwibe/py-geventserver',
    version='0.5',
    license='BSD',
    install_requires=['gevent'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: System Administrators',
        'Operating System :: POSIX',
    ],
    scripts=['geventserver.py'],
)
