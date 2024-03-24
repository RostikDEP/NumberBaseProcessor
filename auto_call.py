import keyboard
import pyautogui
import pyperclip
import time

def make_call():
	delay = 0.5
	pyautogui.hotkey('ctrl', 'c')
	pyautogui.click(x=704, y=1045) #click phone icon
	time.sleep(delay)
	pyautogui.click(x=747, y=71) #click to keyboard icon
	time.sleep(delay)
	pyautogui.typewrite(pyperclip.paste())
	time.sleep(delay)
	pyautogui.click(x=1675, y=884) #click call button

def on_key_event(event):
	if event.event_type == keyboard.KEY_DOWN and event.name == 'insert':
		make_call()

def main():
	keyboard.on_press(on_key_event)
	try:
		keyboard.wait('f12')  
	except KeyboardInterrupt:
		pass
	finally:
		keyboard.unhook_all()

if __name__ == "__main__":
	main()
