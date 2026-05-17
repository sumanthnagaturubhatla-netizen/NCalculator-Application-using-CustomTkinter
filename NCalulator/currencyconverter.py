import customtkinter as ctk
def currencycon():
   top=ctk.CTk()
   top.geometry("1500x1000")
   top.title("currency converter")
   la=ctk.CTkLabel(top,text="Currency Converter",font=("Arial",25))
   la.place(x=30,y=45)
   la1=ctk.CTkLabel(top,text="Enter the currency value",font=("Arial",25))
   la1.place(x=30,y=75)
   e1=ctk.CTkEntry(top,placeholder_text="Enter the value for INDIAN RUPEE VALUE",border_width=2,border_color="grey",corner_radius=10,width=300)
   e1.place(x=30,y=109)
   e2=ctk.CTkEntry(top,placeholder_text="ENTER THE DOLLAR VALUE,GB VALUE,JAPAN VALUE,AE VALUE AND UK GB ",border_width=2,border_color="grey",corner_radius=10,width=300)
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
   
   def inrtousd():
      inr=int(e1.get())
      usd=inr//89
      e2.delete(0,"end")
      e2.insert(0,str(usd))
   
   def inrtoeuro():
      inr=int(e1.get())
      eur=inr//96
      e2.delete(0,"end")
      e2.insert(0,str(eur))
   
   def inrtogbp():
      inr=int(e1.get())
      gbp=inr//112
      e2.delete(0,"end")
      e2.insert(0,str(gbp))
   
   def inrtojpy():
      inr=int(e1.get())
      jpy=inr/1.7
      e2.delete(0,"end")
      e2.insert(0,str(jpy))
   
   def inrtoae():
      inr=int(e1.get())
      ae=inr//24
      e2.delete(0,"end")
      e2.insert(0,str(ae))
   
   def usdtoinr():
      usd=int(e2.get())
      inr=usd*89
      e1.delete(0,"end")
      e1.insert(0,str(inr))
      
   def eurotoinr():
      eur=int(e2.get())
      inr=eur*96
      e1.delete(0,"end")
      e1.insert(0,str(inr))
   
   def gbptoinr():
       gbp=int(e2.get())
       inr=gbp*112
       e1.delete(0,"end")
       e1.insert(0,str(inr))
   
   def jpytoinr():
      jpy=int(e2.get())
      inr=jpy*1.7
      e1.delete(0,"end")
      e1.insert(0,str(inr))
   
   def aetoinr():
      ae=int(e2.get())
      inr=ae*24
      e1.delete(0,"end")
      e1.insert(0,str(inr))
   
   btn1=ctk.CTkButton(top,text="Indian rupees into united states dollars",fg_color="green",hover_color="blue",command=inrtousd)
   btn1.place(x=30,y=200)
   btn2=ctk.CTkButton(top,text="Indian rupees into euros",fg_color="green",hover_color="blue",command=inrtoeuro)
   btn2.place(x=30,y=240)
   btn3=ctk.CTkButton(top,text="Indian rupees into united kingdom gb",fg_color="green",hover_color="blue",command=inrtogbp)
   btn3.place(x=30,y=280)
   btn4=ctk.CTkButton(top,text="Indian rupees into japan yen",fg_color="green",hover_color="blue",command=inrtojpy)
   btn4.place(x=30,y=320)
   btn5=ctk.CTkButton(top,text="Indian rupees into AE",fg_color="green",hover_color="blue",command=inrtoae)
   btn5.place(x=30,y=360)
   btn6=ctk.CTkButton(top,text="united states dollars into Indian Rupees",fg_color="green",hover_color="blue",command=usdtoinr)
   btn6.place(x=30,y=400)
   btn7=ctk.CTkButton(top,text="euos into Indian Rupees",fg_color="green",hover_color="blue",command=eurotoinr)
   btn7.place(x=30,y=440)
   btn8=ctk.CTkButton(top,text="united kingdom into Indian Rupees",fg_color="green",hover_color="blue",command=gbptoinr)
   btn8.place(x=30,y=480)
   btn9=ctk.CTkButton(top,text="japan yen dollars into Indian Rupees",fg_color="green",hover_color="blue",command=jpytoinr)
   btn9.place(x=30,y=520)
   btn10=ctk.CTkButton(top,text="united Arab Emirates into Indian Rupees",fg_color="green",hover_color="blue",command=aetoinr)
   btn10.place(x=30,y=560)
   top.mainloop()
