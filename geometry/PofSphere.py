#===========================================================
# ALGO: P = pi*r^3
#===========================================================

# sec. 1 - main function and asigning a constant value
pi = 3.1415
def sph(r):
    P = pi*r**3
    print("P =", P)

# sec. 2 - Test
print("Test for r = 3:")
r = 3
sph(r)

input("Press enter to exit.. ")
#======================== END OF FILE ======================
