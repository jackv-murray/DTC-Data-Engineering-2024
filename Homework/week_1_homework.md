## Question 1
run the command to get information on Docker

docker --help

Now run the command to get help on the "docker build" command:

docker build --help

Do the same for "docker run".

Which tag has the following text? - Automatically remove the container when it exits

**Answer: rm**

## Question 2
Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash. Now check the python modules that are installed ( use pip list ).

What is version of the package wheel ?

**Answer: I ran docker run -it --entrypoint=bash python:3.9 with gave me the answer of version 0.42.0**


## Question 3
How many taxi trips were totally made on September 18th 2019?

**Answer: 15612**  
```
SELECT count(*)
  FROM green_taxi_trips
  WHERE DATE(lpep_pickup_datetime) = DATE('2019-09-18')
  AND DATE(lpep_dropoff_datetime) = DATE('2019-09-18')
 ```

## Question 4
Which was the pick up day with the largest trip distance Use the pick up time for your calculations.

    2019-09-18
    2019-09-16
    2019-09-26
    2019-09-21

**Answer: 2019-09-26**
```
SELECT MAX(trip_distance), DATE(lpep_pickup_datetime)
  FROM green_taxi_trips
  WHERE DATE(lpep_pickup_datetime) IN (
                                       DATE('2019-09-18'),
                                       DATE('2019-09-16'),
  									   DATE('2019-09-26'),
                                       DATE('2019-09-21'))
 GROUP BY DATE(lpep_pickup_datetime)
```

 ## Question 5 
Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown

Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?

**Answer: Brooklyn, Manhattan, Queens**
 ```
 SELECT sum(total_amount), "Borough"
   FROM green_taxi_trips
   LEFT JOIN taxi_zone_lookup
   ON taxi_zone_lookup."LocationID" = green_taxi_trips."PULocationID" 
   WHERE DATE(lpep_pickup_datetime) = DATE('2019-09-18')
   GROUP BY "Borough"
   ORDER BY sum(total_amount) DESC
   ;
```

## Question 6
For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip? We want the name of the zone, not the id.

**Answer: JFK Airport**
```
 WITH pickups AS (
 SELECT tip_amount, "Borough", "Zone", lpep_dropoff_datetime, "DOLocationID"
   FROM green_taxi_trips
   LEFT JOIN taxi_zone_lookup
   ON taxi_zone_lookup."LocationID" = green_taxi_trips."PULocationID" 
   WHERE "PULocationID" = 7   
   AND EXTRACT(MONTH FROM lpep_dropoff_datetime) = 9
   ORDER BY 1 DESC
   LIMIT 1
 )
 
 SELECT taxi_zone_lookup."Zone"
   FROM taxi_zone_lookup
   INNER JOIN pickups
   ON taxi_zone_lookup."LocationID" = pickups."DOLocationID" 
```

## Question 7
```
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.13.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials)
  project     = var.project
  region      = var.region
}
...
```

Omitting the rest of the terraform code but the rest of my terraform file creates two resources: 

**(1)** a google storage bucket, with name and location defined in the variable file. 

**(2)** a google big query dataset, with its dataset_id and location defined in the variable file. 

The output is included in the homework submission form. 
