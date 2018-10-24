class Borg:
    __shared_state = {"1" : "2"}
    def __init__(self):
        self.x = 1
        self.__dict__= self.__shared_state
        pass
b = Borg()
b1 = Borg()

'''behaves as singleton'''
print ("Borg obj :  : ", b) #b and b1 are distinct objects
print ("Borg 1 obj :  :", b1)
print ("Borg dict : : ", b.__dict__) #b and b1 share the same state
print ("Borg 1 dict : : ", b1.__dict__)