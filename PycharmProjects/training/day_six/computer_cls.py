#Each one class has different specifications which could be brought in through via adapter.

class Computer:
    def __init__(self, n):
        self.name = n
    def __str__(self):
        return "the {} computer".format(self.name)
    def execute(self):
        return "executes a program"

#c1 = Computer("mycomp")
#print (c1)

#the mycomp computer

class Synthesizer:
    def __init__(self, n):
        self.name = n
    def __str__(self):
        return "the {} synthesizer".format(self.name)
    def play(self):
        return "can play a song"

# c1 = Computer("mycomp")
# s1 = Synthesizer("mysong")
# #print (c1)
#
# print (c1.execute())
# print (s1.play())

class Human:
    def __init__(self, n):
        self.name = n
    def __str__(self):
        return "the {} human".format(self.name)
    def speak(self):
        return "can speak words"

class Adapter:
    def __init__(self, o, adaptor_methods):
        self.obj = o
        self.__dict__.update(adaptor_methods) ##Object oriented design pattern of creating a dict
    def __str__(self):
        return str(self.obj)

objects = [Computer('Asus')] #common list#computer is client

synth = Synthesizer('moog')
objects.append(Adapter(synth, dict(execute=synth.play()))) #Replacing execute with play

human = Human('Bob')
objects.append(Adapter(human, dict(execute= human.speak())))

# for i in objects:
#     print ("{}{}".format(str(i), i.execute()))

# Aliter
c1 = Computer('asus')
s1 = Synthesizer('moog')
h1 = Human('speak')
as1 = Adapter(s1, dict(execute = s1.play))
ah = Adapter(h1, dict(execute = h1.speak))

#execute is replaces by s1.play and h1.speak
print (as1.obj,as1.execute())
print (ah.obj,ah.execute())

# the moog synthesizer can play a song
# the speak human can speak words


