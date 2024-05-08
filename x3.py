from tkinter import *
import tkinter.messagebox
tkinter.messagebox.askyesno("hello")
detail={
    "name",
}
root=Tk()
root.geometry("500x500")
name=Label(root,text="name")
name.grid(row=0)
name_entery=Entry(root)
detail_file=open("detail.txt","w")
def submit():
    tkinter.messagebox.askyesno("hello")
    c2=name_entery.get()
    detail.add(c2)
    detail_file.write(str(c2))
    
    pass
name_entery.grid(row=0,column=1)
submit_button=Button(root,text="submit",command=submit)
submit_button.grid(row=1)

print(name_entery.get())
mainloop()
detail_file.close()