import pyscreenshot as ImageGrab
import pyautogui
import time
n=155001 #設定
while n<=155155: #設定
    time.sleep(10) #設定
    strname = str(n) + ".png"
    image = ImageGrab.grab()
    image.save(strname)
    #pyautogui.click(button='left')
    pyautogui.press('left') #設定
    n+=1
print("finish")
