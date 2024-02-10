if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd
import datetime as dt


@transformer
def transform(data, *args, **kwargs):


    taxi_dtypes = {
                'VendorID': pd.Int64Dtype(),
                'passenger_count': pd.Int64Dtype(),
                'lpep_pickup_datetime': str,
                'lpep_dropoff_datetime': str,
                'trip_distance': float,
                'RatecodeID': pd.Int64Dtype(),
                'store_and_fwd_flag': str,
                'PULocationID': pd.Int64Dtype(),
                'DOLocationID': pd.Int64Dtype(),
                'payment_type': pd.Int64Dtype(),
                'fare_amount': float,
                'extra': float,
                'mta_tax': float,
                'tip_amount': float,
                'tolls_amount': float,
                'improvement_surcharge': float,
                'total_amount': float,
                'congestion_surcharge': float 
            }    

    
    #change column data types
    data = data.astype(taxi_dtypes)

    #format columns names from camel case to snake case
    data.columns = (data.columns
                .str.replace('(?<=[a-z])(?=[A-Z])', '_', regex=True)
                .str.lower()
    )

    data['lpep_pickup_datetime'] = data['lpep_pickup_datetime'].astype(date)


    print(data.dtypes)

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    #assert output['lpep_pickup_datetime'].dtype == 'datetime64[ns]'
