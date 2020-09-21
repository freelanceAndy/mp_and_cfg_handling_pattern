import os,time,json,random,string
from multiprocessing import Pool


def exceute_database_query(sql_query, result_processor, database_name):
    t1 = time.perf_counter()
    time.sleep(2)
    query_result = {random_char(): random_word()}
    query_time = time.perf_counter() - t1
    return result_processor, query_result, query_time

def set_all_columns(query_result, cfg_obj):
    # This function represents cfg assignment based on results from query
    for k,v in query_result.items():
        cfg_obj[k] = v

def itemized_sales(query_result, cfg_obj):
    # This function represents custom data processing for cfg assignment
    cfg_obj.sales = f"Custom results parsing logic for cfg assignment: {query_result}"
    
def random_word():
    return ''.join(random.choice(string.ascii_letters) for x in range(5))

def random_char():
    return random.choice(string.ascii_letters)

# Some queries to run on database asyncronously
sql_queries = [("SELECT MAX(cost) AS max_sale_cost FROM sales where transaction_date=sysdate;", set_all_columns),
               ("SELECT SUM(cost) AS total_sales_revenue FROM sales;", set_all_columns),
               ("SELECT COUNT(*) AS todays_total_sales FROM sales where transaction_date=sysdate;", set_all_columns),
               ("SELECT item_id, count(item_name) AS total_sales FROM SALES GROUP BY item_id;", itemized_sales),
               ("SELECT SUM(cost) AS total_sales_revenue FROM sales;", set_all_columns),
               ("SELECT COUNT(*) AS todays_total_sales FROM sales where transaction_date=sysdate;", set_all_columns),
               ("SELECT item_id, count(item_name) AS total_sales FROM SALES GROUP BY item_id;", itemized_sales)
]

class Object(object):
    def __str__(self):
        return json.dumps(self.__dict__, indent=4, sort_keys=True)
    def __setitem__(self, variable_name, variable_value):
        self.__dict__[variable_name] = variable_value

# cfg Object for containing the results of the queries and other info
cfg = Object()
cfg.x = 3
cfg.y = "three"
cfg.z = []
cfg["a"] = "Aye!"  # makes use of __setitem__

# Phase 1: Run multiprocesses for I/O intensive database executions
full_run_t1 = time.perf_counter()
max_processes = 4
pool = Pool(processes = max_processes)
jobs = [pool.apply_async(exceute_database_query, (sql_query, result_processor, "database_name")) for sql_query, result_processor in sql_queries]
results = [res.get() for res in jobs]
lapse_seconds_all_queries = time.perf_counter() - full_run_t1
print(f"lapse_seconds_all_queries: {lapse_seconds_all_queries}")

# Phase 2: CPU-side processing of results
for result_processor, query_result, query_time in results:
    result_processor(query_result, cfg)
    print(f"query_result: {query_result} query_time: {query_time}")
print("Config Object:")
print(cfg)
