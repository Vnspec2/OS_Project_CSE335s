
from fns import *
def choosenprocess():  #check if user choose round robin to enable the quantum scale to choose the quantum time

    if (x.get()=="round robin"):
          quantum_label['state']=NORMAL
          quantum_scale['state']=NORMAL
    else:
          quantum_label['state']=DISABLED
          quantum_scale['state']=DISABLED



def nextclick():                     #find the conditions that enable or disable next button after confirming the input data

    if (x.get() in ["fcfs","sjf premitive","sjf non premitive","priority premitive","priority non premitive"] and process_no_scale.get()>0):
          next_buttom['state'] = NORMAL
    elif (x.get()=="round robin" and process_no_scale.get()>0 and quantum_scale.get()>0):
          next_buttom['state']=NORMAL
    else :next_buttom['state']=DISABLED



def process_scale_0(value=None):    #if the user set the number of processes to 0
    if(process_no_scale.get()==0):
        next_buttom['state'] = DISABLED

def quantum_scale_0(value=None):     #if the user set the quantum time to 0 if he choosed round robin scheduling
    if(quantum_scale.get()==0):
        next_buttom['state'] = DISABLED

def next_scr():
    def reset():
        python = sys.executable
        os.execl(python, python, *sys.argv)

    #create new window after clicking next button
    def test12():
        if(x.get()in["fcfs"]):
            avgt=FCFS(int(process_no_scale.get()))
            Name_label.config(text="average waiting time is "+str(avgt))
        if (x.get() in ["sjf non premitive"]):
            avgt=SJFnonpreem(int(process_no_scale.get()))
            Name_label.config(text="average waiting time is " + str(avgt))
        if (x.get() in ["sjf premitive"]):
            avgt=SJFpreem(int(process_no_scale.get()))
            Name_label.config(text="average waiting time is " + str(avgt))
        if (x.get() in ["priority non premitive"]):
           avgt= Prioritynon(int(process_no_scale.get()))
           Name_label.config(text="average waiting time is " + str(avgt))
        if (x.get() in ["round robin"]):
           avgt=RR(int(process_no_scale.get()), float(quantum_scale.get()))
           Name_label.config(text="average waiting time is " + str(avgt))
        if (x.get() in ["priority premitive"]):
           avgt= priority_preem(int(process_no_scale.get()))
           Name_label.config(text="average waiting time is " + str(avgt))
        calculate_button.config(state=DISABLED)

    new_window=Tk()
    columnn=1
    roww=1
    labels = [ "Arrival T", "Burst T"]
    frame_label1=Frame(new_window,bd=10)   #frame for table
    frame_label1.grid()
    for label2 in labels:                           #adding table's row labels
        label2=Label(frame_label1,text=label2,width=20)
        label2.grid(row=0,column=columnn)
        columnn=columnn+1
    prioritylabel=Label(frame_label1,text="priority no",state=NORMAL if x.get()in ["priority premitive","priority non premitive"] else DISABLED,width=20)
    prioritylabel.grid(row=0, column=3)

    for i in range(process_no_scale.get()):             #add p1,p2 ,pn labels (column labels)
        label2=Label(frame_label1,text="p"+str(i))
        label2.grid(column=0,row=roww)
        roww=roww+1
    i=0

    for i in range(process_no_scale.get()):

            aindex=Scale(frame_label1,from_=0, to=12 ,resolution=1,length=100)   #ab: arrival, burst
            aindex.grid(row=i+1,column=1)
            at1.append(aindex)
            bindex = Scale(frame_label1, from_=0, to=12, resolution=1, length=100)  # ab: arrival, burst
            bindex.grid(row=i + 1, column=2)
            bt1.append(bindex)
            priorityindex = Scale(frame_label1, from_=0, to=12, resolution=1, length=100,state=NORMAL if x.get() in ["priority premitive", "priority non premitive"] else DISABLED)
            priorityindex.grid(column=3,row=i+1)
            pt1.append(priorityindex)
    calculate_button=Button(new_window,text="calculate",command=test12)
    calculate_button.grid(column=5)
    Name_label = Label(new_window,text='average waiting time is ',font=('Times', 24))
    Name_label.grid(column=8, row=4)
    reset_button = Button(new_window, text="reset", command=reset)
    reset_button.grid(column=5, row=6)



    new_window.title('scheduler assignment')
    new_window.geometry("1500x1000")
    new_window.mainloop()

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

next_buttom=Button(window,text="Next",state=DISABLED,command=next_scr)
next_buttom.grid(column=2 ,pady=20)
hint_label=Label(window,text="to enable next button \n -click on submit button \n -check  number of processes >0 \n  -quantum(if RR is choosen) >0 \n -a schedule is choosen ",font=('Times', 12))
hint_label.grid(column=2)

window.title('scheduler assignment')
window.geometry("1000x1000")
window.mainloop()
