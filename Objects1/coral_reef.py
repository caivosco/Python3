class Coral:
 def community(self):
  print('coral lives in a community')

class Anemone:
 def protect_clownfish(self):
  print('the anemone is protecting clownfish')

class CoralReef(Coral, Anemone):
 pass

great_barrier = CoralReef()
great_barrier.community()
great_barrier.protect_clownfish()

