#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'face_recognition_models',
    'Click>=6.0',
    'dlib>=19.3.0',
    'numpy',
HEAD
    'Pillow'

    'scipy'
51acc6e (pre-release fixes)
]

test_requirements = [
    'tox',
    'flake8'
]

setup(
    name='face_recognition',
    version='1.4.0',

 d8bce10 (tweaks)

    version='0.1.3',
13a31cf (Replace local models with a call to face_recognition_models)
    description="Recognize faces from Python or from the command line",
    long_description=readme + '\n\n' + history,
    author="Adam Geitgey",
    author_email='ageitgey@gmail.com',
    url='https://github.com/ageitgey/face_recognition',
    packages=[
        'face_recognition',
    ],
    package_dir={'face_recognition': 'face_recognition'},
    package_data={
        'face_recognition': ['models/*.dat']
    },
    entry_points={
        'console_scripts': [
            'face_recognition=face_recognition.face_recognition_cli:main',
            'face_detection=face_recognition.face_detection_cli:main'
        ]
    },
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='face_recognition',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
