import matplotlib.pyplot as plt

# Graph 1: Bed Utilization
methods = ["Traditional", "RL Model"]
utilization = [75, 92]

plt.figure()
plt.bar(methods, utilization)
plt.title("Bed Utilization Comparison")
plt.xlabel("Method")
plt.ylabel("Utilization (%)")
plt.show()


# Graph 2: Waiting Time
waiting = [30, 8]

plt.figure()
plt.bar(methods, waiting)
plt.title("Waiting Time Comparison")
plt.xlabel("Method")
plt.ylabel("Time (minutes)")
plt.show()


# Graph 3: Overflow Rate
overflow = [12, 2]

plt.figure()
plt.bar(methods, overflow)
plt.title("Overflow Rate Comparison")
plt.xlabel("Method")
plt.ylabel("Overflow (%)")
plt.show()

methods = ["Traditional", "RL Model"]
waiting = [30, 8]

plt.figure()
plt.bar(methods, waiting)
plt.title("Waiting Time Comparison")
plt.xlabel("Method")
plt.ylabel("Time (minutes)")
plt.show()

methods = ["Traditional", "RL Model"]
overflow = [12, 2]

plt.figure()
plt.bar(methods, overflow)
plt.title("Overflow Rate Comparison")
plt.xlabel("Method")
plt.ylabel("Overflow (%)")
plt.show()