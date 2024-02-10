import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_parquet_data(*args, **kwargs):

    
    files = []
    lst = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

    for i in lst:
        url = f'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-{i}.parquet' 
        df = pd.read_parquet(url, engine='auto')
        files.append(df)
       # print(url)
    df = pd.concat(files, axis=0, ignore_index=True)

    print(df.dtypes)
    return df




@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

