import pyautogui
import time
import os
import matplotlib.pyplot as plt
import PIL
from PIL import Image
import numpy as np

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
    elif i == 1:
        # time.sleep(3)  # wait 3 seconds before first screenshot
        my_screen_shot = pyautogui.screenshot()
        file_num = str(i)
        my_screen_shot.save(f'{lecture_title}/{str(lecture_title)}_{file_num}.png')
        print('Zrzut ekranu zapisany')

        i += 1
        time.sleep(wait_beetwen_screen)


    else:
        my_screen_shot = pyautogui.screenshot()
        file_num = str(i)
        previous_file_num = str(i-1)
        my_screen_shot.save(f'{lecture_title}/{str(lecture_title)}_{file_num}.png')

        # compare if screenshot have changed
        previous_img = (np.asarray(Image.open(f'{lecture_title}/{str(lecture_title)}_{previous_file_num}.png')))
        current_img = (np.asarray(Image.open(f'{lecture_title}/{str(lecture_title)}_{file_num}.png')))

        if np.array_equal(previous_img, current_img):
            os.remove(f'{lecture_title}/{str(lecture_title)}_{file_num}.png')
            print('Kopia poprzedniego zrzutu usunięta')

        else:
            print('Zrzut ekranu zapisany')
            i += 1

        time.sleep(wait_beetwen_screen)


print('Pamiętaj skopiować screeny w bezpieczne miejsce, nie chcesz przypadkiem ich nadpisać!!!')






