import os

def makeDir(dir):
    Location = os.getcwd()
    patho = os.path.join(Location,"ImageData2","Original",dir)
    pathc = os.path.join(Location,"ImageData2","Cropped",dir)
    os.mkdir(patho)
    os.mkdir(pathc)
    pathonp = os.path.join(patho,"Not Properly Held")
    pathop = os.path.join(patho,"Properly Held")
    pathcnp = os.path.join(pathc,"Not Properly Held")
    pathcp = os.path.join(pathc,"Properly Held")
    os.mkdir(pathonp)
    os.mkdir(pathop)
    os.mkdir(pathcnp)
    os.mkdir(pathcp)
    os.mkdir(os.path.join(pathonp,"Both Hands"))
    os.mkdir(os.path.join(pathonp,"Left Hand"))
    os.mkdir(os.path.join(pathonp,"Right Hand"))
    os.mkdir(os.path.join(pathcnp,"Both Hands"))
    os.mkdir(os.path.join(pathcnp,"Left Hand"))
    os.mkdir(os.path.join(pathcnp,"Right Hand"))
    pathopFront = os.path.join(pathop,"Front")
    pathopTop = os.path.join(pathop,"Top")
    pathopBottom = os.path.join(pathop,"Bottom")
    pathopRight = os.path.join(pathop,"Right")
    pathopLeft = os.path.join(pathop,"Left")
    os.mkdir(pathopFront)
    os.mkdir(pathopTop)
    os.mkdir(pathopBottom)
    os.mkdir(pathopLeft)
    os.mkdir(pathopRight)
    pathcpFront = os.path.join(pathcp,"Front")
    pathcpTop = os.path.join(pathcp,"Top")
    pathcpBottom = os.path.join(pathcp,"Bottom")
    pathcpRight = os.path.join(pathcp,"Right")
    pathcpLeft = os.path.join(pathcp,"Left")
    os.mkdir(pathcpFront)
    os.mkdir(pathcpTop)
    os.mkdir(pathcpBottom)
    os.mkdir(pathcpLeft)
    os.mkdir(pathcpRight)
    os.mkdir(os.path.join(pathopFront,"Relaxed"))
    os.mkdir(os.path.join(pathopFront,"Compressed"))
    os.mkdir(os.path.join(pathopTop,"Relaxed"))
    os.mkdir(os.path.join(pathopTop,"Compressed"))
    os.mkdir(os.path.join(pathopBottom,"Relaxed"))
    os.mkdir(os.path.join(pathopBottom,"Compressed"))
    os.mkdir(os.path.join(pathopRight,"Relaxed"))
    os.mkdir(os.path.join(pathopRight,"Compressed"))
    os.mkdir(os.path.join(pathopLeft,"Relaxed"))
    os.mkdir(os.path.join(pathopLeft,"Compressed"))
    os.mkdir(os.path.join(pathcpFront,"Relaxed"))
    os.mkdir(os.path.join(pathcpFront,"Compressed"))
    os.mkdir(os.path.join(pathcpTop,"Relaxed"))
    os.mkdir(os.path.join(pathcpTop,"Compressed"))
    os.mkdir(os.path.join(pathcpBottom,"Relaxed"))
    os.mkdir(os.path.join(pathcpBottom,"Compressed"))
    os.mkdir(os.path.join(pathcpRight,"Relaxed"))
    os.mkdir(os.path.join(pathcpRight,"Compressed"))
    os.mkdir(os.path.join(pathcpLeft,"Relaxed"))
    os.mkdir(os.path.join(pathcpLeft,"Compressed"))

makeDir('Present_Black_Red')
    