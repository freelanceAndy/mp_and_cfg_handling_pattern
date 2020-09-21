# Multiprocessing and CFG Handling Pattern
Example use of Python multiprocessing Pools and dynamic configuration object assignment.

## General Info
This example code is for when you want to break up a program into two distinct phases:
1. multiprocessing to gather information from a network resource.
1. compute the results single-threaded
The example network processes here are database executions. Each query is also listed with its `result_processor` which is a function. After the multiprocessing phase is complete, each result set is sent to its assigned `result_processor` along with a configuration object. There, we see the configuration object is dynamically assigned attributes based on either the column names of the results or some other custom processing which is represented here by the function `itemized_sales`.

Regarding the `cfg_obj`, we see in its class definition an override of the `__str__` function to print meaningful information to the user. And we see an implementation of the `__setitem__` function which is what allows the function `set_all_columns` to dynamically assign those configuration attributes with: `cfg_obj[k] = v`.

## Run Program and see output:
```
$ /usr/bin/python3 mp_and_cfg_handling_pattern.py
lapse_seconds_all_queries: 4.018662230002519
query_result: {'h': 'WQKss'} query_time: 2.002564299997175
query_result: {'n': 'iuGQi'} query_time: 2.0024301299999934
query_result: {'o': 'niQyr'} query_time: 2.0023436920018867
query_result: {'j': 'orlPE'} query_time: 2.002317946004041
query_result: {'j': 'FUBSe'} query_time: 2.0023015519982437
query_result: {'R': 'oXKag'} query_time: 2.002203301002737
query_result: {'t': 'wlqGl'} query_time: 2.0021805389988003
Config Object:
{
    "R": "oXKag",
    "a": "Aye!",
    "h": "WQKss",
    "j": "FUBSe",
    "n": "iuGQi",
    "o": "niQyr",
    "sales": "Custom results parsing logic for cfg assignment: {'t': 'wlqGl'}",
    "x": 3,
    "y": "three",
    "z": []
}
```
These query results and column names are generated randomly. Niether the database execution, results, nor results processing reflect realistic code. The function `exceute_database_query` would normally be responsible for creating a database connection, running the query, and closing the database connection. But this function is meant to represent accessing any external resource.
