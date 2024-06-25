class test:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name}"


class test2(test):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def speak(self):
        return f"{self.name} from test2"


testobj = test2("Nutan", "I am Nutan")
print(testobj.speak())
