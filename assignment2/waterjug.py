from collections import defaultdict
j1=4
j2=3
target=2
visited=defaultdict( lambda: False)
print(visited)
def water(am1, am2):
    if (am1==target and am2==0)or(am1==0 and am2==target):
        print(am1,am2)
        return True
    if visited[(am1,am2)]==False:
        print(am1,am2)
        visited[(am1,am2)]=True
        return((water(0,am2))or(water(am1,0)or))
    else:
        return False
        print('steps')