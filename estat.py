import eurostat
import pandas as pd
import plotille
import re
import warnings

def search(in_value=None):
    if in_value is None:
        in_value = input("Enter your search value: ")
    toc_df = eurostat.get_toc_df()
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('display.max_colwidth', None)
    return eurostat.subset_toc_df(toc_df, in_value)

def show_geos(code):
    par_values = eurostat.get_par_values(code, 'geo')
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    return par_values

def show(code):
    return eurostat.get_data_df(code)

def parse_custom_date(date_str):
    # Custom date parsing for "2018-S1" format
    match = re.match(r'(\d{4})-S(\d)', date_str)
    if match:
        year, quarter = match.groups()
        quarter_start_month = (int(quarter) - 1) * 3 + 1
        return f"{year}-{quarter_start_month:02d}"
    return date_str

def plot(code, geo='DE', col=0, t=12):
    eurostat.get_pars(code)
    my_filter_pars = {'geo': [geo]}
    data = eurostat.get_data_df(code, filter_pars=my_filter_pars)
    data_transposed = data.T[col][9:].tail(t).fillna(0)

    # Identify the data format based on the first index
    idx_format = data_transposed.index[0]

    # If the data is in "2018-S1" format, apply custom date parsing
    if '-' in idx_format and 'S' in idx_format:
        data_transposed.index = data_transposed.index.map(parse_custom_date)

    # Suppress the UserWarning related to date format inference
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=UserWarning)
        # Convert the index to datetime if not already in the required formats
        data_transposed.index = pd.to_datetime(data_transposed.index, errors='coerce')

    # Remove invalid dates (NaT) resulting from errors='coerce'
    data_transposed = data_transposed.dropna()

    # Sort the data based on the datetime index
    data_transposed.sort_index(inplace=True)

    # If the index is still empty, it means there are no valid dates to plot
    if data_transposed.empty:
        print("No valid dates to plot.")
        return

    x = data_transposed.index
    y = data_transposed.values.astype(float)
    
    print(f'Code: {code} | Geo: {geo} | {data}')
    fig = plotille.Figure()
    fig.width = 100
    fig.height = 30

    fig.plot(x, y)
    print("____________________________________________________________________________________________________________________")
    return print(fig.show())