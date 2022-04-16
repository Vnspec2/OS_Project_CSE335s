import string
from tkinter import *
from tkinter import *
from tkinter import Frame, Label
from tkinter.constants import LEFT
from tkinter import ttk

from pip._internal.operations import build

P_num=0
rr_Q=0
my_entries = []

def choosenprocess():  #check if user choose round robin to enable the quantum scale to choose the quantum time

    if (x.get()=="round robin"):
          quantum_label['state']=NORMAL
          quantum_scale['state']=NORMAL
    else:
          quantum_label['state']=DISABLED
          quantum_scale['state']=DISABLED



def nextclick():                     #find the conditions that enable or disable next button after confirming the input data
    print(process_no_scale.get())
    print(x.get())
    if (x.get() in ["fcfs",'sjf premitive',"sjf non premitive","priority premitive","priority non premitive"] and process_no_scale.get()>0):
          next_buttom['state'] = NORMAL
    elif (x.get()=="round robin" and process_no_scale.get()>0 and quantum_scale.get()>0):
          next_buttom['state']=NORMAL
    else :next_buttom['state']=DISABLED

def process_scale_0(value=None):    #if the user set the number of processes to 0
    if(process_no_scale.get()==0):
        next_buttom['state'] = DISABLED


def quantum_scale_0(value=None):     #if the user set the quantum time to 0 if he coosed round robin scheduling
    if(quantum_scale.get()==0):
        next_buttom['state'] = DISABLED
def appending_shit(val):
    my_entries.append(val)

def next_scr():
    def test12():
        entry_list = ''
        for entries in my_entries:
            entry_list = entry_list + str(entries.get()) + '\n'
            my_label.config(text=entry_list)
    P_num=process_no_scale.get()
    rr_Q=quantum_scale.get()
    win1_frame.destroy()
    num=0
    num1=0
    labels = ["Process", "Arrival T", "Burst T", "Pirority"]
    frame_2nd_label=Frame(window)
    frame_2nd_label.pack(side=TOP)
    frame_2nd_slider=Frame(window)
    frame_2nd_slider.pack(side=LEFT)
    frame_button=Frame(window)
    frame_button.pack(side=BOTTOM)
    button1212=Button(frame_button,text="test",command=test12)
    button1212.pack()
    my_label=Label(frame_button,text='')
    my_label.pack(side=BOTTOM)
    for label in labels:
        Name_label = Label(frame_2nd_label, text=label,state=DISABLED)
        Name_label.pack(side=LEFT,padx=90)


    for num1 in range(4):
        if ((x.get() in ["fcfs", 'sjf premitive', "sjf non premitive", "round robin"]) and num1 == 3):
            break
        for num in range(P_num):
           if(num1==0):
               label0 = Label(frame_2nd_slider, text="P" + str(num), state=DISABLED)
               label0.grid(row=num, column=num1,padx=90,pady=5)
           else:
               in_slider = Scale(frame_2nd_slider, from_=0, to=12, resolution=1)
               in_slider.grid(row=num,column=num1,pady=5,padx=90)
               my_entries.append(in_slider)









window=Tk()
# add widgets here
window.resizable(True,True)
processes=["fcfs","sjf premitive","sjf non premitive","priority premitive","priority non premitive","round robin"]
x=StringVar()
y=DoubleVar();
column=0

window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)


win1_frame=Frame(window)  # screen 1 frame
win1_frame.grid(sticky="nsew")

win1_frame.rowconfigure(1, weight=1)
win1_frame.columnconfigure(0, weight=1)

frame_radio=Frame(win1_frame) #process frame screen 1
frame_radio.grid(row=0)


for process in processes:
    radiobutton=Radiobutton(frame_radio,text=process,variable=x,value=process,command=choosenprocess)
    radiobutton.grid(row=0,column=column,pady=20)
    column=column+1

frame1=Frame(win1_frame)   #1st Slider Frame screen1
frame1.grid(row=1)

frame1.rowconfigure(0, weight=1)
frame1.columnconfigure(0, weight=1)

process_no_scale=Scale(frame1,from_=0 , to=6,command=process_scale_0)
process_no_scale.pack(side=TOP)
process_no_label=Label(frame1,text="submit number of processes")
process_no_label.pack()

frame2=Frame(win1_frame)  #2nd Slider Frame screen1
frame2.grid(row=2)

quantum_scale=Scale(frame2,from_=0 , to=6,resolution=0.1,state=DISABLED,command=quantum_scale_0)
quantum_scale.pack(side=TOP)
quantum_label=Label(frame2,text="submit quantum interval",state=DISABLED)
quantum_label.pack()

frame3=Frame(win1_frame)  #Buttons Frame Screen1
frame3.grid(row=3)

input_submit_button=Button(frame3,text="submit the input",command=nextclick)
input_submit_button.pack(side=LEFT)
next_buttom=Button(frame3,text="Next",state=DISABLED,command=next_scr)
next_buttom.pack(side=LEFT)


window.title('scheduler assignment')
window.geometry("1000x900")
window.mainloop()
