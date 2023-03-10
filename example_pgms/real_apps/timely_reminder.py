import time
#import pymsgbox
import easygui

print("What do you want to get reminded")
text = str(input())

print("In how many minutes do you want to get reminded?")
timer = float(input())
print("The timer is set is", timer, "minute(s)")
timer = timer *60
time.sleep(timer)
print("This is time for", text)
#pymsgbox.alert('ScrumPost!', 'Alert')
#response = pymsgbox.prompt('Done?Click Ok')
easygui.msgbox("Reminder Msg for SCRUM POST!", title="ScrumPost")