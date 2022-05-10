class Test:
    num = 100

    def __init__(self, *args):
        print("Param-cons calling")
        self.firstNumber = args[0]
        self.secondNumber = args[1]

    def printSum(self):
        return self.firstNumber + self.secondNumber + self.num

    def demo(self):
        print("Demo method calling")
        print("Sum is: ", Test.printSum(self))


t1 = Test(2, 5)
t1.demo()