import string
from tkinter import *
from tkinter import *

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



window=Tk()
# add widgets here
processes=["fcfs","sjf premitive","sjf non premitive","priority premitive","priority non premitive","round robin"]
x=StringVar()
y=DoubleVar();
column=0
for process in processes:
    radiobutton=Radiobutton(window,text=process,variable=x,value=process,command=choosenprocess)
    radiobutton.grid(row=0,column=column,pady=20)
    column=column+1

process_no_scale=Scale(window,from_=0 , to=6,command=process_scale_0)
process_no_scale.grid(pady=20)
process_no_label=Label(window,text="submit number of processes")
process_no_label.grid()

quantum_scale=Scale(window,from_=0 , to=6,resolution=0.1,state=DISABLED,command=quantum_scale_0)
quantum_scale.grid(pady=20)
quantum_label=Label(window,text="submit quantum interval",state=DISABLED)
quantum_label.grid()

input_submit_button=Button(window,text="submit the input",command=nextclick)
input_submit_button.grid(column=2)

next_buttom=Button(window,text="Next",state=DISABLED)
next_buttom.grid(column=2 ,pady=20)

window.title('scheduler assignment')
window.geometry("900x500")
window.mainloop()

