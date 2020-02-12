#making my first push onto new repo, printing hello world
print("Hello World?")
print("Hello World!")


class personClass:
    def __init__(self, name = "John Hancock", age =63):
        self.name = name
        self.age = age
    

    #verifiers
    def ageCheck(self):
        print("I am "+ str(self.age) + " years old.")
    
    def nameCheck(self):
        print("My name is "+self.name+".")

    #modifiers
    def ageSet(self, age):
        self.age = age

    def nameSet(self, name):
        self.name = name


class studentClass(personClass):
    def __init__(self, name="John Hancock", age=63, clas ="None"):
        personClass.__init__(self, name, age)
        self.clas = clas
    def classCheck(self):
        print("I'm currently taking "+self.clas)
    def classSet(self, clas):
        self.clas = clas
    def checkAll(self):
        self.classCheck()
        self.nameCheck()
        self.ageCheck()




person2 = studentClass()
person2.checkAll()
person2.classSet("ComSci 1")
person2.checkAll()
#person1 = personClass()
#person1.ageCheck()
#person1.nameCheck()
#person1.nameSet("Peter Parker")
#person1.ageSet(21)
#person1.ageCheck()
#person1.nameCheck()
