import pygame          
import pygame.camera
import datetime
import time

pygame.camera.init()

# make the list of all available cameras 
camlist = pygame.camera.list_cameras() 
  
# if camera is detected or not 
if camlist: 
  
    # initializing the cam variable with default camera 
    cam = pygame.camera.Camera(camlist[0], (640, 480)) 
  
    # opening the camera 
    cam.start() 
    # capturing the single image 
    image = cam.get_image() 
  
    # saving the image 
    pygame.image.save(image, "bmo.jpg")
    cam.stop
  
# if camera is not detected the moving to else part 
else: 
    print("No camera on current device") 