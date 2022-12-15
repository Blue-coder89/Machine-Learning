import cv2
import mediapipe as mp
from math import sqrt
import os

def recordImages(videoFile,imageDirectory,Bias = 0):
    mpPose = mp.solutions.pose
    pose = mpPose.Pose()
    cap = cv2.VideoCapture(videoFile)
    i = 1 + Bias
    while True:
        background = cv2.imread('./black.webp')
        success,img = cap.read()
        img = cv2.flip(img,1)
        if success is False: break
        h,w,c = img.shape
        background = background.reshape((h,-1,3))
        background = background[:,0:w,:]
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results = pose.process(imgRGB)
        zl,zr,xl,xr,yl,yr = [None]*6
        if results.pose_landmarks:
            sxl,sxr,syl,syr = [None]*4
            for id,ln in enumerate(results.pose_landmarks.landmark):
                cx,cy = int(ln.x*w) ,int(ln.y*h)
                if id == 19:
                    zl = ln.z
                    xl = ln.x
                    yl = ln.y
                elif id == 20:
                    zr = ln.z
                    xr = ln.x
                    yr = ln.y
                if id == 23:
                    sxl = ln.x * w
                    syl = ln.y * h
                if id == 24:
                    sxr = ln.x * w
                    syr = ln.y * h
            if zl is None or zr is None: continue
            xc = (xl + xr)/2 
            yc = (yl + yr)/2
            cx = int(xc*w)
            cy = int(yc*h)
            Diameter = sqrt((sxl - sxr)**2 + (syr - syl)**2)
            Radius = int(1.4*Diameter)
            lox = max(cx - Radius,0)
            loy = max(cy - Radius,0)
            hix = min(cx + Radius,w)
            hiy = min(cy + Radius,h)
            background[loy:hiy,lox:hix] = img[loy:hiy,lox:hix]
        # cv2.imshow("Image",img)
        id = ""
        if i < 10: id = '000' + str(i)
        elif i < 100: id = '00' + str(i) 
        elif i < 1000: id = '0' + str(i)
        else: id = str(i)
        croppedImage = img[loy:hiy,lox:hix]
        croppedImage = cv2.resize(croppedImage,(200,200))
        pathc = os.path.join("ImageData2","Cropped",imageDirectory,"Image{}_Black_Red_cropped.jpg".format(id))
        patho = os.path.join("ImageData2","Original",imageDirectory,"Image{}_Black_Red_original.jpg".format(id))
        cv2.imwrite(pathc,croppedImage)
        cv2.imwrite(patho,img)
        i += 1
        # cv2.imshow("Image",background)
        cv2.waitKey(1)

# def recordTables(csvFile,imageDirectory,label,numRows = 500):
#     mpPose = mp.solutions.pose
#     pose = mpPose.Pose()
#     pathToImages = os.path.join('ImageData','Images')
#     pathToImages = os.path.join(pathToImages,imageDirectory)
#     files = os.listdir(pathToImages)
#     Images = []
#     ZLeft = []
#     ZRight = []
#     XLeft = []
#     XRight = []
#     YLeft = []
#     YRight = []
#     for file in files:
#         background = cv2.imread('./black.webp')
#         img = cv2.imread(os.path.join(pathToImages,file))
#         img = cv2.flip(img,1)
#         h,w,c = img.shape
#         background = background.reshape((h,-1,3))
#         background = background[:,0:w,:]
#         imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#         results = pose.process(imgRGB)
#         zl,zr,xl,xr,yl,yr = [None]*6
#         if results.pose_landmarks:
#             for id,ln in enumerate(results.pose_landmarks.landmark):
#                 cx,cy = int(ln.x*w) ,int(ln.y*h)
#                 if id == 19:
#                     zl = ln.z
#                     xl = ln.x
#                     yl = ln.y
#                 elif id == 20:
#                     zr = ln.z
#                     xr = ln.x
#                     yr = ln.y
#                 if id == 19 or id == 20:
#                     cv2.circle(img,(cx,cy),10,(255,0,0),cv2.FILLED)
#             if zl is None or zr is None: continue
#         cv2.imshow("Image",img)
#         Images.append(os.path.join(imageDirectory,file))
#         ZLeft.append(zl)
#         ZRight.append(zr)
#         if xl is not None: xl *= w
#         if xr is not None: xr *= w
#         if yl is not None: yl *= h
#         if yr is not None: yr *= h
#         XLeft.append(xl)
#         XRight.append(xr)
#         YLeft.append(yl)
#         YRight.append(yr)
#         cv2.waitKey(1)
#     Labels = [label]*len(Images)
#     dataDictionary = {'Images':Images,'label':Labels,'xl':XLeft,'yl':YLeft,'zl':ZLeft,'xr':XRight,'yr':YRight,'zr':ZRight}
#     dataFrame = pd.DataFrame(dataDictionary,columns=dataDictionary.keys())
#     dataFrame = dataFrame.head(numRows)
#     dataFrame.to_csv('ImageData\CSV\{}.csv'.format(csvFile))

