a = "cbaCBA"
a_list = []

for i in range(len(a)):
    print(a[i])
    print('====')
    print((' ').join(map(str, a[i])))
