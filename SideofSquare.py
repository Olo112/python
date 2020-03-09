#===========================================================
# ALGO: a = (d^2)/2
#===========================================================

# sec. 1 - Import(s) and asigning a constant value
import math
sqrt = math.sqrt

# sec. 2 - main function

def a(d):
    P = (d**2)/2
    a = sqrt(P)
    print("a = ", a)

print("Test for d = 8:")
d = 8
a(d)

input("Press enter to exit..")
#========================== END OF FILE ====================
