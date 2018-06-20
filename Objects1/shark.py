import fish

class Shark(fish.Fish):
 def __init__(self,first_name,last_name='Shark',skeleton='cartilage'):
  self.first_name=first_name
  self.last_name=last_name
  self.skeleton=skeleton

 def swim_backwards(self):
  print('the shark cannot swim backwards, only skin and sink')

sammy = Shark("Sammy")
print(sammy.first_name + " " + sammy.last_name)
sammy.swim()
sammy.swim_backwards()

print(sammy.skeleton)
