class qsequence(object):
    def __init__(self, s):
        self.s = s[:]

    def __next__(self):
        try:
            q = self.s[-self.s[-1]] + self.s[-self.s[-2]]
            self.s.append(q)
            return q
        except IndexError:
            raise StopIteration()
    def __iter__(self): #magic function
        return self

    def current_state(self):
        return self.s

qseq = qsequence([1,1])
#for i in qseq:
#    print ("The value is >>>", i)

print([next(qseq) for __ in range(10)])