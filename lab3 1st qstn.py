l = [1, 2, 3, 4]
m = [5, 6, 7, 8]
a = []
d = {}
a.extend(l)
a.extend(m)  # using extened they are combined into another list and added into dictionary "d"
d["seperate_l"] = l
d["seperate_m"] = m
print(a, "is the combined list of l and m in another list")
for _ in a:
    d["combined"] = a
print(d)
