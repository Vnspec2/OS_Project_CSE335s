import string
from tkinter import *
from tkinter import *
from tkinter import Label
from matplotlib import pyplot as plt
import numpy as np
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
import matplotlib.patches as mpatches
from tkinter import *
from matplotlib import pyplot as plt
import string
from tkinter import *
from tkinter import *
from tkinter import Label
from matplotlib import pyplot as plt
import numpy as np
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
import matplotlib.patches as mpatches


at1=[]
bt1=[]
pt1=[]
at=[]
bt=[]
pr=[]


def FCFS(n):
    for entry in at1:
        at.append(int(entry.get()))
    for entry1 in bt1:
        bt.append(int(entry1.get()))

    wt = [0] * n  # waiting time
    tat = [0] * n  # turn around time
    rt = [0] * n  # remaining time

    for i in range(n):
        rt[i] = bt[i]
    t = 0  # current time
    first = 0
    complete = 0
    check = False
    while (complete != n):
        for j in range(n):
            if ((at[j] <= t) and (rt[j] > 0)):
                first = j
                check = True
        if (check == False):
            t += 1
            continue
        rt[first] = 0
        plt.barh(y=1, left=t, width=bt[first], height=0.5, alpha=0.5)
        plt.text(t, 1, s=first, ha='left', va='center')

        t += bt[first]
        complete += 1

        wt[first] = (t - bt[first] - at[first])
        if wt[first] < 0:
            wt[first] = 0

    for i in range(n):
        tat[i] = bt[i] + wt[i]

    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]

    AWT = total_wt / n
    ATT = total_tat / n
    plt.show()
    return ATT, AWT
    # self.lineEdit_3.setText(int(n))
def SJFnonpreem(n):
    for entry in at1:
        at.append(int(entry.get()))
    for entry1 in bt1:
        bt.append(int(entry1.get()))

    wt = [0] * n
    tat = [0] * n
    rt = [0] * n

    for i in range(n):
        rt[i] = bt[i]
    complete = 0
    t = 0
    minm = 999999999
    short = 0
    check = False

    while (complete != n):
        for j in range(n):
            if ((at[j] <= t) and
                    (rt[j] < minm) and rt[j] > 0):
                minm = rt[j]
                short = j
                check = True
        if (check == False):
            t += 1
            continue

        rt[short] = 0

        minm = 999999999

        plt.barh(y=1, left=t, width=bt[short], height=0.5, alpha=0.5)
        plt.text(t, 1, s=short, ha='left', va='center')

        complete += 1
        check = False
        t += bt[short]

        wt[short] = (t - bt[short] - at[short])

        if (wt[short] < 0):
            wt[short] = 0

    for i in range(n):
        tat[i] = bt[i] + wt[i]

    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]

    AwT = total_wt / n
    ATT = total_tat / n
    plt.show()
    return ATT, AwT
def SJFpreem(n):
    for entry in at1:
        at.append(int(entry.get()))
    for entry1 in bt1:
        bt.append(int(entry1.get()))

    wt = [0] * n
    tat = [0] * n
    rt = [0] * n

    for i in range(n):
        rt[i] = bt[i]
    complete = 0
    t = 0
    minm = 999999999
    short = 0
    check = False

    while (complete != n):
        for j in range(n):
            if ((at[j] <= t) and
                    (rt[j] < minm) and rt[j] > 0):
                minm = rt[j]
                short = j
                check = True
        if (check == False):
            t += 1
            continue
        plt.barh(y=1, left=t, width=1, height=0.5, alpha=0.5)
        plt.text(t, 1, s=short, ha='left', va='center')
        rt[short] -= 1

        minm = rt[short]
        if (minm == 0):
            minm = 999999999

        if (rt[short] == 0):
            complete += 1
            check = False
            fint = t + 1

            wt[short] = (fint - bt[short] - at[short])

            if (wt[short] < 0):
                wt[short] = 0

        t += 1

    for i in range(n):
        tat[i] = bt[i] + wt[i]

    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]

    AwT = total_wt / n
    ATT = total_tat / n
    plt.show()
    return ATT, AwT
