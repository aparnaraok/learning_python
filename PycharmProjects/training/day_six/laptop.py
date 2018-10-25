#Each one class has different specifications which could be brought in through via adapter.

class Laptop:
    def __init__(self, n):
        self.name = n
    def __str__(self):
        return "the {} laptop".format(self.name)
    def execute(self):
        return "executes a program"

#c1 = Computer("mycomp")
#print (c1)

#the mycomp computer

class Dell:
    def __init__(self, n):
        self.name = n
    def __str__(self):
        return "the {} Dell laptop".format(self.name)
    def play(self):
        return "Has HDMI port"

# c1 = Computer("mycomp")
# s1 = Synthesizer("mysong")
# #print (c1)
#
# print (c1.execute())
# print (s1.play())

class Macintosh:
    def __init__(self, n):
        self.name = n
    def __str__(self):
        return "the {} Macintosh".format(self.name)
    def speak(self):
        return "Has USB port"

class Adapter:
    def __init__(self, o, adaptor_methods):
        self.obj = o
        self.__dict__.update(adaptor_methods) ##Object oriented design pattern of creating a dict
    def __str__(self):
        return str(self.obj)

# objects = [Computer('Asus')] #common list#computer is client
#
# synth = Synthesizer('moog')
# objects.append(Adapter(synth, dict(execute=synth.play()))) #Replacing execute with play
#
# human = Human('Bob')
# objects.append(Adapter(human, dict(execute= human.speak())))

# for i in objects:
#     print ("{}{}".format(str(i), i.execute()))

# Aliter
c1 = Laptop('Windows')
d1 = Dell('dell')
u1 = Macintosh('mac')
as1 = Adapter(d1, dict(execute = d1.play))
ah = Adapter(u1, dict(execute = u1.speak))

#execute is replaces by s1.play and h1.speak
print (as1.obj,as1.execute())
print (ah.obj,ah.execute())

# the moog synthesizer can play a song
# the speak human can speak words


