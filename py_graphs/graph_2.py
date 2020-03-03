# sec. 1 importing module(s) from the library/es
from matplotlib import pyplot as plt

# sec. 2 all the data that is stored in the lists
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

# sec. 3 designing the graph for plots like color, linestyle ...
# plot showing the "other devs" graph/label
plt.plot(ages_x, dev_y, color = 'grey', linestyle = '--',marker = 'o', label = "Other devs")
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]

# plot showing the python graph/label
plt.plot(ages_x, py_dev_y, color = 'blue', linestyle = '--', marker = 'o', label = "Python")

# sec. 4 naming the labels
plt.xlabel("Ages")
plt.ylabel("Madian Salary (USD)")
plt.title("Median Salary (USD) by age")
plt.legend()
plt.grid()
plt.show()
