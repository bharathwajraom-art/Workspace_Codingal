from abc import ABC,abstractmethod
class ABsclass(ABC):
    def print(self,x):
        print("passed value",x)
    def task(self):
        print("we are inside ABsclass task")
class testclass(ABsclass):
    def task(self):
        print("we are inside test class task")
ob1=testclass()
ob1.task()
ob1.print(100)
