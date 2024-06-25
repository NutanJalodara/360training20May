class test1:
    def __init__(self, name):
        self.name = name
    
    def test1(self):
        return f"{self.name} from test1"

class test2(test1):
    def __init__(self, name, lname):
        super().__init__(name)
        self.lname = lname
    
    def test2(self):
        return f"{self.name} {self.lname} from test2"

class test(test2):
    def __init__(self, name, lname, minitial):
        super().__init__(name, lname)
        self.minitial = minitial
    
    def test(self):
        return f"{self.name} {self.minitial} {self.lname} from test."

testobj = test("Nutan", "Vasoya", "V")
print(testobj.test2())
print(testobj.test()) 
