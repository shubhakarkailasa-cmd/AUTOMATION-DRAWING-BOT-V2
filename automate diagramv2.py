import pyautogui
import cv2
import time
time.sleep(5)
image=cv2.imread('image.png')
if image is None:
    quit()
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edges1=cv2.Canny(gray,100,255)
contour,_=cv2.findContours(edges1,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
canvas_x,canvas_y=pyautogui.position()
for cnt in contour:
        pyautogui.mouseDown()
        for point in cnt:
            x,y=point[0]
            pyautogui.dragTo(canvas_x+int(x),canvas_y+int(y))
        pyautogui.mouseUp()
print(contour)
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()



