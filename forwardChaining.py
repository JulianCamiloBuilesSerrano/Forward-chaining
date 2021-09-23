
class  expresion():
    def __init__(self, exp):
        self.exp = exp
    #end def
    def validate(self,Conocimiento):
        return self.exp in Conocimiento
    #end def
    def __str__(self):
        return self.exp
    #end def
#end class
class Rule():
    
    def __init__(self,k):
        self.rules = []
        self.operands = []
        self.knowledge,self.q = k.split("=>")
        for k in self.knowledge:
            if k == " ":
                continue
            if k == "&" or k == "O":
                self.operands.append(k)
            else:
                n = expresion(k)
                self.rules.append(n)
            #end if
        #end for
    #end def
    def show(self):
        for i in self.rules:
            print(i)
        #end for
        print("-------")
        for i in self.operands:
            print(i)
        #end for
    #end def
    def eval(self, facts):
        self.facts = facts
        if len(self.operands) == 0:
            if self.rules[0].validate(self.facts):
                return self.q
            else:
                return None
        #end if
        if self.evalR(self.rules[0].validate(self.facts),self.operands,self.rules):
            return self.q
        else:
            return None
    #end def
        
    def evalR(self, precondition,ope, ru):
        if len(ope) == 0:
            return precondition
        #end if
        else:
            if ope[0] == "&":
                if precondition and ru[1].validate(self.facts):
                    return self.evalR(True,ope[1:],ru[1:])
                else:
                    return self.evalR(False,ope[1:],ru[1:])
                #end if 
            #end if
                    
            elif ope[0] == "O":
                
                if precondition or ru[1].validate(self.facts):
                    return self.evalR(True,ope[1:],ru[1:])
                else:
                    return self.evalR(False,ope[1:],ru[1:])
                #end if
            #end if         
    #end def
class ForwarChaning():
    
    def __init__(self):
        self.rules = []
        self.Facts = set()
    #end def

    def addRule(self, rule):
        r =  Rule(rule)
        self.rules.append(r)
    #end def

    def addFact(self, fact):
        self.Facts.add(fact)
    #end def

    def calculate(self):
        copy =  self.Facts.copy()
        for r in self.rules:
            x = r.eval(self.Facts)

            if x is not None:
                self.addFact(x)
        
        if len(copy.difference(self.Facts)) != 0:
            print("La nueva información de hechos: ",self.Facts)
            self.calculate()
        elif len(self.Facts.difference(copy)) != 0: 
            print("La nueva información de hechos: ",self.Facts)
            self.calculate()
        
    #end def


"""     
x = "A =>M"
n = Rule(x)
print(x)
print(n.eval(["A","L"]))
   """
forwar = ForwarChaning()
forwar.addFact("A")
forwar.addFact("L")
forwar.addRule("Z & L =>S")
forwar.addRule("A & N =>E")
forwar.addRule("D O M =>Z")
forwar.addRule("A=>M")
forwar.addRule("L & M =>E")
forwar.addRule("B & C =>Q")

forwar.calculate()