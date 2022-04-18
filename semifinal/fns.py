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
    #ATT = total_tat / n
    plt.show()
    return  AWT
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
    return  AwT
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
    return  AwT
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
    return  awt
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
    return AWT
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
    return AWT
