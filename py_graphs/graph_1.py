from matplotlib import pyplot

plt = pyplot
x = [1, 2, 3]
y = [1, 4, 9]
z = [10, 5, 0]
plt.plot(x, y)
plt.plot(x, z)
plt.title("Test graph")
plt.xlabel('x')
plt.ylabel('y and z')
plt.legend(["how I learn python", "how I learn Java"])
plt.show()


