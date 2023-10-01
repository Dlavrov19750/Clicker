import time
import threading
from turtle import left
import os
import button as button
import clicking as clicking
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode, Key
from time import perf_counter
import pyautogui
import keyboard
os.chdir(r'C:\Python programs\PycharmProjects\Clicker')
start = perf_counter()
toggle_key = KeyCode(char='/')

clicking = False
mouse = Controller()


def clicker():
	while True:
		if clicking:
			mouse.click(Button.left, 1)
			time.sleep(0.2)


def toggle_event(key):
	if key == toggle_key:
		global clicking
		end = perf_counter()
		print(end - start)
		clicking = not clicking


def main():
	clicking_thread = threading.Thread(target=clicker)
	clicking_thread.start()

	with Listener(on_press=toggle_event) as listener:
		listener.join()


print('Должно работать')



if __name__ == '__main__':
	main()