def Prioritynon(n):
    for entry in at1:
        at.append(int(entry.get()))
    for entry1 in bt1:
        bt.append(int(entry1.get()))
    for entry2 in pt1:
        pr.append(int(entry2.get()))

    wt = [0] * n
    tat = [0] * n

    complete = 0
    t = 0
    prior = 99999999
    first = 0
    check = False

    while (complete != n):
        for j in range(n):
            if ((at[j] <= t) and
                    (pr[j] <= prior)):

                if (pr[j] == prior):
                    if (at[j] > at[first]):
                        continue

                prior = pr[j]
                first = j
                check = True
        if (check == False):
            t += 1
            continue

        pr[first] = 999999999

        prior = 99999999

        plt.barh(y=1, left=t, width=bt[first], height=0.5, alpha=0.5)
        plt.text(t, 1, s=first, ha='left', va='center')

        complete += 1
        check = False
        t += bt[first]

        wt[first] = (t - bt[first] - at[first])

        if (wt[first] < 0):
            wt[first] = 0

    for i in range(n):
        tat[i] = bt[i] + wt[i]
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]

    awt = total_wt / n
    att = total_tat / n
    plt.show()
    return att, awt
def RR(n,quantum):
    for entry in at1:
        at.append(int(entry.get()))
    for entry1 in bt1:
        bt.append(int(entry1.get()))

    wt = [0] * n
    tat = [0] * n
    rem_bt = [0] * n

    for i in range(n):
        rem_bt[i] = bt[i]
    t = 0  # Current time
    check = False
    complete = 0

    while (complete != n):

        for j in range(n):

            if (rem_bt[j] > 0 and at[j] <= t):

                check = True
                if (rem_bt[j] > quantum):

                    plt.barh(y=1, left=t, width=quantum, height=0.5, alpha=0.5)
                    plt.text(t, 1, s=j, ha='left', va='center')

                    t += quantum
                    rem_bt[j] -= quantum

                else:

                    plt.barh(y=1, left=t, width=rem_bt[j], height=0.5, alpha=0.5)
                    plt.text(t, 1, s=j, ha='left', va='center')

                    t = t + rem_bt[j]
                    wt[j] = t - bt[j] - at[j]
                    rem_bt[j] = 0
                    complete += 1
        if (check == False):
            t += 1
            continue
        check = False

    for i in range(n):
        tat[i] = bt[i] + wt[i]

    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]

    AWT = total_wt / n
    ATT = total_tat / n
    plt.show()
    return AWT, ATT
def priority_preem(n):
    for entry in at1:
        at.append(int(entry.get()))
    for entry1 in bt1:
        bt.append(int(entry1.get()))
    for entry2 in pt1:
        pr.append(int(entry2.get()))

    wt = [0] * n
    tat = [0] * n
    rt = [0] * n

    for i in range(n):
        rt[i] = bt[i]
    complete = 0
    t = 0
    prior = 999999999
    first = 0
    check = False

    while (complete != n):
        for j in range(n):
            if ((at[j] <= t) and
                    (pr[j] <= prior) and rt[j] > 0):
                if (pr[j] == prior):
                    if (at[j] > at[first]):
                        continue
                prior = pr[j]
                first = j
                check = True

        if (check == False):
            t += 1
            continue
        plt.barh(y=1, left=t, width=1, height=0.5, alpha=0.5)
        plt.text(t, 1, s=first, ha='left', va='center')
        rt[first] -= 1  # remaining time ^_^

        if (rt[first] == 0):
            complete += 1
            pr[first] = 999999999
            prior = 99999999
            check = False
            fint = t + 1

            wt[first] = (fint - bt[first] - at[first])

            if (wt[first] < 0):
                wt[first] = 0

        t += 1

    for i in range(n):
        tat[i] = bt[i] + wt[i]

    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]

    AWT = total_wt / n
    ATT = total_tat / n
    plt.show()
    return AWT, ATT

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

    #create new window after clicking next button
    def test12():
        if(x.get()in["fcfs"]):
            FCFS(int(process_no_scale.get()))
        if (x.get() in ["sjf non premitive"]):
            SJFnonpreem(int(process_no_scale.get()))
        if (x.get() in ["sjf premitive"]):
            SJFpreem(int(process_no_scale.get()))
        if (x.get() in ["priority non premitivee"]):
            Prioritynon(int(process_no_scale.get()))
        if (x.get() in ["round robin"]):
            RR(int(process_no_scale.get()), float(quantum_scale.get()))
        if (x.get() in ["priority premitive"]):
            priority_preem(int(process_no_scale.get()))

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
    Name_label = Label(new_window,text='')
    Name_label.grid(column=8, row=4)



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

window.title('scheduler assignment')
window.geometry("900x500")
window.mainloop()
