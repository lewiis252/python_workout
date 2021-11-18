import pyautogui
import time
import os

num_of_minutes = int(input('Podaj czas trwania wykładu w minutach: '))
lecture_title = ((input('Podaj tytuł wykładu: ')).replace(' ', '_'))
wait_beetwen_screen = float(input('Co ile sekund wykonać screenshot? : '))

if not os.path.exists(lecture_title):
    os.mkdir(lecture_title)
    print("Directory " , lecture_title ,  " Created ")
else:
    print("Taki folder " , lecture_title ,  " już istnieje!!!! Nadpiszę dane!!! Kontynuować?")
    answer = input('[tak]/[nie]: ')
    if answer == 'nie':
        quit()

i = 1
status = True

stop_cond = num_of_minutes*60/wait_beetwen_screen

while status:
    if i == stop_cond:
        status = False
    my_screen_shot = pyautogui.screenshot()
    file_num = str(i)
    my_screen_shot.save(f'{lecture_title}\{str(lecture_title)}_{file_num}.png')
    print('screenshot saved')

    time.sleep(wait_beetwen_screen)

    i+=1
print('Pamiętaj skopiować screeny w bezpieczne miejsce, nie chcesz przypadkiem ich nadpisać!!!')
