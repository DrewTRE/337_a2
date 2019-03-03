from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Global variable for the wallet value. 
# Unsure of what is returned from the hexa, a string or a int/float/etc. 
Wallet = 0

window = Tk()
window.title("Wallet")

# Window Size
window.geometry('550x130')
tab_control = ttk.Notebook(window)
tab_control.pack()

# Tab Frames
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

# Stretch Entry Column
tab1.grid_columnconfigure(1, weight = 2)
tab2.grid_columnconfigure(1, weight = 2)

########################### Tab Labels ########################################
tab_control.add(tab1, text = 'Recieve')
tab_control.add(tab2, text = 'Send')
tab_control.pack(fill = 'both')

########################### Text ##############################################
# Main Window
label = Label(window, text = 'Wallet Amount', padx = 5, pady = 0)
label.pack()

labela = Label(window, text = Wallet, padx = 5, pady = 0)
labela.pack()

# Tab 1 
label1 = Label(tab1, text = 'Enter Wallet ID', padx = 5, pady = 5)
label1.grid(column = 0, row = 0, sticky = W)

label1a = Label(tab1, text = 'Enter EMD', padx = 5, pady = 5)
label1a.grid(column	= 0, row = 1, sticky = W)


# Tab 2
label2 = Label(tab2, text = 'Enter Wallet ID', padx = 5, pady = 5)
label2.grid(column	= 0, row = 0, sticky = W)

label2a = Label(tab2, text 	= 'Send Amount', padx = 5, pady = 5)
label2a.grid(column	= 0, row = 1, sticky = W)


########################### Entry #############################################
# Tab 1
idEntry1 = Entry(tab1, width = 75)
idEntry1.grid(row = 0, column = 1)

hexEntry = Entry(tab1, width = 75)
hexEntry.grid(row = 1, column = 1)
# Tab 2
idEntry2 = Entry(tab2, width  = 75)
idEntry2.grid(row = 0, column = 1)

amountEntry = Entry(tab2, width	= 75)
amountEntry.grid(row = 1, column = 1)

########################### Buttons ###########################################
# Output when the button is clicked.
# clickedRecieve and clickedSend should both update the Wallet total which is on it's
# own window, so they both can update the global variable Wallet. 
def clickedReceive():
	messagebox.showinfo('Success', 'Money Recieved')

# Should display the token, probably have to set a variable to recieve it. 
def clickedSend():
	messagebox.showinfo('Success', 'Money Sent')

def sync():
	print('')
	#Add Sync Function

# Tab 1
button_sync1 = Button(tab1, text = 'Sync', command = sync, padx = 0, pady = 0)
button_sync1.grid(column = 2, row = 0, padx = 5, pady = 0,sticky = EW)

button_receive1 = Button(tab1, text = 'Receive', command = clickedReceive, padx = 0, pady = 0)
button_receive1.grid(column = 2, row = 1, padx = 5, pady = 0, ipadx = 1, sticky = EW)

# Tab 2
button_sync2 = Button(tab2, text = 'Sync', command = sync, padx = 0, pady = 0)
button_sync2.grid(column = 2, row = 0, padx = 5, pady = 0, ipadx = 9, sticky = EW)

button_send2 = Button(tab2, text = 'Send', command = clickedSend, padx = 0, pady = 0)
button_send2.grid(column = 2, row = 1, padx = 5, pady = 0, sticky = EW)

window.mainloop()