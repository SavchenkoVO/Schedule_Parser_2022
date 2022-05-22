# -*- coding: utf-8 -*-
import pandas as pd


def transform_schedule(schedule, parameters, output_file) -> pd.DataFrame:
    df = pd.DataFrame(schedule, columns=parameters)
    results_to_csv(df, output_file)
    return df


def results_to_csv(DataFrame, output_file) -> pd.DataFrame:
    DataFrame.to_csv(output_file, sep=';', na_rep='NaN')
