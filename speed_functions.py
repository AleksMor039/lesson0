import time


def func(function):
    start_time = time.perf_counter
    function()
    end_time = time.perf_counter
    execution_time = end_time - start_time
    print(execution_time)
    # print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
