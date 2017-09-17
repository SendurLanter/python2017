
# coding: utf-8

# In[1]:


from vpython import*
face = sphere()
right = sphere(pos=vector(0.8,0.8,0.8),radius=0.3,color=color.yellow)
left = sphere(pos=vector(-0.8,0.8,0.8),radius=0.3,color=color.yellow)
eye1 = sphere(pos=vector(0.3,0.3,1.2),radius=0.15,color=color.red)
eye2 = sphere(pos=vector(-0.3,0.3,1.2),radius=0.15,color=color.red)
nose = sphere(pos=vector(0,0,1.2),radius=0.05,color=color.green)
mouse = ellipsoid(pos=vector(0,-0.3,1),size=vector(1.2,0.27,0.27),color=color.blue)

