import os
import ctypes
import random
from VDA.Engine import StartUp


class AppOpener:
    """It can open multiple software when the user provides the path and also change the desktop background. """

    def OpenApplication(self):  # When user enter the path it will open the application .
        print("DEMO PATH : C:\\Program Files\\Microsoft VS Code\\Code.exe")
        path = input("Enter the path of Application you want to open.")
        os.startfile(path)

    def desktop_background(self):  # It changes the desktop background .
        lst_images = ["mountain.jpg", "wallpaper.jpg", "brown.jpg", "pink_beauty.jpg", "alone.jpg", "sun.jpg",
                      "city_beauty.jpg", "happy.jpg", "pokemon.jpg", "purple_beauty.jpg", "wheat.jpg", "paris.jpg"]
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, random.choice(lst_images), 0)
        StartUp().Speak("Desktop background is successfully changed")
        print("Desktop background is successfully changed!")
