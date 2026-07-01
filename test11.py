class myclass:
    __privateVar=27
    def __privMeth(self):
        print("I am inside class myclass")
    def hello(self):
        print("Private Variable value",myclass.__privateVar)
ob1=myclass()
ob1.hello()
ob1.__privMeth
