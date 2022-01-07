import tkinter as tk
main = tk.Tk()

#StringVar for currentValue in R0C2
currentValue = tk.StringVar(main, "0")
#Called by the setValues button, looks for content in the entry box and updates the "current" label
def setValues():
    content = entry.get()
    print(content)
    currentValue.set(content)

#This kills the program
def exitProgram():
    main.destroy()

#Title and window size
main.title("Title")
main.geometry("350x200")

#Descriptions on the far left
tk.Label(main, text="Duration (min): ").grid(row=0, column=0)

#Entry boxes for values amidship
entry = tk.Entry(main, width=10)
entry.grid(row=0, column=1)

#Displays what the value is currently set to.
currentValueLabel = tk.Label(textvariable=currentValue)
currentValueLabel.grid(row=0,column=2)

#Takes any inputted values and sets them in the "Current" column using def setValues
setValuesButton = tk.Button(text='Set Values',width=30,command=setValues)
setValuesButton.grid(row=9, column=0, columnspan=2)

#Red button to end program
exitButton = tk.Button(main, text='Exit Program',fg='white',bg='red',width=30, height=1,command=exitProgram)
exitButton.grid(row=20, column = 0, columnspan=2)
main.mainloop()