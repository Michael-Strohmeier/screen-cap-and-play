import time
#
import pyautogui
import win32gui


class Capture:
    def __init__(self, window_title: str):
        # window_title = window_title.encode("unicode_escape")
        self.hwnd = win32gui.FindWindow(None, window_title)

        win32gui.SetForegroundWindow(self.hwnd)

        menu_bar_offset = 16

        x_0, y_0, x_1, y_1 = self.get_window_dimensions()
        self.region = (x_0, y_0 + menu_bar_offset, x_1, y_1 - menu_bar_offset)

        # don't feel like dealing with the status bar at the bottom of the jnes emulator so...
        if "jnes" in window_title.lower():
            self.region = (x_0, y_0 + menu_bar_offset - 10, x_1, y_1 - menu_bar_offset - 24)

    def get_window_dimensions(self):
        x_0, y_0, x_1, y_1 = win32gui.GetClientRect(self.hwnd)
        x_0, y_0 = win32gui.ClientToScreen(self.hwnd, (x_0, y_0))
        x_1, y_1 = win32gui.ClientToScreen(self.hwnd, (x_1 - x_0, y_1 - y_0))

        return x_0, y_0, x_1, y_1

    def get_window(self):
        return pyautogui.screenshot(region=self.region)
