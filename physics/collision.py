import math
class Particle:
        def __init__(self, name, position, velocity, mass):
                self.name = name
                self.position = position
                self.velocity = velocity
                self.mass = mass
                self.radius = math.sqrt(mass)
class Wall(Particle):
        def __init__(self, *args, **kw):
                super(Wall, self).__init__(*args, **kw)
                self.radius = 15
def collision(a, b):
        if a.position <= b.position:
                if a.velocity > b.velocity:
                        result = elasticresult(a,b)
                else:
                        result = "no collision"
        if a.position > b.position:
                if a.velocity < b.velocity:
                        result = elasticresult(a,b)
                else:
                        result = "no collision"

        print(result)

def elasticresult(a, b):
        temp = a.velocity
        a.velocity = ((2 * b.mass * b.velocity
                       + a.mass * a.velocity - b.mass * a.velocity)
                        /(a.mass + b.mass))
        b.velocity = ((2 * a.mass * temp
                       + b.mass * b.velocity - a.mass * b.velocity)
                       /(a.mass + b.mass))
        return (a.name + "'s new velocity is " + str(a.velocity) + '\n'
                + b.name + "'s new velocity is " + str(b.velocity))



