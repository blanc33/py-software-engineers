class SoftwareEngineer:  # parent for all other classes
    def __init__(self, name: str) -> None:  # como usar name
        self.name = name
        self.skills = []  # extended by the child classes

    def learn_skill(self, skill: str) -> None:
        self.skills.append(skill)
