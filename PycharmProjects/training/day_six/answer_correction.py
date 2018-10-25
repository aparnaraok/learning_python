class Correction:
    #real answers
    # f = open("model.csv")
    # rlis = list(map(lambda x: x.strip().split(','),f.readlines()))
    # print(rlis)
    # dic = dict(map(lambda x: (int(x[ 0 ]),x[ 1 ]),rlis))
    # print(dic)

    #right answers
    # f1 = open("answers.csv")
    # rlis1 = list(map(lambda x: x.strip().split(','),f1.readlines()))
    # dic1 = dict(map(lambda x: (int(x[0]),x[1]),rlis1))
    # print(dic1)

    # i=1
    # count = 0
    # length = len(dic)
    # while(i <= length):
    #     if(dic[i] == dic1[i]):
    #         count += 1
    #     i+=1
    #
    # print("the total marks are",count)
    #listTotal = list(map(lambda x,y:x==y,rlis,rlis1 ))
    # count= 0
    # for var in listTotal:
    #     if(var):
    #         count +=1
    # print("the total marks are",count)

    f = open("model.csv")
    rlis = list(map(lambda x: x.strip().split(','), f.readlines()))

    f1 = open("answers.csv")
    rlis1 = list(map(lambda x: x.strip().split(','), f1.readlines()))

    listTotal = list(map(lambda x, y: x == y, rlis, rlis1))

    count = 0
    i = 0
    while i<len(rlis1):
        if rlis1[i][1] == 'x':
            count+=1
        i+=1
    print("the total marks are",listTotal.count(True)-count)

