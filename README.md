# gsalib
A Python version of the R gsalib library of utility functions for GATK, specifically for reading GATK Report files into pandas DataFrames. See https://github.com/broadinstitute/gsalib.  

# Installation
```python
pip install gsalib
```

# Usage
```python
from gsalib import GatkReport

report = GatkReport('/path/to/gsalib/test/test_v1.0_gatkreport.table')
table = report.tables['ExampleTable']
```

# Documentation
https://gsalib.readthedocs.io/en/latest/
