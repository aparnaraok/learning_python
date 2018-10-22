def iter_each(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except:
            break
        else:
            print ("Item is >>>>", item)
iter_each({12,14,16})