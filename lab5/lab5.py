
# coding: utf-8

# In[1]:


from vpython import *
g=9.8
size=0.25
height=15.0
scene = display(width=8000,height=8000,center=(0,height/2.0),background=(0.5,0.5,0))
floor = box(length=30,height=0.01,width=10,color=color.blue)
ball=sphere(radius=size,color=color.red)
ball.pos=vector(-15,2,0)
ball.v=vector(8,8,0)
dt=0.001
A=arrow(shaftwidth=0.1)
count=0
while ball.pos.y>=size:    
    A.pos=ball.pos+vector(0.25,0,0)
    A.axis=1.5*ball.v
    count+=dt
    rate(1000)
    ball.v.y+=-g*dt
    ball.pos.x+=ball.v.x*dt
    ball.pos.y+=ball.v.y*dt
print (count)
    

