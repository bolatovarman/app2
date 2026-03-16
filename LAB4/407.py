class Reverse:
    def __init__(self , t): 
        self.text = t
        
    def __iter__(self):
        i = len(self.text) - 1
        while i >= 0:
            yield self.text[i]
            i -= 1
            
s = input()
r = Reverse(s) 
for x in r.__iter__(): 
    print(x,end="")
    
    