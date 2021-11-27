import pyautogui
import time
import os

num_of_minutes = int(input('Enter duration of lecture (minutes): '))
lecture_title = ((input('Enter name of lecture: ')).replace(' ', '_'))
wait_beetwen_screen = float(input('How long to wait between next screenshot (for example 5) (seconds): '))

if not os.path.exists(lecture_title):
    os.mkdir(lecture_title)
    print("Directory " , lecture_title ,  " Created ")
else:
    print("This directory " , lecture_title ,  " Already exist. I will overwitten it and files in that directory. Are you sure to continue?")
    answer = input('[yes]/[no]: ')
    if answer == 'no':
        quit()

i = 1
status = True

stop_cond = num_of_minutes*60/wait_beetwen_screen

while status:
    if i == stop_cond:
        status = False
    my_screen_shot = pyautogui.screenshot()
    file_num = str(i)
    my_screen_shot.save('{}\{}_{}.png'.format(lecture_title, str(lecture_title), file_num))
    print('screenshot saved')

    time.sleep(wait_beetwen_screen)

    i+=1
print('Remember to copy screenshots to safe location. You may accidentaly overwrite it.')
