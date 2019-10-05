# ###################################################
#  Visualising Linear Time Complexity using Termgraph
# ###################################################
#
# Usage:
# -----
# ➜ $ pip3 install termgraph
# ➜ $ python3 visualize_linear_time_complexity.py
# Finished 'target' in 1.0052 secs
# Finished 'target' in 2.0057 secs
# Finished 'target' in 3.0090 secs
# Finished 'target' in 4.0102 secs
# Finished 'target' in 5.0119 secs
# Finished 'target' in 6.0239 secs
# Finished 'target' in 7.0231 secs
# Finished 'target' in 8.0202 secs
# Finished 'target' in 9.0175 secs
# Finished 'target' in 10.0192 secs

# ➜ $ termgraph visualize_linear_time_complexity.dat
# 1 : ▇ 1.01
# 2 : ▇▇ 2.01
# 3 : ▇▇▇ 3.01
# 4 : ▇▇▇▇ 4.01
# 5 : ▇▇▇▇▇ 5.01
# 6 : ▇▇▇▇▇▇ 6.02
# 7 : ▇▇▇▇▇▇▇ 7.02
# 8 : ▇▇▇▇▇▇▇▇ 8.02
# 9 : ▇▇▇▇▇▇▇▇▇ 9.02
# 10: ▇▇▇▇▇▇▇▇▇▇ 10.02
#
#
#
# A sample script

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

# Linear complexity O(n)
@timer
def target(n):
    j = 0
    for i in n:
        time.sleep(1) # add time interval to build a clear chart with a small sample
        j += 1
    return j

inputs = [
    list(range(1)),
    list(range(2)),
    list(range(3)),
    list(range(4)),
    list(range(5)),
    list(range(6)),
    list(range(7)),
    list(range(8)),
    list(range(9)),
    list(range(10)),
]

data = []

for item in inputs:
    start = time.time()
    target(item)
    end = time.time()
    data.append({
        "count": len(item),
        "time_elapsed": (end - start)
    })

f = open("visualize_linear_time_complexity.dat","w+")
f.write("# Example Data Set 1\r\n")
for record in data:
    f.write(str(record["count"]) + "   " + str(record["time_elapsed"]) + "\r\n")
f.close()
