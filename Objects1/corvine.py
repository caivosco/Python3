

import fish

class Corvine(fish.Fish):
 def __init__(self, water = 'freshwater'):
  self.water = water
  super().__init__(self)

sammy = Corvine() 
sammy.first_name='Sammy'

print(sammy.last_name)
sammy.swim()
sammy.swim_backwards()
print(sammy.eyelids)
print(sammy.water)
print(sammy.skeleton)
