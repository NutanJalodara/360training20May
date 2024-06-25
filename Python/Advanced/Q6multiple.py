class test1:
    def test1(self):
        return "test1"

class test2:
    def test2(self):
        return "test2"

class test(test1, test2):
    pass

testStr = test()
print(testStr.test1())
print(testStr.test2())
