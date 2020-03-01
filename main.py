from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

class MyClass():
    def method1(self):
        today = date.today()
        myDatetime = datetime.now()
        print("Today is ", today)
        days = ["mon","tue","wen","thu","fri","sat","sun"]
        print("Today is weekday # is ", days[today.weekday()])
        print ("Hora : ", myDatetime.hour,":",myDatetime.minute )
        print(myDatetime.strftime("%Y/%m/%d"))
    def method2(self, myString = " defult value from argument"):
        print("this is my second method " + myString)

class MySecoundClass(MyClass):
    def method1(self):
        MyClass.method1(self)
        print("My first method from Secound class")

    def method2(self, firstArgument):
        print("secound method : " + firstArgument )

    def timeCompare(self, start=datetime.now(), end=datetime.now()):
        print("one year from start date ", start  + timedelta(days=365))



def main():
    c = MyClass()
    c.method1()
    c.method2("Second argument")

    c2 = MySecoundClass()
    c2.method1()
    c2.method2("argument")
    c2.timeCompare()

if __name__ == "__main__":
    main()
