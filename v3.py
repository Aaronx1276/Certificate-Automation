from tkinter import *
from PIL import ImageTk
import os
import PIL.Image
from PIL import ImageDraw
from PIL import ImageFont
from tkcalendar import Calendar

root = Tk()
root.title("Certificate Automation")
root.geometry("410x350+500+50")
image = PIL.Image.open("./xielogo.png")
resizedImg = image.resize((350, 250))
img = ImageTk.PhotoImage(resizedImg)
panel = Label(root, image = img)

def generateCertificate(date: str):
    str_dt = StringVar()

    img = PIL.Image.open('template1.jpg')
 
    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('FreeMono.ttf', 65)
 
    I1.text((400, 420), name_var.get(),font=myFont,   fill =(0, 0, 0),stroke_width=0, spacing=1)
    # str_dt = date.strftime("%d-%m-%Y")

    I2 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('FreeMono.ttf', 24)
    I2.text((710,570), date,font=myFont,   fill = (0,0,0),stroke_width=0, spacing=1)
    
    I3 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('FreeMono.ttf', 40,)
    I2.text((800,510), Event_var.get(),font=myFont,   fill =(0, 0, 0),stroke_width=0, spacing=1)

    
    # Display edited image
    img.show()
    
    img.save("certificate.jpg")
    

def nextscreen():
    root.withdraw()
    s = Toplevel()
    s.title("Certificate Automation")
    s.geometry('400x800+500+50')

    image = PIL.Image.open("./xielogo.png")
    resizedImg = image.resize((350, 250))
    img = ImageTk.PhotoImage(resizedImg)

    # reading the image
    canvas = Canvas(s, width=300, height=200)
    canvas.pack()
    img=ImageTk.PhotoImage(file="./xielogo.png")
    canvas.create_image(150,100,image=img)
    canvas.image = img


    # panel = Label(s, image = img)

    # setting the application
    # panel.pack()
    myLabel = Label(s, text="")
    myLabel.pack()



    myLabel = Label(s, text="Candidate name")
    myLabel.pack()

    myTextbox = Entry(s, width=30, textvariable = name_var)
    myTextbox.pack()

    myLabel = Label(s, text="")
    myLabel.pack()

    myLabel = Label(s, text="Date")
    myLabel.pack()
    cal = Calendar(s, selectmode = 'day',
               year = 2020, month = 5,
               day = 22,date_pattern="dd-MM-yyyy",)
    
 
    cal.pack(pady = 20)
   


    myLabel = Label(s, text="")
    myLabel.pack()

    
    myLabel = Label(s, text="Event")
    myLabel.pack()

    myTextbox = Entry(s, width=30, textvariable = Event_var)
    myTextbox.pack()

    myLabel = Label(s, text="")
    myLabel.pack()


    myLabel = Label(s, text="")
    myLabel.pack()
    btn = Button(s, text ='Next', bd = '5', command = lambda: generateCertificate(str(cal.get_date())))
    btn.pack()

# setting the application

name_var=StringVar()
date_var = StringVar()
Event_var = StringVar()
panel.pack()
btn = Button(root, text ='Start', bd = '5', command=nextscreen)
btn.pack()
myTextbox = root.mainloop() 