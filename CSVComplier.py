import pandas as pd
from tkinter import * 
from tkinter import ttk



#Accessing the Csv File 
df = pd.read_csv('Attempts to combine.csv')
df['Features'] = df['Reason 1'] + ', '+ df['Reason 2'] + ', ' + df['Reason 3'] + ', ' + df['Reason 4']



#Popup Window 
root = Tk(className='cSV REDO')
frm = ttk.Frame(root, padding=100)
frm.grid()


ttk.Label(frm, text=df).grid(column=10, row=100)
ttk.Button(frm, text="quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

#Basic popup complete


