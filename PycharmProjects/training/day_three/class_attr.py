#Multiple objects of the class can use the static var and the changes get changed easily

class sample:
    x = 22
    def increment(self):
        self.__class__.x += 1 #Accessing using self
        #sample.x += 1 # Accessing using class name
a = sample()
a.increment()
print ("Accessing using object>>>", a.__class__.x)
print ("Accessing using class name >>>", sample.x)