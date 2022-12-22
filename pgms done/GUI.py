from tkinter import*
from tkinter.ttk import*
class Shape:
    def __init__(self,master=None):
     self.master=master
     self.create()
    def create(self):
     self.canvas=Canvas(self.master)
     self.canvas.create_oval(10,10,80,80,outline="black",fill="white",width=2)
     self.canvas.create_oval(230,10,290,60,outline="black", fill="blue",width=2)
     self.canvas.create_rectangle(110,10,210,80,outline="black",fill="blue",width=2)
     self.canvas.create_arc(30,200,90,100,0,extent=210,outline="green",fill="red",width=2)
     points=[150,100,200,120,240,180,210,200,150,150,100,200]
     self.canvas.create_polygon(points,outline="blue",fill="orange",width=2)
     self.canvas.pack(fill=BOTH,expand=1)
     if __name__=="__main__":
      master=Tk()
      shape=Shape(master)
      master.title("Shapes")
      mainloop()                             
