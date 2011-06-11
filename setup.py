from distutils.core import setup
import sys

setup(
    name='geventserver',
    description='Script for launch any wsgi or django application over gevent wsgi server.',
    author='Andrei Antoukh',
    author_email='niwi@niwi.be',
    url='https://github.com/niwibe/py-geventserver',
    version='5',
    license='BSD',
    classifiers = [
        'Development Status :: 5 - Stable',
        'Environment :: Console',
        'Programming Language :: Python',
        'Intended Audience :: System Administrators',
        'Operating System :: POSIX',
    ],
    scripts=['geventserver.py'],
)
