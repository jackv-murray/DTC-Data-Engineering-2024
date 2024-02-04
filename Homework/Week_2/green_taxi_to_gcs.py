import pyarrow as pa
import pyarrow.parquet as pq 
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

#tells pyarrow where our gc credentials are located
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/my-creds.json"

bucket_name = 'de-zoomcamp-test-jm-terra-bucket'
object_key = 'green_taxi_data.parquet'
project_id = 'de-zoomcamp-test'
table_name = "green_taxi_data"
root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):

    #we have to define a pyarrow table, by reading the df into a pyarrow table
    table = pa.Table.from_pandas(data)

    #define gcs object - this will be pulled from our environment variables
    gcs = pa.fs.GcsFileSystem()

    #write to the dataset
    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],
        filesystem=gcs
    )


