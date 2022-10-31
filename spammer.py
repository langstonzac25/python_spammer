#imports the py auto gui and time modules.
import pyautogui, time
#Lets you get to the app that you want to spam.
time.sleep(5)

#The file "spam.txt" is the file that will be spammed.
f = open("spam.txt", 'r')
for word in f:
    pyautogui.typewright(word)
    pyautogui.press("enter")