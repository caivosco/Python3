class Fish:

 def __init__(self, first_name, last_name='Fish', skeleton='bone', eyelids=False):
  self.first_name = first_name
  self.last_name = last_name
  self.skeleton = skeleton
  self.eyelids = eyelids

 def swim(self):
  print('the fish is swmming')

 def swim_backwards(self):
  print('the fish can swin backwards')
