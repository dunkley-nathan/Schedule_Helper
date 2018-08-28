import os
import re
from tkinter import *


command = "pdftotext -table raw_pdf2.pdf"
os.system(command)


	
def client_go():
		root.destroy()
		
def submit():
		submit.subject = entrySubject.get()
		submit.classNum = entryClass.get()
		client_go()

		
root = Tk()
root.title("Schedule Helper")
		
Label(text = "Subject Abreviation:  (ex: MATH, CSCE)").grid(row = 0)
Label(text = "Class Number:  (ex: 151, 304)").grid(row = 1, sticky = W)

entrySubject = Entry(root, width = 8)
entryClass = Entry(root, width = 8)

entrySubject.grid(row = 0, column = 1)
entryClass.grid(row = 1, column = 1)
		
Button(root, text = "Submit", command = submit).grid(row = 2, column = 1)

root.geometry("400x300")
root.mainloop()



pattern = r"^" + submit.subject + "-" + submit.classNum + "-" + "([-\d])"

regexObject = re.compile(pattern)

pdf = open("raw_pdf2.txt", "r")

for line in pdf:
	if re.match(pattern, line):
		print(line)



