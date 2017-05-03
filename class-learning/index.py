class Cat:
    def __init__(self, name,  color):
        self.name=name
        self.color=color
    def __add__(self, other):
        return Cat('Tom',  'brown-black')
    
    
fluffy=Cat('fluffy',  'brown')
jake=Cat('jake',  'black')
Tom= fluffy+jake
print(Tom.name)
del Cat
print(Tom.name)
asd=Cat('ss', 'sds')
