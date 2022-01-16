import tkinter as tk
root = tk.Tk()
root.geometry('1300X768')

frame = tk.Frame(root)
frame.pack()

close_btn = tk.Button(frame,text="Press me!",command = root.destroy)
close_btn.place(relx=0.5,rely=0.5,relheight=0.1,relwidth=0.4,anchor='n')

root.mainloop()
