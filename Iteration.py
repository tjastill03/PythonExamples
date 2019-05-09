# Taylor Astill
# What is happening is a lsit has been craeted and the list is being printed. 
# Then it is sayingfor each of the listed numbers

# list of numbers
numberlist = [1,2,3,4,5,6,7,8,9,10]

print(numberlist)

# iterate over the list
for entry in numberlist:

    # Selection over the iteration
    if (entry % 2) == 0:
        print(entry)