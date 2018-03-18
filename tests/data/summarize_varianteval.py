"""
Copyright 2018 Michael Yourshaw All Rights Reserved
myourshaw@gmail.com

Non-profit use under MIT license

Summarize several tables produced by GATK VariantEval into a VariantEvalMetricsSummary table
as described in (howto) Evaluate a callset with VariantEval
https://software.broadinstitute.org/gatk/documentation/article?id=6211

--input /run/media/yoursham/MY_6Tb_0/germline/data/NA12878.lValExome0030/metrics/NA12878.lValExome0030.recalibrated.filtered.postCGP.GQfiltered.variant_eval.exome.grp
--input /run/media/yoursham/MY_6Tb_0/germline/data/NA12878.lValExome0030.0.1667/metrics/NA12878.lValExome0030.0.1667.recalibrated.filtered.postCGP.GQfiltered.variant_eval.exome.grp.summary.grp
"""

from argparse import ArgumentParser
import json
import pandas as pd
from pathlib import Path

import gsalib


def df_to_dict(df, orient='None'):
    """
    Replacement for pandas' to_dict which has trouble with
    upcasting ints to floats in the case of other floats being there.
    https://github.com/pandas-dev/pandas/issues/12859#issuecomment-208319535
    see also https://stackoverflow.com/questions/37897527/get-python-pandas-to-dict-with-orient-records-but-without-float-cast
    :param df: a pandas DataFrame
    :param orient: The format of the intermediate JSON string and resulting dict
    :return: dict
    """
    return json.loads(df.to_json(orient=orient))


def run(**kwargs):
    report_file = kwargs['input']
    print(f'Reading report file : {report_file}')
    if kwargs['output']:
        summary_file = kwargs['output']
    else:
        summary_file = report_file + '.summary.grp'
    Path(summary_file).parent.mkdir(parents=True, exist_ok=True)

    report = gsalib.GatkReport()
    report.read_gatkreport(report_file)

    for k in report.keys():
        report[k].reset_index(inplace=True)

    for k in report.keys():
        report[k].set_index(['CompRod', 'Novelty'], inplace=True)

    # Metrics Analysis
    # See https://software.broadinstitute.org/gatk/documentation/article?id=6211

    compoverlap = report['CompOverlap'].loc[:, ['concordantRate']]
    indelsummary = report['IndelSummary'].loc[:, ['n_SNPs', 'n_indels', 'insertion_to_deletion_ratio']]
    titvvariantevaluator = report['TiTvVariantEvaluator'].loc[:, ['tiTvRatio']]
    countvariants = report['CountVariants'].loc[:, ['nSNPs', 'insertionDeletionRatio']]
    multiallelicsummary = report['MultiallelicSummary'].loc[:, ['nSNPs', 'nIndels']]
    validationreport = report['ValidationReport'].loc[:, ['nComp', 'TP', 'FP', 'FN', 'TN']]

    metrics_analysis = pd.concat([
        compoverlap,
        indelsummary,
        titvvariantevaluator,
        countvariants,
        multiallelicsummary,
        validationreport,
    ],
        axis=1)

    # TODO: dynamically compute formats
    COL_FORMATS = '%s:%s:%s:%.2f:%d:%d:%.2f:%.2f:%d:%.2f%d:%d:%d:%d:%d:%d:%d'
    # col_types = []
    # header_formats = []
    # output_formats = []
    # for cell in list(metrics_analysis.itertuples())[0]:
    #     col_types.append(type(cell))

    metrics_dict = df_to_dict(metrics_analysis, orient='split')

    # an extra VariantEvalMetricsSummary column and two indices will be added
    n_cols = len(metrics_dict['columns']) + 3
    n_rows = len(metrics_dict['data'])

    # TODO: left justify strings
    with open(summary_file, 'w') as sf:
        sf.write('#:GATKReport.v1.1:1' + '\n')
        sf.write(f'#:GATKTable:{n_cols}:{n_rows}:{COL_FORMATS}:;' + '\n')
        sf.write(f'#:GATKTable:{kwargs["table_name"]}:Selected metrics from VariantEval' + '\n')
        rows = [[kwargs["table_name"]] +['CompRod', 'Novelty'] + metrics_dict['columns']]
        for i in range(len(metrics_dict['index'])):
            rows.append([kwargs["table_name"]] + list(metrics_dict['index'][i]) + list(map(str, metrics_dict['data'][i])))
        widths = [max(map(len, col)) for col in zip(*rows)]
        for row in rows:
            sf.write("  ".join((val.rjust(width) for val, width in zip(row, widths))) + '\n')

    print(f'Results output to : {summary_file}')


def main():
    parser = ArgumentParser()
    parser.add_argument("-i", "--input",
                        required=True,
                        help="GATK report file from VariantEval")
    parser.add_argument("-o", "--output",
                        help="output file (default: <input>.summary.grp)")
    parser.add_argument("--table_name",
                        default='VariantEvalMetricsSummary',
                        help="output table name (default: VariantEvalMetricsSummary)")

    args = parser.parse_args()

    run(**vars(args))


if __name__ == "__main__":
    main()
