import customtkinter as ctk
def lengthcon():
   top=ctk.CTk()
   top.geometry("500x650")
   top.title("length converter")
   la=ctk.CTkLabel(top,text="Length Converter",font=("Arial",25))
   la.place(x=30,y=45)
   la1=ctk.CTkLabel(top,text="Enter the length value",font=("Arial",25))
   la1.place(x=30,y=75)
   e1=ctk.CTkEntry(top,placeholder_text="Enter the value in METERS",border_width=2,border_color="grey",corner_radius=10,width=300)
   e1.place(x=30,y=109)
   e2=ctk.CTkEntry(top,placeholder_text="ENTER KM, CM, MM, INCH, FOOT VALUES",border_width=2,border_color="grey",corner_radius=10,width=300)
   e2.place(x=30,y=150)
   
   def on_enter(event):
      e1.configure(border_color="green")
   
   def on_leave(event):
      e1.configure(border_color="gray")
   
   e1.bind("<Enter>",on_enter)
   e1.bind("<Leave>",on_leave)
   
   def on_enter(event):
      e2.configure(border_color="green")
   
   def on_leave(event):
      e2.configure(border_color="gray")
   
   e2.bind("<Enter>",on_enter)
   e2.bind("<Leave>",on_leave)
   
   def mtokm():
      m=int(e1.get())
      km=m/1000
      e2.delete(0,"end")
      e2.insert(0,str(km))
   
   def mtocm():
      m=int(e1.get())
      cm=m*100
      e2.delete(0,"end")
      e2.insert(0,str(cm))
   
   def mtomm():
      m=int(e1.get())
      mm=m*1000
      e2.delete(0,"end")
      e2.insert(0,str(mm))
   
   def mtoinch():
      m=int(e1.get())
      inch=m*39.37
      e2.delete(0,"end")
      e2.insert(0,str(inch))
   
   def mtoft():
      m=int(e1.get())
      ft=m*0.3048
      e2.delete(0,"end")
      e2.insert(0,str(ft))
   
   def kmtom():
      km=int(e2.get())
      m=km*1000
      e1.delete(0,"end")
      e1.insert(0,str(m))
      
   def cmtom():
      cm=int(e2.get())
      m=cm/100
      e1.delete(0,"end")
      e1.insert(0,str(m))
   
   def mmtom():
       mm=int(e2.get())
       m=mm/1000
       e1.delete(0,"end")
       e1.insert(0,str(m))
   
   def inchtom():
      inch=int(e2.get())
      m=inch/39.37
      e1.delete(0,"end")
      e1.insert(0,str(m))
   
   def fttom():
      ft=int(e2.get())
      m=ft/0.3048
      e1.delete(0,"end")
      e1.insert(0,str(m))
   
   btn1=ctk.CTkButton(top,text="meters into kilometers",fg_color="green",hover_color="blue",command=mtokm)
   btn1.place(x=30,y=200)
   btn2=ctk.CTkButton(top,text="meters into centimeters",fg_color="green",hover_color="blue",command=mtocm)
   btn2.place(x=30,y=240)
   btn3=ctk.CTkButton(top,text="meters into millimeters",fg_color="green",hover_color="blue",command=mtomm)
   btn3.place(x=30,y=280)
   btn4=ctk.CTkButton(top,text="meters into inches",fg_color="green",hover_color="blue",command=mtoinch)
   btn4.place(x=30,y=320)
   btn5=ctk.CTkButton(top,text="meters into foot",fg_color="green",hover_color="blue",command=mtoft)
   btn5.place(x=30,y=360)
   btn6=ctk.CTkButton(top,text="kilometers into meters",fg_color="green",hover_color="blue",command=kmtom)
   btn6.place(x=30,y=400)
   btn7=ctk.CTkButton(top,text="centimeters into meters",fg_color="green",hover_color="blue",command=cmtom)
   btn7.place(x=30,y=440)
   btn8=ctk.CTkButton(top,text="millimeters into meters",fg_color="green",hover_color="blue",command=mmtom)
   btn8.place(x=30,y=480)
   btn9=ctk.CTkButton(top,text="inches into meters",fg_color="green",hover_color="blue",command=inchtom)
   btn9.place(x=30,y=520)
   btn10=ctk.CTkButton(top,text="foot into meters",fg_color="green",hover_color="blue",command=fttom)
   btn10.place(x=30,y=560)
   top.mainloop()