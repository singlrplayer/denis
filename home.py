"""denis sergeiev 5-A"""
from turtle import *

width(2)
color('black')

def p(d,i,o,l): #прямо кутник
    up()
    setpos(d,i)
    down()
    setpos(o,i)
    setpos(o,l)
    setpos(d,l)
    setpos(d,i)

p(150,-175, -200, 125)
p(-125,75,-25,-50 )
p(50,-25,150,-175)
p(-175,-100,25,-175)
p(-125,-125,-100,-175)
p(-50,-125,-25,-175)
p(100,-150,75,-175)



def r(p,t,d,s,b,l): #три кутник
    up()
    setpos(p,t)
    down()
    setpos(d,s)
    setpos(b,l)
    setpos(p,t)
    
r(-200,125,-25,350,150,125)
r(40,275,100,275,100,200)
r(-175,-100,-150,-75,-125,-100)
r(-100,-100,-75,-75,-50,-100)
r(-25,100,0,75,25,100)
r(-25,-100,0,-75,25,-100)



def i(r,t,o):# круг
    up()
    goto(r,t)
    down()
    circle(o)

i(-25,175,50)
i(75,-100,5)


def e(y,l,f,d,s,a,e,r): #рисочки
    up()
    goto(y,l)
    down()
    setpos(f,d)
    up()
    goto(s,a)
    down()
    setpos(e,r)
    
e(-125,25,-25,25,-75,75,-75,-50)
e(-25,275,-25,175,-75,225,25,225)   


up()
goto(-200,-350)
down()
write("denis sergeiev 5-a class:)")
done()
