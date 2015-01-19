import webbrowser #import the webbrowser module
import time #import the time module

total_breaks = 3
break_count = 1
print ('This program started on '+time.ctime())
while (break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://codility.com") #this open the browser on a specific page
    break_count = break_count + 1
