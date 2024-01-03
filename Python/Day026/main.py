import tkinter

window = tkinter.Tk()
#window title
window.title("My First one")
#window size
window.minsize(width = 500, height=300)

#label
my_label = tkinter.Label(text = "I am a label", font = ("Arial",24 , "bold"))
my_label.pack()

#always in the end
window.mainloop()