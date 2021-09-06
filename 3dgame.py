# from math import trunc
# from direct.showbase.PythonUtil import fitSrcAngle2Dest
# from numpy import positive
from ursina import *

def update():
    firstEntity.rotation_y+=50*time.dt
    firstEntity.position+=firstEntity.forward*time.dt

#window.fullscreen=True #전체화면
window.borderless=False #테두리창 
app=Ursina()
firstEntity=Entity(model='cube',color=color.rgb(255,0,0),texture='brick',
                                                         position=(0,0,0),
                                                         rotation=(0,0,0),
                                                         scale=2,
                                                         )
secondEntity=Entity(parent=firstEntity,
                    model='sphere',
                    position=(1,1,1),
                    )


EditorCamera()
app.run() 