

import fish

class Trout(fish.Fish):

 pass

terry = Trout('Teerry')
print(terry.first_name)
print(terry.last_name)
print(terry.skeleton)
print(terry.eyelids)
terry.swim()
terry.swim_backwards()

