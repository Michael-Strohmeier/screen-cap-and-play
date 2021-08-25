"""
pip install opencv-python
pip install PyAutoGUI
pip install pywin32
pip install numpy
pip install psutil
pip install pynput
"""

import os
import time

import cv2
from PIL import Image
import numpy as np
import pandas as pd

from capture import Capture
from bot import Bot, flush

if __name__ == "__main__":
    i = 0
    key_strokes = pd.read_csv("data.csv")

    window_title = "Jnes 1.2"

    try:
        cap = Capture(window_title=window_title)
    except:
        rom_path = "E:\\ROMs\\Super Mario Bros. (World).nes"
        os.startfile(rom_path)

        time.sleep(3)

        cap = Capture(window_title=window_title)

    bot = Bot()

    bot.setup()
    time.sleep(3.05)

    images = []

    start_time = time.time()
    while i < len(key_strokes):
        dt = time.time() - start_time

        window = cap.get_window()
        np_window = np.array(window)

        if bot.act(dt, arr=key_strokes.iloc[i]):
            i += 1

        """cv2.imshow("screen", np_window)
        if (cv2.waitKey(1) & 0xFF) == ord("q"):
            cv2.destroyAllWindows()
            break"""

        img = Image.fromarray(np.uint8(np_window)).convert('RGB')


        images.append(img)

    flush()

    img.save("out.gif", save_all=True, append_images=images)

