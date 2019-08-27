class function_class:
    def __init__(self,fCase):
        print("FCASE >>>>>>>>>>>",fCase)
        fDic = {'A':self.A,         # mapping: string --> variable = function name
                'B':self.B,
                'C':self.C}
        self.fActive = fDic[fCase]
        print(self.fActive)
        
    def A(self):
        print('here runs function A')
    def B(self):
        print('here runs function B')
    def C(self):
        print('here runs function C')
    def run_function(self):
        self.fActive()

#---- main ----------        
fList = ['A','B','C']              # list with the function names as strings
for f in fList:                    # run through the list
    g = function_class(f)
    g.run_function()
