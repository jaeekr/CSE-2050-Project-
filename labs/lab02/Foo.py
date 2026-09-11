class Foo:

    def __init__(self, name, profession):
        self.name = name
        self.profession = profession

    def speak(self):
        return self.name + " says hello!"

    def __repr__(self):
        return "Foo(" + self.name + ", " + self.profession + ")"
    


    