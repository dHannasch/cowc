========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor|
        |
    * - package
      - | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/cars-overhead-with-context/badge/?style=flat
    :target: https://readthedocs.org/projects/cars-overhead-with-context
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/LLNL/cars-overhead-with-context.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/LLNL/cars-overhead-with-context

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/LLNL/cars-overhead-with-context?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/LLNL/cars-overhead-with-context

.. |commits-since| image:: https://img.shields.io/github/commits-since/LLNL/cars-overhead-with-context/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/LLNL/cars-overhead-with-context/compare/v0.0.0...master



.. end-badges

An example package. Generated with cookiecutter-pylibrary.

Installation
============

::

    pip install cars-overhead-with-context

You can also install the in-development version with::

    pip install https://github.com/LLNL/cars-overhead-with-context/archive/master.zip


To git clone and develop::

    git clone git@github.com/LLNL/cars-overhead-with-context.git@master
    git config --local include.path ../.gitconfig

Documentation
=============


https://cars-overhead-with-context.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
