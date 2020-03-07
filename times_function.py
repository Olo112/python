#===========================================================
# ALGO: f(n) = n! = n (to) i (i=1)
#===========================================================

# sec. 1 - function
def f(n):
    temp = 1
    for i in range(0, n + 1):
        temp = temp * 1
        print(temp)


print("Test with an int of 5: ")
f(5)
input("Press enter to exit..")
#============================= END OF FILE ===================================
