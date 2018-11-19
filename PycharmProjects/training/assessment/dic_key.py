
def get_keys(d, keys=[], values=[]):
    for (key, value) in d.items():
        keys.append(key)
        if type(value) == dict:
            get_keys(value, keys, values)
        else:
            values.append(value)
    return [keys, values]

k = get_keys({'a':{'b':{'c':{'d':'e'}}}})
print("Keys", k[0])
print("Values", k[1])

a = [0,1]
[a.append(a[i]+a[i+1]) for i in range(10)]
print(a)