class Family:

    def __init__(self, lastname):
        self.lastname = lastname

    def to_string(self):
        print(f"This family last name is {self.lastname}")

    
class Father(Family):

    def __init__(self, father_name, lastname):
        super(Father, self).__init__(lastname)
        self.father_name = father_name

    def to_string(self):
        print(f"The father name is {self.father_name} and the lastname is {self.lastname}")

class Mother(Family):
    
    def __init__(self, mother_name, lastname):
        super(Mother, self).__init__(lastname)
        self.mother_name = mother_name

    def to_string(self):
        print(f"The mother name is {self.mother_name} and the lastname is {self.lastname}")


#class Child(Father, Mother):
family = Family("zuluaga")
family.to_string()
father = Father("luis", "Zuluaga")

# django y django-rest mas que cualquier cosa
# aws
# docker
# crear una api con django rest
#brocker
#reddis