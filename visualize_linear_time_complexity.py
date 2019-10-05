# ###################################################
#  Visualising Linear Time Complexity using Termgraph
# ###################################################
#
# ➜ $ pip3 install termgraph
# ➜ $ python3 visualize_linear_time_complexity.py
# Target received this input:
# [0]
# Target received this input:
# [0, 1]
# Target received this input:
# [0, 1, 2]
# Target received this input:
# [0, 1, 2, 3]
# Target received this input:
# [0, 1, 2, 3, 4]
# Target received this input:
# [0, 1, 2, 3, 4, 5]
# Target received this input:
# [0, 1, 2, 3, 4, 5, 6]
# Target received this input:
# [0, 1, 2, 3, 4, 5, 6, 7]
# Target received this input:
# [0, 1, 2, 3, 4, 5, 6, 7, 8]
# Target received this input:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# ➜ $ termgraph visualize_linear_time_complexity.dat
#
# 1 : ▇ 1.00
# 2 : ▇▇ 2.01
# 3 : ▇▇▇ 3.01
# 4 : ▇▇▇▇ 4.01
# 5 : ▇▇▇▇▇ 5.01
# 6 : ▇▇▇▇▇▇ 6.01
# 7 : ▇▇▇▇▇▇▇ 7.02
# 8 : ▇▇▇▇▇▇▇▇ 8.02
# 9 : ▇▇▇▇▇▇▇▇▇ 9.02
# 10: ▇▇▇▇▇▇▇▇▇▇ 10.02
#
#
# A sample script
import time

# Linear complexity O(n)
def target(n):
    print("Target received this input:")
    print(n)
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
