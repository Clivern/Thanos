# ###################################################
#  Visualising Time Complexity using Termgraph
# ###################################################

import time
import functools

# Calculate the runtime
def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

"""
Constant time — O(1) "There is always a fixed number of operations."
"""
@timer
def constant(n):
    result = n * n
    time.sleep(1) # add time interval to build a clear chart with a small sample
    return result


"""
Logarithmic time — O(log n) "The value of n is halved on each iteration of the loop"
"""
@timer
def logarithmic(n):
    result = 0
    while n > 1:
        time.sleep(1) # add time interval to build a clear chart with a small sample
        n //= 2
        result += 1
    return result


"""
Linear time — O(n)
"""
@timer
def linear(n):
    for i in range(n):
        time.sleep(1) # add time interval to build a clear chart with a small sample
    return 1


"""
Quadratic time — O(n^2).
"""
@timer
def quadratic(n):
    result = 0
    for i in range(n):
        time.sleep(1) # add time interval to build a clear chart with a small sample
        for j in range(i, n):
            time.sleep(1) # add time interval to build a clear chart with a small sample
            result += 1
    return result


"""
Linear time — O(n + m) "Sometimes the complexity depends on more variables (see example below)."
"""
@timer
def linear2(n, m):
    result = 0
    for i in range(n):
        time.sleep(1) # add time interval to build a clear chart with a small sample
        result += i
    for j in range(m):
        time.sleep(1) # add time interval to build a clear chart with a small sample
        result += j
    return result


inputs = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20
]

data_constant = []

for item in inputs:
    start = time.time()
    constant(item)
    end = time.time()
    data_constant.append({
        "count": item,
        "time_elapsed": (end - start)
    })

f = open("visualize_constant_time_complexity.dat","w+")
f.write("# Constant Data Set 1\r\n")
for record in data_constant:
    f.write(str(record["count"]) + "   " + str(record["time_elapsed"]) + "\r\n")
f.close()

data_logarithmic = []

for item in inputs:
    start = time.time()
    logarithmic(item)
    end = time.time()
    data_logarithmic.append({
        "count": item,
        "time_elapsed": (end - start)
    })

f = open("visualize_logarithmic_time_complexity.dat","w+")
f.write("# Logarithmic Data Set 1\r\n")
for record in data_logarithmic:
    f.write(str(record["count"]) + "   " + str(record["time_elapsed"]) + "\r\n")
f.close()


data_linear = []

for item in inputs:
    start = time.time()
    linear(item)
    end = time.time()
    data_linear.append({
        "count": item,
        "time_elapsed": (end - start)
    })

f = open("visualize_linear_time_complexity.dat","w+")
f.write("# Linear Data Set 1\r\n")
for record in data_linear:
    f.write(str(record["count"]) + "   " + str(record["time_elapsed"]) + "\r\n")
f.close()


data_quadratic = []

for item in inputs:
    start = time.time()
    quadratic(item)
    end = time.time()
    data_quadratic.append({
        "count": item,
        "time_elapsed": (end - start)
    })

f = open("visualize_quadratic_time_complexity.dat","w+")
f.write("# Quadratic Data Set 1\r\n")
for record in data_quadratic:
    f.write(str(record["count"]) + "   " + str(record["time_elapsed"]) + "\r\n")
f.close()

data_linear2 = []

for item in inputs:
    start = time.time()
    linear2(item, item)
    end = time.time()
    data_linear2.append({
        "count": item,
        "time_elapsed": (end - start)
    })

f = open("visualize_linear2_time_complexity.dat","w+")
f.write("# Linear2 Data Set 1\r\n")
for record in data_linear2:
    f.write(str(record["count"]) + "   " + str(record["time_elapsed"]) + "\r\n")
f.close()
