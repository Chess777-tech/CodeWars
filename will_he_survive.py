"""
A hero is on his way to the castle to complete his mission. 
However, he's been told that the castle is surrounded with a couple of powerful dragons! 
each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. 
Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?
Return true if yes, false otherwise :)
"""


def hero(bullets,dragons):
    required_bullets = dragons * 2
    return bullets >= required_bullets


result = hero(100,50)
result2 = hero(50,100)
print(result)
print(result2)
