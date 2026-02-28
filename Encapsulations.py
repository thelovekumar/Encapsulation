class Student:
    rollnum = 10
    __name = "abc"#private
    __gen = "Male" # private
    city = "pune" #public
    _age = 26 #protected


    def show(self):
        print("*************STUENT INFO **************")
        print("Roll Num:",self.rollnum)
        print("Name:",self.__name)
        print("Gender:",self.__gen)
        print("city:",self.city)
        print("age:",self._age)

    def setName(self,nm):
        self.__name = nm

    def getName(self):
        return self.__name
    


s = Student()
s.show()
s.setName("love")
print()
print("outside the class")

print("Name:",s.getName())
print("city:",s.city)
        

