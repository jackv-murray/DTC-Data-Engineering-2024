--creating the external table
CREATE OR REPLACE EXTERNAL TABLE `de-zoomcamp-test.ny_taxi.homework_three`
OPTIONS (
  format = 'parquet',
  uris = ['gs://de-zoomcamp-test-jm-terra-bucket/green_taxi_2022_hwk3.parquet']
)
;

--create a table from the external table
CREATE OR REPLACE TABLE `de-zoomcamp-test.ny_taxi.homework_three_table`
AS SELECT * 
     FROM `de-zoomcamp-test.ny_taxi.homework_three`
;

/* Question 1
counting distinct pulocation_id: external table
*/
SELECT count(distinct pulocation_id) 
  FROM `ny_taxi.homework_three`
;

/* Question 2
counting distinct pulocation_id: materialised table
*/
SELECT count(distinct pulocation_id) 
  FROM `ny_taxi.homework_three_table`
;
/* Question 3
records where fare_amount = 0
*/
SELECT count(*)
  FROM `ny_taxi.homework_three_table`
  WHERE fare_amount = 0
;
/* Question 4
creating an optimised table, clustered on pulocation_id, partitioned on lpep_pickup_datetime
had to create date column to cluster, to avoid parquet issue reading default date types
*/
CREATE TABLE `ny_taxi.homework_three_table_clustered_partitioned` 
PARTITION BY date_column
CLUSTER BY pulocation_id AS
SELECT date(PARSE_TIMESTAMP('%Y-%m-%d %H:%M:%S', lpep_pickup_datetime)) as date_column, *
  FROM `ny_taxi.homework_three_table`

;
/* Question 5
distinct pulocation_ids between 06/01/2022 and 06/30/2022
*/
SELECT distinct pulocation_id
  FROM `ny_taxi.homework_three_table_clustered_partitioned` --`ny_taxi.homework_three_table`
  WHERE date_column BETWEEN '2022-06-01' and '2022-06-30'

