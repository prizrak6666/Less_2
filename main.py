import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 1000
        self.alive = True
    def to_study(self):
        print("Time to ctudy")
        self.progress +=0.12
        self.progress -=3
    def to_sleep(self):
        print("I want sleep")
        self.gladness +=3
        self.money -=50
    def to_chill(self):
        print("Rest time")
        self.gladness +=5
        self.progress -=0.1

    def to_money(self):
            print("Time to make money")
            self.gladness -=5
            self.money +=100

    def is_alive(self):
        if self.progress < 0.5:
            print("Tebe vidrehovano")
            self.alive = False
        elif self.gladness <=0:
            print("Depression...")
            self.alive = False
        elif self.progress >5:
            print("Extern")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress,2)}")
    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        vipadkove = random.randint
        if vipadkove ==1:
            self.to_study()
        elif vipadkove ==2:
            self.to_sleep()
        elif vipadkove ==3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

timofij = Student(name = "Timofij")

for day in range(365):
    if timofij.alive ==False:
        break
    timofij.live(day)
