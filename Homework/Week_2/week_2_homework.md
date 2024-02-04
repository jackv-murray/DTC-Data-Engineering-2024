**all of the mage blocks I created are located in the folder and were used to answer the following questions**

**my pipeline is scheduled as:**

![alt text](https://github.com/jackv-murray/DTC-Data-Engineering-2024/blob/main/Homework/Week_2/trigger_small.png)

## Question 1
Once the dataset is loaded, what's the shape of the data?
```
    266,855 rows x 20 columns
    544,898 rows x 18 columns
    544,898 rows x 20 columns
    133,744 rows x 20 columns
```

**Answer: 266,855 rows x 20 columns**

## Question 2
Upon filtering the dataset where the passenger count is greater than 0 and the trip distance is greater than zero, how many rows are left?
```
    544,897 rows
    266,855 rows
    139,370 rows
    266,856 rows
```

**Answer: 139,370 rows**


## Question 3
Which of the following creates a new column lpep_pickup_date by converting lpep_pickup_datetime to a date?
```
    data = data['lpep_pickup_datetime'].date
    data('lpep_pickup_date') = data['lpep_pickup_datetime'].date
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt().date() 
```

**Answer: data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date**  

## Question 4
What are the existing values of VendorID in the dataset?
```
    1, 2, or 3
    1 or 2
    1, 2, 3, 4
    1
```

**Answer: 1 or 2**


 ## Question 5 
How many columns need to be renamed to snake case?
```
    3
    6
    2
    4
```

**Answer: 4**


## Question 6
Once exported, how many partitions (folders) are present in Google Cloud?
```
    96
    56
    67
    108
```

**Answer: for me, I had 95 so I selected the closest option of 96**

