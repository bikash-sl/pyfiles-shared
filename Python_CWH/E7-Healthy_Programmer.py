"""
Healthy Programmer
9am - 5pm
Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
Physical activity - physical.mp3 every - 45 min - ExDone - log
Rules
Pygame module to play audio
"""

# my solution using schedule module (external)
from pygame import mixer
import time
import schedule

notification = ["Eye exercises", "Water break", "Physical exercises"]
tune = ["eyes.ogg", "water.ogg", "exercise.ogg"]


def current_time():
    import datetime
    return datetime.datetime.now().strftime("%d-%b-%Y \t %I:%M %p")


def musicplay(music_file, notice):
    mixer.init()
    mixer.music.load(music_file)
    mixer.music.play(-1)
    while True:
        user_input = input(f"Enter 'done' if you have done {notice}: ")
        if user_input == "done":
            mixer.music.stop()
            break


def logger(notice):
    with open("Health_logger.txt", "a") as log:
        log.write(f"{current_time()} \t\t {notice}\n")


def eye_exercise():
    musicplay(tune[0], notification[0])
    logger(notification[0])


def water_break():
    musicplay(tune[1], notification[1])
    logger(notification[1])


def phy_exercise():
    musicplay(tune[2], notification[2])
    logger(notification[2])


schedule.every(33).minutes.do(eye_exercise)
schedule.every(45).minutes.do(water_break)
schedule.every(58).minutes.do(phy_exercise)

while True:
    schedule.run_pending()
    time.sleep(1)

"""
# Harry's solution
from pygame import mixer
from datetime import datetime
from time import time


def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break


def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    # musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40*60
    exsecs = 30*60
    eyessecs = 45*60

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes > eyessecs:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musiconloop('eyes.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musiconloop('physical.mp3', 'donephy')
            init_exercise = time()
            log_now("Physical Activity done at")
"""
