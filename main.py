import tkinter

window = tkinter.Tk()

window.title("Mile to Km Converter")
window.minsize(300,100)


#Label is equal to
is_equal = tkinter.Label(text = "is equal to")
is_equal.grid(row = 1, column=0)

#Label Miles
miles = tkinter.Label(text = "Miles")
miles.grid(column=2,row=0)

#Entry
input = tkinter.Entry()
input.grid(row = 0, column= 1)

#Label Km
km = tkinter.Label(text = "KM")
km.grid(column=2,row=1)

#Label is 0
result = tkinter.Label(text = "0")
result.grid(row=1,column=1)
#Button

def but_click():
    print("Calculate")
    result["text"] = str(int(input.get())*1.6)

button = tkinter.Button(text = "Click", command= but_click)
button.grid(row= 2, column=1)



window.mainloop()