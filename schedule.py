import os
import re
from tkinter import *


command = "pdftotext -table raw_pdf.pdf"
os.system(command)

class Window(Frame):
	
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.master = master
		self.init_window()
	
	def init_window(self):
		
		self.master.title("Schedule Helper")
		
		self.pack(fill = BOTH, expand = 1)
		
		goButton = Button(self, text = "Go", command = self.client_go)
		
		goButton.place(x = 0, y = 0)
		
	def client_go(self):
		root.destroy()


	
root = Tk()
root.geometry("500x300")
app = Window(root)
root.mainloop()




subject = "STLC"

pattern = r"^" + subject + "-([-\d])"

regexObject = re.compile(pattern)

pdf = open("test_pdf.txt", "r")

for line in pdf:
	if re.match(pattern, line):
		print(line)



