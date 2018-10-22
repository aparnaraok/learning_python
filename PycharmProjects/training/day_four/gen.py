#Func can return only one val whereas gen can contain multiple yields

def func_a():
    return "a"

def gen_a():
    yield "b"
    yield "c"
    yield "d"

print (func_a())
print (gen_a()) #Returns gen obj
#Will think that it iterates over only one object again and again
print (next(gen_a()))
print (next(gen_a()))
print (next(gen_a()))

gen_obj = gen_a()
print (next(gen_obj))
print (next(gen_obj))
print (next(gen_obj))
print (next(gen_obj))

#yield / gen remembers what the latest val is whereas return does not