class Friends():
# can't put anything in above bracket
    language= "Bengali"
    id_no= 12345

    """def full():
        print(f"The ID number {id_no} has the language {language}")... Wrong"""

    @staticmethod
    # staticmethod works on only the immediate below function, no one else
    def first():
        print("Welcome")
    """def second():
        print("Report:=>").... Will give same error on calling"""
    @staticmethod
    def second():
        print("Report:=>")

    def full(any):
        # btw, we can use anything in place of 'any'
        # can't use id_no or language without any key
        print(f"The ID number {any.id_no} has the language {any.language}")
    
    def __init__(an, language, id_no, name):
        an.language= language
        an.id_no= id_no
        an.name= name
        # above 3 can function only if parameter is passed
        # look at last class to understand this part 
        print(f"Experimenting with {an.name}, {an.language}, {an.id_no}")

    def __init__(keep): # automatically does the function for 1 time for each object
        print("It's automatic function")

    """def full2(self, language, id_no, name):
        self.language= language
        self.id_no= id_no
        self.name= name
        print(f"{name} has ID number {self.id_no} has language {self.language}")
        .....Doesn't work"""

f= Friends()
print(f.language)
f.id_no= 13579
print(f.id_no)
f.name= "Pradipta" # creates name through f in Friends
print(f.name, f.language, f.id_no)
g= Friends()
print(g.language, g.id_no)
"""print(g.name)....Error as there is no name in Friends"""
g.full()
g.first()
g.second()
# only works on __init__ function
class New():
    def __init__(self, language, id_no, name):
        self.language= language
        self.id_no= id_no
        self.name= name
        # since we initalised these above 3, we can use it anywhere in this class
        print(f"Name {self.name} with ID {self.id_no} has language {self.language}")

    def Ending(self):
        # see, we can call them in any function
        print(f"Thank You {self.name}")

    def End(any):
        # result will be same even if we use different instance parameter 
        # i.e. any, self
        print(f"For ID {any.id_no}, it is THE END")
    
    @staticmethod
    def Try():
        print(f"Come back later")
h= New("Hindi", 24680, "Anirudh")
h.Ending()
h.End()
"""y= Friends("Japanese", 54732, "Pradipta")....
Can't be called due to __init__(keep) can have 1 parameter only"""
