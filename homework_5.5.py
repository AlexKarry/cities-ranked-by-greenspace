file = open('cities_green_space.csv')

data = {}  # initialize an empty dict

for lines in file:  # for each string line in file
    lines = lines.rstrip()  # new str with newline removed
    item = lines.split(',')  # split str line in comma.
    city = item[0]  # 1st item of split:  the city - Oslo
    pct = item[1]  # 2nd item of split:  the value - 68.00%
    pct_split = pct[0:4]  # the value of split:  the value - 68.0
    data[city] = float(pct_split)  # add value float
file.close()

sort = sorted(data, key=data.get,
              reverse=True)  # returns a list of keys, key= arg will sort dict by value, reverse= arg reverses the sort order

print("Cities Ranked by Greenspace (% of total area)")

for key in sort:  # for each key line in sort
    print(key, data[key])
exit()