def croppingDirectory(imageDirectory,numRows):
    Location = os.getcwd()
    pathc = os.path.join(Location,"ImageData2","Cropped",imageDirectory)
    patho = os.path.join(Location,"ImageData2","Original",imageDirectory)
    files = os.listdir(pathc)
    files.sort()
    l = len(files)
    print(l)
    for id in range(1,10):
        os.remove(os.path.join(pathc,'Image000' + str(id) + '_Black_Red_cropped.jpg'))
        os.remove(os.path.join(patho,'Image000' + str(id) + '_Black_Red_original.jpg'))
    for id in range(10,31):
        os.remove(os.path.join(pathc,'Image00' + str(id) + '_Black_Red_cropped.jpg'))
        os.remove(os.path.join(patho,'Image00' + str(id) + '_Black_Red_original.jpg'))
    for id in range(numRows+1,l+1):
        if id < 1000: 
            os.remove(os.path.join(pathc,'Image0' + str(id) + '_Black_Red_cropped.jpg'))
            os.remove(os.path.join(patho,'Image0' + str(id) + '_Black_Red_original.jpg'))
        else: 
            os.remove(os.path.join(pathc,'Image' + str(id) + '_Black_Red_cropped.jpg'))
            os.remove(os.path.join(patho,'Image' + str(id) + '_Black_Red_original.jpg'))


# try:
#     videoFile = os.path.join("VideoWithPalattesRing","Not Properly Held","NLeftBlackRed.mp4")
#     imageDirectory = os.path.join("Present_Black_Red","Not Properly Held","Left Hand") 
#     recordImages(videoFile,imageDirectory)
#     croppingDirectory(imageDirectory,1030)
# except Exception as e:
#     print('Error in NLeftBlackRed')
# try:
#     videoFile = os.path.join("VideoWithPalattesRing","Not Properly Held","NRightBlackRed.mp4")
#     imageDirectory = os.path.join("Present_Black_Red","Not Properly Held","Right Hand") 
#     recordImages(videoFile,imageDirectory)
#     croppingDirectory(imageDirectory,1030)
# except Exception as e:
#     print('Error in NRightBlackRed')
# try:
#     videoFile = os.path.join("VideoWithPalattesRing","Not Properly Held","NBothBlackRed.mp4")
#     imageDirectory = os.path.join("Present_Black_Red","Not Properly Held","Both Hands") 
#     recordImages(videoFile,imageDirectory)
#     croppingDirectory(imageDirectory,1030)
# except Exception as e:
#     print('Error in NBothBlackRed')
# try:
#     videoFile = os.path.join("VideoWithPalattesRing","Properly Held","Bottom","BottomRelaxedBlackRed.mp4")
#     imageDirectory = os.path.join("Present_Black_Red","Properly Held","Bottom","Relaxed") 
#     recordImages(videoFile,imageDirectory)
#     croppingDirectory(imageDirectory,1030)
# except Exception as e:
#     print('Error in BottomRelaxedBlackRed')
# try:
#     videoFile = os.path.join("VideoWithPalattesRing","Properly Held","Bottom","BottomCompressedBlackRed.mp4")
#     imageDirectory = os.path.join("Present_Black_Red","Properly Held","Bottom","Compressed") 
#     recordImages(videoFile,imageDirectory)
#     croppingDirectory(imageDirectory,1030)
# except Exception as e:
#     print('Error in BottomCompressedBlackRed')
try:
    videoFile = os.path.join("VideoWithPalattesRing","Properly Held","Front","FrontRelaxedBlackRed.mp4")
    imageDirectory = os.path.join("Present_Black_Red","Properly Held","Front","Relaxed") 
    recordImages(videoFile,imageDirectory)
    croppingDirectory(imageDirectory,1030)
