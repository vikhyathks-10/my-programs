class Father:
    def father_skill(self):
        print("Father: Driving")


class Mother:
    def mother_skill(self):
        print("Mother: Cooking")


class Child(Father, Mother):
    def own_skill(self):
        print("Child: Programming")


c = Child()

c.father_skill()
c.mother_skill()
c.own_skill()