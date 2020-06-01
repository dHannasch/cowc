#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


def get_version_for_conda_meta_yaml():
    """
    load_setup_py_data() will actually run arbitrary code from setup.py,
    so in theory we ought to be able to get the version without needing to set it manually.
    https://stackoverflow.com/questions/38919840/get-package-version-for-conda-meta-yaml-from-source-file
    """
    return '0.0.0'
    # return pkg_resources.get_distribution(__name__).version


setup(
    name='cars-overhead-with-context',
    use_scm_version={
        'local_scheme': 'dirty-tag',
        'write_to': 'src/cars_overhead_with_context/_version.py',
        'fallback_version': '0.0.0',
    },
    get_version_for_conda_meta_yaml=get_version_for_conda_meta_yaml,
    description='An example package. Generated with cookiecutter-pylibrary.',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='T. Nathan Mundhenk',
    author_email='mundhenk1@llnl.gov',
    url='https://github.com/LLNL/cars-overhead-with-context',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
    ],
    project_urls={
        'Documentation': 'https://cars-overhead-with-context.readthedocs.io/',
        'Changelog': 'https://cars-overhead-with-context.readthedocs.io/en/latest/changelog.html',
        'Issue Tracker': 'https://github.com/LLNL/cars-overhead-with-context/issues',
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    install_requires=[
        'click',
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
    setup_requires=[
        'setuptools_scm>=3.3.1',
    ],
    entry_points={
        'console_scripts': [
            'cars-overhead-with-context = cars_overhead_with_context.cli:main',
        ]
    },
)
