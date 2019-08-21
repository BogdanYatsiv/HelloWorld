class Person:
    info:str
    def __init__(self,new_name:str,new_age:int):
        self.info = f"{new_name}s age is {new_age}"