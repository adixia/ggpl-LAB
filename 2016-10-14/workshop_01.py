
# coding: utf-8

# In[1]:

from pyplasm import *


# In[2]:

def createBeamsAndPillars(beamSec,pillarSec,distanceBtwPill,eightsBeam):
    maxHeight= SUM(eightsBeam)+beamSec[1]
    pillarLong=CUBOID([pillarSec[0],pillarSec[1],maxHeight]) 
    pillars=[]
    floor=[]
   
    for d in range(len(distanceBtwPill)):
        pillars.append(pillarLong)
        floor.append(T(2)(pillarSec[1]))
        
        for h in range(len(eightsBeam)):
            beam=CUBOID([beamSec[0],distanceBtwPill[d],beamSec[1]])
            floor.append(T(3)(eightsBeam[h]))
            floor.append(beam)
       
    
        floor.append(T(2)(pillarSec[1]))  
        img=STRUCT(floor) 
        floor=[]
        if d != len(distanceBtwPill)-1:
            pillars.append(img)
        img=[]
        pillars.append(T(2)(distanceBtwPill[d]+pillarSec[1]))
    
    final=STRUCT(pillars)
    return final


# 

# In[3]:

beamSec=(0.5,0.5) #bx,bz 
pillarSec=(0.5,0.5) #px,py 
distanceBtwPill=[1,1,1,4,3]
eightsBeam= [1,1,1,1,1,1,1]


# In[4]:

k=createBeamsAndPillars(beamSec,pillarSec,distanceBtwPill,eightsBeam)
VIEW(k)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# ### 

# In[ ]:



