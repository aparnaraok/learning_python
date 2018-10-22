class Repeater:
    def __init__(self, v, uplim):
        self.value  = v
        self.limit = uplim
        self.count = 0
    def __iter__(self):
        return  self
    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        self.count += 1
        return self.value
br1 = Repeater("hello", 4)

# print (next(br1))
# print (next(br1))
# print (next(br1))
# print (next(br1))
#print (next(br1)) #Raises Stop Iteration

# try:
#     for var in br1:
#         print("Inside for >>>", var)
# except:
#     print ("Done")

# while True:
#     try:
#         print (next(br1))
#     except:
#         print ("out of while loop")
#         break

###Output:
# hello
# hello
# hello
# hello
# out of while loop
