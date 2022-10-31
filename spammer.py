#imports the py auto gui and time modules.
import pyautogui, time
#Lets you get to the app that you want to spam.
time.sleep(5)
f = open("spam.txt", 'r')
for word in f:
	pyautogui.press("enter")
    pyautogui.typewrite(word)