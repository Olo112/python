#===========================================================
# ALGO: d = sqrt(2a^2)
#===========================================================

# sec. 1 - import (s) and aigning a constant value
import math
sqrt = math.sqrt

# sec. 2 - main function
def d(a):
    d = sqrt(2* a**2)
    print("d =", d)


# sec. 3 - test
print("Test for a = 5:")
a = 5
d(a)

input("Press enter to exit.. ")
#========================== END OF FILE ====================
