import json
from pathlib import Path
import string
from functools import cache

import pandas as pd
from multiplan.stop_words import STOP_WORDS


def remove_punctuation(text: str) -> str:
    allow_letters = set(string.ascii_lowercase)
    text = text.lower()
    text = ''.join([letter for letter in text if letter in allow_letters])
    return text


@cache
def get_rent_the_runway_data_frame() -> pd.DataFrame:
    print(3)
    data_file = Path('data/renttherunway_final_data.json')
    with open(data_file) as file:
        data = [json.loads(record) for record in file.readlines()]
        print(4)
    df = pd.json_normalize(data)
    print(5)

    df['Peso em Kg'] = (
        df['weight'].str.replace('lbs', '').astype(float) / 2.205
    )
    df['Peso em Kg'] = (df['Peso em Kg'] / 5).round() * 5

    return df


def get_fit_data_frame() -> pd.DataFrame:
    rent_the_run_way = get_rent_the_runway_data_frame()
    total_df = (
        rent_the_run_way.groupby(['rented for'], dropna=True)[['fit']]
        .count()
        .rename(columns={'fit': 'Total'})
    )

    fit_df = (
        rent_the_run_way.loc[rent_the_run_way['fit'] == 'fit']
        .groupby(['rented for'], dropna=True)[['fit']]
        .count()
    )

    fit = (
        pd.merge(
            total_df,
            fit_df,
            right_index=True,
            left_index=True,
        )
        .reset_index()
        .sort_values(['fit'], ascending=False)
    )
    fit['Porcentagem'] = fit['fit'] / fit['Total'] * 100
    fit = fit.rename(columns={'fit': 'Fit', 'rented for': 'Rented for'})
    return fit


def get_could_word_frequencies() -> pd.DataFrame:
    rent_the_run_way = get_rent_the_runway_data_frame()
    cloud_word = (
        rent_the_run_way['review_text']
        .str.lower()
        .str.split(' ')
        .explode('review_text')
        .apply(remove_punctuation)
    ).to_frame()
    cloud_word = cloud_word.loc[~cloud_word['review_text'].isin(STOP_WORDS)]
    cloud_word = cloud_word['review_text'].value_counts().head(30)
    return cloud_word.to_dict()


def get_category_size() -> pd.DataFrame:
    rent_the_runaway = get_rent_the_runway_data_frame()
    category_size = rent_the_runaway[['category', 'size']].dropna()
    category_size['count'] = category_size['size']
    category_size = (
        category_size.groupby(['category', 'size']).count().reset_index()
    )
    return category_size
