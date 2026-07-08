class India():
    def captial(self):
        print("New delhi is the captial of India")
class USA():
    def captial(self):
        print("Washington,D.C. is the captial of USA")
ob1=India()
ob2=USA()
for country in(ob1,ob2):
    country.captial()
