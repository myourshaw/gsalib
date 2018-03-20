gsalib: Python/pandas package of utility functions for GATK
=============================================================

gsalib makes it easy for Python users to analyze metrics reports created by the Broad Institute's Genome Analysis Toolkit (GATK). The Broad provides an R library called gsalib that allows you to load GATKReport files into R for further analysis (https://gatkforums.broadinstitute.org/gatk/discussion/1244/what-is-the-gatkreport-file-format). gsalib is an adaptation of the R libray that allows you to load GATKReport files into Python/pandas DataFrames.

gsalib does not support the samtools.metrics reports created by `Picard Tools <https://broadinstitute.github.io/picard/picard-metric-definitions.html>`_. To analyze Picard reports with Python, consider using the `Crimson <https://pypi.python.org/pypi/Crimson>`_ module.

Features
--------

- Compatible with Python 2 and 3
- Reads GATKReport versions 0.x and 1.x
- Allows analysis with powerful pandas DataFrames and plotting

Installation
------------

Install gsalib by running

::

    pip install gsalib

Example
-------

::

    from gsalib import GatkReport

    report = GatkReport('/path/to/gsalib/test/test_v1.0_gatkreport.table')
    table = report.tables['ExampleTable']

Contribute
----------

- Issue Tracker: github.com/myourshaw/gsalib/issues
- Source Code: github.com/myourshaw/gsalib

Support
-------

If you are having issues, please let me know.

License
-------

The project is licensed under the MIT license.
