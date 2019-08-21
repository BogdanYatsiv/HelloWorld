class Human:
    sex: str
    name: str
    def __init__(self,new_name:str):
        self.name = new_name

class Man(Human):
    sex = "male"

class Woman(Human):
    sex = "female"

def God():
    adam = Man("Adam")
    eve = Woman("Eve")
    human_list = []
    human_list.append(adam)
    human_list.append(eve)
    return human_list