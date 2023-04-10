import base64
from functools import cache
from io import BytesIO
import json
from pathlib import Path
import string

import pandas as pd
from wordcloud import WordCloud

from multiplan.stop_words import STOP_WORDS


@cache
def get_rent_the_runway_data_frame() -> pd.DataFrame:
    data_file = Path('data/renttherunway_final_data.json')
    with open(data_file) as file:
        data = [json.loads(record) for record in file.readlines()]
    df = pd.json_normalize(data)

    df['Peso em Kg'] = (
        df['weight'].str.replace('lbs', '').astype(float) / 2.205
    )
    df['Peso em Kg'] = (df['Peso em Kg'] / 5).round() * 5
    df.to_parquet('data/rent_the_runway.parquet', index=False)

    return df


def save_weight_histogram():
    runaway_df = get_rent_the_runway_data_frame()
    weight_histogram = runaway_df[['Peso em Kg']]
    weight_histogram.to_parquet('data/weight_histogram.parquet', index=False)


def save_fit_data_frame() -> pd.DataFrame:
    runway_df = get_rent_the_runway_data_frame()
    total_df = (
        runway_df.groupby(['rented for'], dropna=True)[['fit']]
        .count()
        .rename(columns={'fit': 'Total'})
    )

    fit_df = (
        runway_df.loc[runway_df['fit'] == 'fit']
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
    fit.to_parquet('data/fit.parquet', index=False)


def remove_punctuation(text: str) -> str:
    allow_letters = set(string.ascii_lowercase)
    text = text.lower()
    text = ''.join([letter for letter in text if letter in allow_letters])
    return text


def save_wordcloud() -> pd.DataFrame:
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

    cloud_word_frequencies = cloud_word.to_dict()
    wc = WordCloud().generate_from_frequencies(
        frequencies=cloud_word_frequencies
    )
    wc.to_file('multiplan/assets/wordcloud.png')


def save_category_size() -> pd.DataFrame:
    rent_the_runaway = get_rent_the_runway_data_frame()
    category_size = rent_the_runaway[['category', 'size']].dropna()
    category_size['count'] = category_size['size']
    category_size = (
        category_size.groupby(['category', 'size']).count().reset_index()
    )
    category_size.to_parquet('data/category_size.parquet')


save_weight_histogram()
save_fit_data_frame()
save_wordcloud()
save_category_size()
