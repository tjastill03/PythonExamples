# Taylor Astill
# It is creating a list of the names that are in both lists.

morninglist = ["Jacob","Ron","Harold","TAylor","Billy"]
print(morninglist)

afternoonlist = ["Jacob","Ron","Harold","Ryan","Sean"]
print(afternoonlist)

lunchList = []

for child in morninglist:
    print(child)

    if (child in afternoonlist):
        lunchList.append(child)

print(lunchList)