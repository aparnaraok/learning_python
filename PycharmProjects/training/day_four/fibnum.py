class Fibnum:
    def __init__(self):
        self.fn1 = 1
        self.fn2 = 1
    def __next__(self):
        self.fn1, self.fn2, oldfn2 = self.fn1+self.fn2, self.fn1, self.fn2
        return  oldfn2
    def __iter__(self):
        #Takes 'f' object
        print ("Inside iterator>>>>", self)
        return  self

def main():
    f = Fibnum()
    print ("F is >>>>>", f)
    for i in f: #Possible because of __iter__()
        if i > 20:
            break
        else:
            print ("The value of i is >>>>>", i)
if __name__ == '__main__':
    main()
