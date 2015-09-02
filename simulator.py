from tkinter import *

from physics import collision
import turtle


a = collision.Particle("apple", 0, 500, 1000)
b = collision.Particle("orange", 200, 0, 100)
#c = collision.Particle("banana", -20, 0, 100)

leftwall = collision.Wall("leftwall", -300, 0, 1000000000)
rightwall = collision.Wall("rightwall", 300, 0, 1000000000)

particles = [a,b,leftwall,rightwall] #particle list

#initialization
root = Tk()
root.title("1D collision simulation")
v = StringVar()
v.set("Total Kinectic Energy = ")
info = Message(root, textvariable = v, width=500)
info.pack()
canvas = Canvas(root, width = 800, height = 500)
canvas.pack()


obj = []
for p in particles:
    temp = turtle.RawTurtle(canvas)
    obj.append(temp)
    if type(p) is collision.Particle:
        temp.shape("circle")
        temp.speed(0)
        temp.up()
        temp.shapesize(p.radius/10, p.radius/10, None)
    if type(p) is collision.Wall:
        temp.shape("square")
        temp.speed(0)
        temp.up()
        temp.shapesize(15,1.5, None)

tincrement = 0.05

while True:
    index = 0
    for o in obj :
        o.setpos(particles[index].position, 0)
        particles[index].position += particles[index].velocity * tincrement
        index += 1
        
    templist = list(particles)
    totalk = 0
    for p in particles :
        totalk += 0.5 * p.mass * p.velocity**2
        templist.pop(0)
        for w in templist :
            impactdistance = (p.radius + w.radius)
            if p is not w and abs(p.position - w.position) <= impactdistance :  
                collision.collision(p,w)            
    v.set("Total kinectic energy = "+ str(totalk))
    

