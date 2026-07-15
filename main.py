
import tkinter as tk
from tkinter import ttk, messagebox
import os

quiz=[
("Capital of Pakistan?",["Karachi","Lahore","Islamabad","Peshawar"],2),
("2 + 5 * 2 = ?",["10","12","14","9"],1),
("Python was created by?",["Guido van Rossum","Bill Gates","Dennis Ritchie","Elon Musk"],0),
("Largest planet?",["Earth","Mars","Jupiter","Venus"],2),
("HTML stands for?",["Hyper Text Markup Language","Home Tool Markup Language","Hyperlinks","None"],0),
]

HS_FILE="highscore.txt"
try:
    with open(HS_FILE) as f: high=int(f.read())
except:
    high=0

idx=0
score=0
time_left=15
after_id=None

root=tk.Tk()
root.title("Quiz Game")
root.geometry("700x500")
root.configure(bg="#263238")

title=tk.Label(root,text="🎮 Quiz Game",font=("Arial",22,"bold"),bg="#263238",fg="white")
title.pack(pady=10)

score_lbl=tk.Label(root,text="",bg="#263238",fg="lightgreen",font=("Arial",12))
score_lbl.pack()
timer_lbl=tk.Label(root,text="",bg="#263238",fg="orange",font=("Arial",12))
timer_lbl.pack()

prog=ttk.Progressbar(root,length=400,maximum=len(quiz))
prog.pack(pady=10)
prog_lbl=tk.Label(root,bg="#263238",fg="white")
prog_lbl.pack()

q_lbl=tk.Label(root,wraplength=600,font=("Arial",16,"bold"),bg="#263238",fg="white")
q_lbl.pack(pady=20)

ans=tk.IntVar(value=-1)
rbs=[]
for i in range(4):
    rb=tk.Radiobutton(root,variable=ans,value=i,font=("Arial",12),bg="#455A64",fg="white",selectcolor="#4CAF50")
    rb.pack(fill="x",padx=60,pady=4)
    rbs.append(rb)

def finish():
    global high
    if score>high:
        high=score
        with open(HS_FILE,"w") as f:f.write(str(high))
    if messagebox.askyesno("Finished",f"Score: {score}/{len(quiz)}\nHigh Score: {high}\nPlay again?"):
        restart()
    else:
        root.destroy()

def tick():
    global time_left,after_id,idx
    timer_lbl.config(text=f"⏳ Time: {time_left}s")
    if time_left<=0:
        idx+=1
        load()
    else:
        time_left-=1
        after_id=root.after(1000,tick)

def load():
    global time_left,after_id
    if after_id:
        root.after_cancel(after_id)
    if idx>=len(quiz):
        finish();return
    ans.set(-1)
    q,o,_=quiz[idx]
    q_lbl.config(text=q)
    for i in range(4):
        rbs[i].config(text=o[i])
    score_lbl.config(text=f"Score: {score}")
    prog["value"]=idx
    prog_lbl.config(text=f"Question {idx+1}/{len(quiz)}")
    time_left=15
    tick()

def next_q():
    global idx,score
    if ans.get()==-1:
        messagebox.showwarning("Select","Choose an answer.")
        return
    if ans.get()==quiz[idx][2]:
        score+=1
    idx+=1
    load()

def restart():
    global idx,score
    idx=0
    score=0
    load()

btn=tk.Button(root,text="Next",command=next_q,bg="#4CAF50",fg="white",font=("Arial",13,"bold"))
btn.pack(pady=20)

load()
root.mainloop()
