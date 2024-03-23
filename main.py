import pyautogui
import time
import cv2
import pytesseract
# pyautogui.typewrite(number)


class Parser:
	def __init__(self):
		self.global_delay = 0.01
		self.number_segment = "050694"
		self.number_part = 10
		self.current_number = ""
		self.TIMEOUT = 0.02


	def CheckUnknown(self):
		screen = pyautogui.screenshot(region = (390, 88, 200, 40))
		text = pytesseract.image_to_string(screen)
		# print(text)
		if "Unknown" in text:
			return True
		else: 
			return False


	def ViberCheck(self):
		pyautogui.click(x=38, y=60)	#клік по іконкі профілю
		time.sleep(self.global_delay)
		pyautogui.click(x=126, y=265)	#клік по іконкі клави
		time.sleep(self.global_delay)

		pyautogui.typewrite(self.current_number)	#ВСтавка номера
		time.sleep(self.global_delay)

		pyautogui.click(x=229, y=508)	#клік по іконкі повідомлення
		time.sleep(self.global_delay)



	def WriteName(self):
		screen = pyautogui.screenshot(region=(453, 95, 350, 37))
		text = pytesseract.image_to_string(screen, lang="ukr+eng")
		return text.replace("\n", "")


	def GoParse(self):
		for x in range(0, 1000):
			self.current_number = self.number_segment + str(x).zfill(4)
			self.ViberCheck()
			# exist = not self.CheckUnknown()
			name = str(self.WriteName())
			if "nown" in name:
				continue
			print(f"{name} - {self.current_number}")
			with open("numbers.txt", "a", encoding="utf-8") as file:
				file.write(f"{name}-{self.current_number}\n")
				file.close()
			time.sleep(self.TIMEOUT)



parser = Parser()
# parser.ViberCheck()
# parser.CheckUnknown()
parser.GoParse()