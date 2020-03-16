#===========================================================
# ALGO: SQRT(a^2 + b^2)
#===========================================================

# sec. 1 - import(s) and asigning a constant value
import math
sqrt = math.sqrt

# sec. 2 - main function
def pyth(a, b):
    c = sqrt(a**2 + b**2)
    print("c =", c)

# sec. 3 - test
print("Test for a = 8 and b = 6")
a = 8
b = 6
pyth(a, b)

input("Press enter to exit.. ")
#======================== END OF FILE ======================
