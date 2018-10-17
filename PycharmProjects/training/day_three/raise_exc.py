try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print ("Type is >>>", type(inst))
    print ("Args is >>>", inst.args)
    print ("Inst is >>>", inst)

    #print ("X is ", x)
    #print ("Y is ", y)
