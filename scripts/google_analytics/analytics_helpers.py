import pandas as pd


def make_df(report):
    """Turn a single report from a Google Analytics response into dataframe"""

    dim_labels = report['columnHeader']['dimensions']
    metric_labels = [entry['name']
                     for entry
                     in report['columnHeader']['metricHeader']['metricHeaderEntries']]

    output = []
    rows = report['data'].get('rows', [])
    for row in rows:
        current_data = {}

        for k, v in zip(dim_labels, row['dimensions']):
            current_data[k] = v

        metric_values = [d['values'] for d in row['metrics']]
        metric_values = [item for sublist in metric_values for item in sublist]
        for k, v in zip(metric_labels, metric_values):
            current_data[k] = int(v)

        output.append(current_data)

    return pd.DataFrame(output)
