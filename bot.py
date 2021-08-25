import time
from direct_input import PressKey, ReleaseKey

LEFT = 0xCB
RIGHT = 0xCD
F = 0x21
D = 0x20

F1 = 0x3B
S = 0x1F


def flush():
    ReleaseKey(S)
    ReleaseKey(D)
    ReleaseKey(F)

    ReleaseKey(F1)
    ReleaseKey(LEFT)
    ReleaseKey(RIGHT)


class Bot:
    def __init__(self):
        # left, right, a, b
        self.prev_keys = [0, 0, 0, 0]

        self.active_keys = [0, 0, 0, 0]
        self.keys = [LEFT, RIGHT, F, D]

    @staticmethod
    def setup():
        flush()

        time.sleep(0.5)

        PressKey(F1)
        time.sleep(0.05)
        ReleaseKey(F1)

        time.sleep(0.5)
        PressKey(S)
        time.sleep(0.05)
        ReleaseKey(S)

    def act(self, dt, arr):
        if dt >= arr["times"]:
            arr = [arr["left"], arr["right"], arr["f"], arr["d"]]
            for i, val in enumerate(arr):
                if self.active_keys[i] != val:
                    if val == 0:
                        ReleaseKey(self.keys[i])
                        self.active_keys[i] = 0
                    else:
                        PressKey(self.keys[i])
                        self.active_keys[i] = 1

            return True
        else:
            return False

    def press(self, key: int):
        if self.active_keys[key] == 0:
            self.active_keys[key] = 1

            PressKey(self.keys[key])
            # pyautogui.keyDown(self.buttons[key])

    def release(self, key: int):
        if self.active_keys[key] == 1:
            self.active_keys[key] = 0

            time.sleep(0.001)
            ReleaseKey(self.keys[key])

    def pause(self):
        PressKey(S)
        time.sleep(0.05)
        ReleaseKey(S)
