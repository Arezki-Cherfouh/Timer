import time
import pygame
import os
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "finish.mp3"))
while True:
    fromexceed=False
    try:
        timer=input("Set a timer:\n>>> ")
        if timer.find(":"):
            try:
                s=timer.split(":")
                if len(s)==2:
                    timer=int(s[0])*60+int(s[1])
                elif len(s)==3:
                    timer=(int(s[0])*60)*60+int(s[1])*60+int(s[2])
                elif len(s)>3:
                    print("Timer only supports hours!")
                    fromexceed=True
                    pass
            except ValueError:
                print("Invalid input")
                pass
        try:
            timer=int(timer)
            for i in range(timer):
                print(f"{timer}")
                timer-=1
                time.sleep(1) 
            pygame.mixer.music.play()
        except ValueError:
            if not fromexceed:
                print("Invalid input")
            pass
    except KeyboardInterrupt:
        print("\nExiting...")
        break