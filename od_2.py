from tkinter import * 
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename 
from PIL import Image


import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox


root = Tk() 
root.geometry('200x100')
filename=''

# This function will be used to open 
# file in read mode and only Python files 
# will be opened 
def open_file():
    global filename
    filename =askopenfilename(title='Select image source',filetypes=(('jpeg files', '*.jpg'), ('all files', '*.*')))
    if filename:
        #file_selection_string.set(self.filename.split('/')[-1])
        img = Image.open(filename)




def convert_file():
	im = cv2.imread(filename)
	bbox, label, conf = cv.detect_common_objects(im)
	output_image = draw_bbox(im, bbox, label, conf)
	plt.imshow(output_image)
	plt.show()



btn = Button(root, text ='Select File', command = lambda:open_file()) 
btn.pack(side = TOP, pady = 10)

btn2 = Button(root, text ='Convert File', command = lambda:convert_file()) 
btn2.pack(side = TOP, pady = 15)
  
mainloop() 
