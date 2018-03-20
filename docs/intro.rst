$project: Python/pandas package of utility functions for GATK
=============================================================

$project makes it easy for Python users to analyze metrics reports created by the Broad Institute's Genome Analysis Toolkit (GATK). The Broad provides an R library called gsalib that allows you to load GATKReport files into R for further analysis (https://gatkforums.broadinstitute.org/gatk/discussion/1244/what-is-the-gatkreport-file-format). $project is an adaptation of the R libray that allows you to load GATKReport files into Python/pandas DataFrames.

$project does not support the samtools.metrics reports created by Picard Tools (). To analyze Picard reports with Python, consider using Crimson (https://pypi.python.org/pypi/Crimson).

Features
--------

- Compatible with Python 2 and 3
- Reads GATKReport versions 0.x and 1.x
- Allows analysis with powerful pandas DataFrames and plotting

Installation
------------

Install $project by running:

::
    pip install gsalib

Example
-------

::
    from gsalib import GatkReport
    import pandas as pd

    report = GatkReport('test_v1.0.gatkreport.table')
    table = report.tables['GenotypeConcordance_Summary']

For more, see `examples/reshape_concordance_table.py` and `examples/summarize_varianteval.py`.

Contribute
----------

- Issue Tracker: github.com/myourshaw/$project/issues
- Source Code: github.com/myourshaw/$project

Support
-------

If you are having issues, please let us know.

License
-------

The project is licensed under the MIT license.