except Exception as e:
    print('Error in FrontRelaxedBlackRed')
# try:
#     videoFile = os.path.join("VideoWithPalattesRing","Properly Held","Front","FrontCompressedBlackRed.mp4")
#     imageDirectory = os.path.join("Present_Black_Red","Properly Held","Front","Compressed") 
#     recordImages(videoFile,imageDirectory)
#     croppingDirectory(imageDirectory,1030)
# except Exception as e:
#     print('Error in FrontCompressedBlackRed')
try:
    videoFile = os.path.join("VideoWithPalattesRing","Properly Held","Left","LeftRelaxedBlackRed.mp4")
    imageDirectory = os.path.join("Present_Black_Red","Properly Held","Left","Relaxed") 
    recordImages(videoFile,imageDirectory)
    croppingDirectory(imageDirectory,1030)
except Exception as e:
    print('Error in LeftRelaxedBlackRed')
# try:
#     videoFile = os.path.join("VideoWithPalattesRing","Properly Held","Left","LeftCompressedBlackRed.mp4")
#     imageDirectory = os.path.join("Present_Black_Red","Properly Held","Left","Compressed") 
#     recordImages(videoFile,imageDirectory)
#     croppingDirectory(imageDirectory,1030)
# except Exception as e:
#     print('Error in LeftCompressedBlackRed')
try:
    videoFile = os.path.join("VideoWithPalattesRing","Properly Held","Right","RightRelaxedBlackRed.mp4")
    imageDirectory = os.path.join("Present_Black_Red","Properly Held","Right","Relaxed") 
    recordImages(videoFile,imageDirectory)
    croppingDirectory(imageDirectory,1030)
except Exception as e:
    print('Error in RightRelaxedBlackRed')
try:
    videoFile = os.path.join("VideoWithPalattesRing","Properly Held","Right","RightCompressedBlackRed.mp4")
    imageDirectory = os.path.join("Present_Black_Red","Properly Held","Right","Compressed") 
    recordImages(videoFile,imageDirectory)
    croppingDirectory(imageDirectory,1030)
except Exception as e:
    print('Error in RightCompressedBlackRed')
try:
    videoFile = os.path.join("VideoWithPalattesRing","Properly Held","Top","TopRelaxedBlackRed.mp4")
    imageDirectory = os.path.join("Present_Black_Red","Properly Held","Top","Relaxed") 
    recordImages(videoFile,imageDirectory)
    croppingDirectory(imageDirectory,1030)
except Exception as e:
    print('Error in TopRelaxedBlackRed')
try:
    videoFile = os.path.join("VideoWithPalattesRing","Properly Held","Top","TopCompressedBlackRed.mp4")
    imageDirectory = os.path.join("Present_Black_Red","Properly Held","Top","Compressed") 
    recordImages(videoFile,imageDirectory)
    croppingDirectory(imageDirectory,1030)
except Exception as e:
    print('Error in TopCompressedBlackRed')

