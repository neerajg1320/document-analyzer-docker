import pandas as pd
import numpy as np

from datetime import datetime, timezone

from inspect import currentframe, getframeinfo


def df_map_columns(df, mapper_dict):
    # https://www.geeksforgeeks.org/combining-multiple-columns-in-pandas-groupby-with-dictionary/
    # Here we shall map data

    # Set the index of df as Column 'id'
    # df = df.set_index('id')
    # The sum function is causing problem for pandas.timestamp i.e. dates
    # df = df.groupby(mapper_dict, axis=1).min()
    df = df.groupby(mapper_dict, axis=1).min()
    return df


def df_clean_integer_columns(df, amount_cols):
    df[amount_cols] = df[amount_cols].replace({'\$': '', ',': ''}, regex=True)
    df[amount_cols] = df[amount_cols].astype(int)
    return df


def df_clean_float_columns(df, amount_cols):
    df[amount_cols] = df[amount_cols].replace({'\$': '', ',': ''}, regex=True)
    df[amount_cols] = df[amount_cols].astype(float)
    return df


def df_clean_date_columns(df, date_cols):

    df[date_cols] = df[date_cols].apply(pd.to_datetime, dayfirst=True, infer_datetime_format=True)

    return df


def df_dates_str(df):
    date_cols = df_get_date_columns_by_name(df)
    df[date_cols] = df[date_cols].applymap(
        lambda x: datetime.strftime(x, "%Y-%m-%d")
    )

    return df


def df_columns_datetime_iso_format(df, date_cols):
    df[date_cols] = df[date_cols].applymap(
        lambda x: datetime.fromtimestamp(x.timestamp(), tz=timezone.utc).isoformat()
    )

    return df


def df_columns_datetime_iso_date_format(df, date_cols):
    df[date_cols] = df[date_cols].applymap(
        lambda x: datetime.fromtimestamp(x.timestamp(), tz=timezone.utc).isoformat().split('T')[0]
    )

    return df


def df_get_integer_columns_by_name(df):
    integer_cols = []
    for column in df.columns:
        if "Integer" in column:
            integer_cols.append(column)
    return integer_cols


def df_get_float_columns_by_name(df):
    amount_cols = []
    for column in df.columns:
        if "Float" in column:
            amount_cols.append(column)
    return amount_cols


def df_get_date_columns_by_name(df):
    date_cols = []
    for column in df.columns:
        if "date" in column.lower():
            date_cols.append(column)
    return date_cols


def df_get_date_columns_by_name(df):
    date_cols = []
    for column in df.columns:
        if "date" in column.lower():
            date_cols.append(column)
    return date_cols


def df_get_date_columns_by_type(df):
    return df.select_dtypes(include=[np.datetime64]).columns


def df_get_column_by_substr_case_insensitive(df, substr):
    cols = []
    for column in df.columns:
        try:
            if substr.lower() in column.lower():
                cols.append(column)
        except AttributeError as e:
            pass

    return cols


def df_get_column_by_substr(df, substr):
    cols = []
    for column in df.columns:
        if substr in column:
            cols.append(column)

    return cols


def df_map_columns_by_groupbydict(df, mapper_dict):
    df = df_map_columns(df, mapper_dict)
    return df


def df_clean_assign_type_for_integers(df):
    # Map the amount columns as float
    integer_cols = df_get_integer_columns_by_name(df)
    df = df_clean_integer_columns(df, integer_cols)

    return df


def df_clean_assign_type_for_floats(df):
    # Map the amount columns as float
    float_cols = df_get_float_columns_by_name(df)
    df = df_clean_float_columns(df, float_cols)

    return df


def df_clean_assign_type_for_dates(df):
    # Serialize the date columns to a format of our choice
    # First we convert then to datetime format using pd.to_datetime function
    date_cols = df_get_date_columns_by_name(df)
    df = df_clean_date_columns(df, date_cols)

    return df


# https://www.geeksforgeeks.org/combining-multiple-columns-in-pandas-groupby-with-dictionary/
def transform_df_using_dict(df, mapper_dict):

    # The following method will change the names to understood format
    df = df_map_columns_by_groupbydict(df, mapper_dict)

    # The following methods are dependent on the above method. So they have to follow
    df = df_clean_assign_type_for_floats(df)

    df = df_clean_assign_type_for_dates(df)

    return df


# Currently we need to have following columns
# src, select, dst, type
def df_get_columns_info_dataframe(src_df):

    src_columns = src_df.columns.values.tolist()

    # frameinfo = getframeinfo(currentframe())
    # print("[{}:{}]:".format(frameinfo.filename, frameinfo.lineno), src_df)

    float_columns = df_get_column_by_substr_case_insensitive(src_df, "float")
    for col in float_columns:
        if src_df[col].dtype == 'object':
            try:
                src_df[col] = src_df[col].str.replace(',', '').astype(float)
            except AttributeError as e:
                frameinfo = getframeinfo(currentframe())
                print("Exception[{}:{}]:".format(frameinfo.filename, frameinfo.lineno))
                print("Column {} is not string".format(col), e)
                print(src_df[col])

    # frameinfo = getframeinfo(currentframe())
    # print("[{}:{}]:".format(frameinfo.filename, frameinfo.lineno), src_df)

    columns = ["src", "srctype", "select", "dst"]
    columns_df = pd.DataFrame(columns=columns)
    index = 0
    for src_column in src_columns:
        column_row = [str(src_column), str(src_df[src_column].dtype), True, str(src_column),]
        # print(column_row)
        columns_df.loc[index] = column_row
        index += 1

    return columns_df


