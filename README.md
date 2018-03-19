# gsalib
A Python version of the R gsalib library of utility functions for GATK, specifically for reading GATK Report files into pandas DataFrames. See https://github.com/broadinstitute/gsalib.  

# Installation
```python
pip install gsalib
```

# Usage
```python
from gsalib import GatkReport
import pandas as pd

report = GatkReport('test_v1.0.gatkreport.table')
table = report.tables['GenotypeConcordance_Summary']
```