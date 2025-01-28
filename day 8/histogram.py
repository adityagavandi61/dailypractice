################ histogram #######################################################################################################

def histogram(num):
    for i in range(1,num+1):
        print("*"*i) 
print("\nWithout ListCompression\n")
histogram(6)

########## list compression #############

num2 = 6
xxx = ["*" * i for i in range(1, num2 + 1)]
print("\nWith ListCompression\n")
print('\n'.join(xxx))