
from tkinter import *
import tkMessageBox
import tkFont
import os
import tkFileDialog
import thread
 

import pyttsx

import sys
try:
  f=str(sys.argv[1])
except:
  f="Untitled" 
def start(f="Untitled" ):
 
 
 r=Tk()
 r.title(f)
 
 scrollbar = Scrollbar(r)
 scrollbar.pack( side = RIGHT, fill=Y ) 

 fon=tkFont.Font(family="serif",weight="normal")
 def nw():
   start()
 def de():
  text.delete(1.0,END)

 def about():
  
  tkMessageBox.showinfo("About","\n Developer: VINAY PUNDHIR ")
 
 def spk():
  s=pyttsx.init()
  s.say(text.get(1.0,END))
  s.runAndWait()
 
 def speak():
   thread.start_new_thread(spk,());
 def auto(nm): 
         if "." in nm: 
           x=open(nm,"w")
         else:
           nm=nm+".txt"
           x=open(nm,"w")
         x.write(text.get(1.0,END))
         x.close()
       
         
         
         
       
       
        
 
 def save(f):
     
      
      if cmp(f,r.title()) is 0 :
     
     
         nm=tkFileDialog.asksaveasfilename()
         auto(nm)
         r.title(nm)
         f=nm
        
         
      else: 

         auto(r.title())
         
 def saveas(f):
          
       nm=tkFileDialog.asksaveasfilename()
       auto(nm,f)
  
 def s():
  
   q=Toplevel()
   q.withdraw()
   fg=tkFileDialog.askopenfilename()
   text.delete(1.0,END)
   try:
     dd=open(fg,"r")
     for gg in dd.readlines():
      text.insert(END,gg)
     dd.close()
     r.title(fg)
   except:
     print ""
 
 menubar=Menu(r,bg="#D69D46",fg="white",relief=FLAT)
 m=Menu(menubar,bg="#D69D46",fg="white",tearoff=0,relief=SUNKEN)
 m.add_command(label="New        ",command=de)
 m.add_command(label="Open       ",command=s)
 
 m.add_command(label="Save       ",command=lambda:save(f)) 
 m.add_command(label="Save as       ",command=lambda:saveas(f)) 


 m.add_command(label="About      ",command=about)
 m.add_separator()
 m.add_command(label="Exit       ",command=r.quit)
 menubar.add_cascade(label="File           ",menu=m)
 m1=Menu(menubar,bg="#D69D46",fg="white",tearoff=0,relief=SUNKEN)
 m1.add_command(label="Speak        ",command=speak)
 m1.add_command(label="New window   ",command=nw)
 menubar.add_cascade(label="Options           ",menu=m1) 

 r.config(menu=menubar)
 text=Text(r,yscrollcommand = scrollbar.set ,height=48,font=fon,width=150,relief=FLAT,fg="#222222")
 text.pack(side=LEFT,fill=BOTH)
 scrollbar.config( command = text.yview )
 text.delete(1.0,END)
 try: 
    y=open(f,"r")
    for yy in y.readlines():
      text.insert(END,yy)
    y.close()

 except:
   ss=1
 lb=Label(r,text="hello")
 lb.pack(side=RIGHT)
 mainloop()

start(f)
