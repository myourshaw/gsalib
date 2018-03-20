$project Tutorial
=================

Introduction
------------

A GATKReport is simply a text document that contains well-formatted, easy to read representation of some tabular data. Many GATK tools output their results as GATKReports. A report contains one or more individual GATK report tables. Every table begins with a header for its metadata and then a header for its name and description. The next row contains the column names followed by the data.


#:GATKReport.v1.1:2
#:GATKTable:11:3:%s:%s:%s:%s:%s:%d:%d:%d:%.2f:%d:%.2f:;
#:GATKTable:CompOverlap:The overlap between eval and comp sites
CompOverlap  CompRod          EvalRod  JexlExpression  Novelty  nEvalVariants  novelSites  nVariantsAtComp  compRate  nConcordant  concordantRate
CompOverlap  dbsnp            test     none            all             106259        3869           102390     96.36        98845           96.54
CompOverlap  dbsnp            test     none            known           102390           0           102390    100.00        98845           96.54
CompOverlap  dbsnp            test     none            novel             3869        3869                0      0.00            0            0.00

#:GATKTable:14:3:%s:%s:%s:%s:%s:%d:%d:%.2f:%d:%d:%.2f:%d:%d:%.2f:;
#:GATKTable:TiTvVariantEvaluator:Ti/Tv Variant Evaluator
TiTvVariantEvaluator  CompRod          EvalRod  JexlExpression  Novelty  nTi    nTv    tiTvRatio  nTiInComp  nTvInComp  TiTvRatioStandard  nTiDerived  nTvDerived  tiTvDerivedRatio
TiTvVariantEvaluator  dbsnp            test     none            all      63401  28285       2.24    7858386    3505967               2.24           0           0              0.00
TiTvVariantEvaluator  dbsnp            test     none            known    61998  26601       2.33      59124      24217               2.44           0           0              0.00
TiTvVariantEvaluator  dbsnp            test     none            novel     1403   1684       0.83    7799262    3481750               2.24           0           0              0.00

Installation
------------
Install $project by running:


::
    pip install gsalib

Analysis
--------
$project has one class, `GatkReport`, that is a dict-like container for all of the tables in a GATK Report file. The `tables` attribute is a key-value object where the key is the table name and the value is a pandas DataFrame that contains the table's data. Note that if a report contains more than one table with the same name the keys will be uniquified as `table`, `table.1`, etc.

Load a report:
::
from gsalib import GatkReport
import pandas as pd

report = GatkReport('test_v1.1.grp')
report_name = report.name
report_tables = report.tables
number of tables = len(report_tables)
table_names = list(tables.keys())
df = tables['GenotypeConcordance_CompProportions']
