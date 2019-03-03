from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.title("Wallet")

# Window Size
window.geometry('550x120')
tab_control = ttk.Notebook(window)

# Tab Frames
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab1.grid_columnconfigure(1, weight = 2)
tab2.grid_columnconfigure(1, weight = 2)

# Tab Labels
tab_control.add(tab1, 	text 	= 'Recieve')
tab_control.add(tab2, 	text 	= 'Send')
tab_control.pack(		expand 	= 1, 
				 		fill 	= 'both'
				 		)

# Text in the main window
# Tab 1 
label1 	= Label(tab1, 
				text 	= 'Enter Wallet ID', 
				padx 	= 5, 
				pady 	= 5)
label1.grid(	column	= 0, 
				row 	= 0, 
				sticky 	= W
				)

label1a 	= Label(tab1, 
				text 	= 'Enter EMD', 
				padx 	= 5, 
				pady 	= 5)
label1a.grid(	column	= 0, 
				row 	= 1, 
				sticky 	= W
				)

label1b 	= Label(tab1, 
				text 	= 'Wallet Amount',
				padx 	= 5, 
				pady 	= 5
				)
label1b.grid(	column	= 0, 
				row		= 2, 
				sticky 	= W
				)

# Tab 2
label2 	= Label(tab2, 
				text 	= 'Enter Wallet ID', 
				padx 	= 5, 
				pady 	= 5)
label2.grid(	column	= 0, 
				row 	= 0, 
				sticky 	= W
				)

label2a 	= Label(tab2, 
				text 	= 'Send Amount', 
				padx 	= 5, 
				pady 	= 5)
label2a.grid(	column	= 0, 
				row 	= 1, 
				sticky 	= W
				)

label2b 	= Label(tab2, 
				text 	= 'Wallet Amount',
				padx 	= 5, 
				pady 	= 5)
label2b.grid(	column	= 0, 
				row		= 2, 
				sticky 	= W
				)

# Entry
# Tab 1
idEntry1 = Entry(	tab1, 
					width 	= 75
					)
idEntry1.grid( 		row 	= 0,
					column	= 1
					)

hexEntry = Entry(	tab1, 
					width 	= 75
					)
hexEntry.grid( 		row 	= 1,
					column	= 1
					)

# Tab 2
idEntry2 = Entry(	tab2, 
					width 	= 75)
idEntry2.grid( 		row 	= 0,
					column	= 1
					)

amountEntry = Entry(tab2,
					width	= 75)
amountEntry.grid( 	row 	= 1,
					column	= 1
					)

# Buttons
# Output when the button is clicked
def clickedReceive():
	messagebox.showinfo('Success', 'Money Recieved')

def clickedSend():
	messagebox.showinfo('Success', 'Money Sent')

def sync():
	print('')
	#Add Sync Function

# Tab 1
button_sync1 = Button(tab1, 	text 	= 'Sync', 
								command = sync,
								padx 	= 0, 
								pady 	= 0)
button_sync1.grid(				column 	= 2, 
								row 	= 0,
								padx 	= 5, 
								pady 	= 0,
								sticky 	= EW
								)


button_receive = Button(tab1, 	text 	= 'Receive', 
								command = clickedSend,
								padx 	= 0, 
								pady 	= 0)
button_receive.grid(			column 	= 2, 
								row 	= 1,
								padx 	= 5, 
								pady 	= 0,
								ipadx	= 1, 
								sticky 	= EW
								)

# Tab 2
button_sync2 = Button(tab2, 	text 	= 'Sync',
								command = sync,
								padx 	= 0, 
								pady 	= 0)
button_sync2.grid(				column 	= 2, 
								row 	= 0,
								padx 	= 5, 
								pady 	= 0,
								ipadx 	= 9,
								sticky 	= EW
								)

button_send2 = Button(tab2, 	text 	= 'Send',
								command = clickedSend,
								padx 	= 0, 
								pady 	= 0)
button_send2.grid(				column 	= 2, 
								row 	= 1,
								padx 	= 5, 
								pady 	= 0,
								sticky 	= EW
								)

window.mainloop()