import os
from functools import wraps

## Exception Handling for file
def exception_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(e)
    return wrapper

## Reads log file
@exception_handler
def read_log_file(file_name):
    with open(file_name) as file:
        content = file.readlines()
    return content

## Returns Number of Errors
@exception_handler
def errors_count(read_log_file):
    ecount = 0
    content  = read_log_file(file_name)
    for line in content:
        if "[error]" in line:
            ecount += 1
    return ecount

## Returns Number of Warnings
@exception_handler
def warnings_count(read_log_file):
    wcount = 0
    content = read_log_file(file_name)
    for line in content:
        if "[warning]" in line:
                wcount += 1
    return wcount

## Returns Number of Info
@exception_handler
def info_count(read_log_file):
    icount = 0
    content = read_log_file(file_name)
    for line in content:
        if "[info]" in line:
                icount += 1
    return icount

## Returns Total log count
@exception_handler
def total_log_count(read_log_file):
    content = read_log_file(file_name)
    lcount = len(content)
    return lcount

## Returns The total size of the logs file in MB
@exception_handler
def get_file_size(file_nameh):
    size = os.path.getsize(file_name)
    size_mb = round(size / (1024 * 1024), 3)
    print('The total size of the logs in MB : {} MB'.format(size_mb))
    return size_mb

## Function Invocations 
file_name = "sample.log"
read_log_file(file_name)
print("Total Number of Errors: ", errors_count(read_log_file))
print("Total Number of Warnings: ", warnings_count(read_log_file))
print("Total Number of Info: ", info_count(read_log_file))
print("Total Log Count: ", total_log_count(read_log_file))
get_file_size(file_name)






    


    






