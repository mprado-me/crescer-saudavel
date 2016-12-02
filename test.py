class MyClass:
    def __init__(self, x):
        self.x = x

page = 1
myClassObject = MyClass(1)

def changePage(page):
    page = 2

def changeClassObject(myClassObject):
    myClassObject.x = 2

print page
print myClassObject.x
changePage(page)
changeClassObject(myClassObject)
print page
print myClassObject.x