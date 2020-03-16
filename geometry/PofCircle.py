#===========================================================
# ALGO: P = pi*r^2
#===========================================================

# sec. 1 - import(s) and asigning a canstant value
import math
pi = 3.1415

# sec. 2 - main function
def cir(r):
    P = pi*(r**2)
    print("P =", P)

# sec. 3 - Test
print("Test for r = 5: ")
r = 5
cir(r)

input("Press enter to exit.. ")
#======================== END OF FILE ======================
