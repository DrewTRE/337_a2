import hashlib
from Crypto.Cipher import AES
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Wallet:
    def __init__(self, SID, balance) :
        self.WID = str(SID)[len(str(SID)) - 3 : len(str(SID))]
        self.balance = balance
        self.key = hashlib.sha256(str(SID).encode('utf-8'))
        self.syncedWallets = {}

    def generateToken(self, otherWID, amount = 0) :
        # If the given wallet ID is not yet synced with this wallet
        amount = str(0).zfill(8)
        thisWID = str(self.WID).zfill(8)
        newWID = str(otherWID).zfill(8)
        if(newWID not in self.syncedWallets) :
            counter = amount
        else :
            counter = self.syncedWallets[newWID]
        
        hexStr = thisWID + newWID + amount + counter
        cipher = HexAES256()
        print(cipher.encrypt(hexStr))
    
    def openToken(self, token) :
        cipher = HexAES256()
        decrypted = cipher.decrypt(token)
        result =  { "senderID" : decryptedToken[0 : 8],
                   "recieverID" : decryptedToken[8 : 16],
                   "amount" : decryptedToken[16 : 24],
                   "counter" : decryptedToken[24 : 32] }
        return result

    def syncWallet(self, token) :
        cipher = HexAES256()
        openToken = openToken(token)

        if(openToken["senderID"] not in self.SyncedWallets) :
            self.SyncedWallets[openToken["senderID"]] = counter
        else :
            print("Can't sync wallets that are already synced!")
    
    def sendMoney(self, otherWID, amount) :
        if(amount > self.balance) :
            print("Can't send " + amount + ", balance is only " + self.balance)
        else :
            self.balance -= amount

        generateToken(otherWID, amount)

    def recieveMoney(self, token) :
        openToken = openToken(token)
        if(openToken["senderID"] not in self.SyncedWallets) :
            print("Unknown sender. Ignoring send request.")
            return false
        elif(openToken["recieverID"] != self.WID.zfill(8)) :
            print("Invalid reciever. Ignoring send request")
            return false
        elif(openToken["counter"] != self.SyncedWallets[openToken["senderID"]]) :
            print("Invalid send request")
            return false
        else :
            self.balance += int(openToken["amount"])
            return true

class BankSystem :

    def __init__(self) :
        self.wallets = {}
    
    """def syncWallets(self, WID1, WID2) :
        
    def transferMoney(self, senderWID, recieverWID) :
           
    def addWallet(self, wallet) :
    
    def issueEMD(self, WID) :"""
    


class HexAES256:
    def __init__(self, key = "F25D58A0E3E4436EC646B58B1C194C6B505AB1CB6B9DE66C894599222F07B893") :
        self.key = bytes.fromhex(key)
    
    def encrypt(self, hexToEncrypt) :
        aes = AES.new(self.key)
        bytesToEncrypt = bytes.fromhex(hexToEncrypt)
        return aes.encrypt(bytesToEncrypt).hex()

    def decrypt(self, hexToDecrypt) :
        aes = AES.new(self.key)
        decrypted = aes.decrypt(bytes.fromhex(hexToDecrypt))
        return decrypted.hex()

########################### UI ################################################
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
tab3 = ttk.Frame(tab_control)

# Stretch Entry Column
tab1.grid_columnconfigure(1, weight = 2)
tab2.grid_columnconfigure(1, weight = 2)
tab3.grid_columnconfigure(1, weight = 2)

########################### Tab Labels ########################################
tab_control.add(tab1, text = 'Sync')
tab_control.add(tab2, text = 'Send')
tab_control.add(tab3, text = 'Recieve')
tab_control.pack(fill = 'both')

########################### Text ##############################################
# Main Window
label = Label(window, text = 'Wallet Amount', padx = 5, pady = 0)
label.pack()

labela = Label(window, text = Wallet, padx = 5, pady = 0)
labela.pack()

# Tab 1 
label1a = Label(tab1, text = 'Wallet', padx = 5, pady = 5)
label1a.grid(column = 0, row = 0, sticky = W)

label1b = Label(tab1, text = 'Enter Token', padx = 5, pady = 5)
label1b.grid(column  = 0, row = 1, sticky = W)

# Tab 2
label2a = Label(tab2, text 	= 'Send Amount', padx = 5, pady = 5)
label2a.grid(column	= 0, row = 0, sticky = W)

# Tab 3
label3a = Label(tab3, text = 'Enter EMD', padx = 5, pady = 5)
label3a.grid(column = 0, row = 0, sticky = W)

########################### Entry #############################################
# Tab 1
idEntry1 = Entry(tab1, width = 75)
idEntry1.grid(row = 0, column = 1)

tokenEntry1 = Entry(tab1, width = 75)
tokenEntry1.grid(row = 1, column = 1)

# Tab 2
amountEntry = Entry(tab2, width	= 75)
amountEntry.grid(row = 0, column = 1)

# Tab 3
hexEntry = Entry(tab1, width = 75)
hexEntry.grid(row = 0, column = 1)

########################### Buttons ###########################################
# Output when the button is clicked.
# clickedRecieve and clickedSend should both update the Wallet total which is on it's
# own window, so they both can update the global variable Wallet. 
def clickedReceive():
	messagebox.showinfo('Success', 'Money Recieved')

# Should display the token, probably have to set a variable to recieve it. 
def clickedSend():
	messagebox.showinfo('Success', 'Money Sent')

def syncReceive():
    # entry = idEntry1.get()
    # encrypted = Wallet.generateToken(entry)
	# entry = "00000" + idEntry1.get() + "000004280000000000000000"
	# cipher = HexAES256()
	# encrypted = cipher.encrypt(entry)
	# print("Token Generation: ", encrypted)
    messagebox.showinfo('Success', encrypted)

def syncSend():
	# entry = "0000042800000" + idEntry1.get() + "0000000000000000"
	# cipher = HexAES256()
	# encrypted = cipher.encrypt(entry)
	# print("Token Generation: ", encrypted)
	messagebox.showinfo('Success', encrypted)

# Tab 1
button_sync1a = Button(tab1, text = 'Sync', command = syncReceive, padx = 0, pady = 0)
button_sync1a.grid(column = 2, row = 0, padx = 5, pady = 0,sticky = EW)

button_sync1b = Button(tab2, text = 'Sync', command = syncSend, padx = 0, pady = 0)
button_sync1b.grid(column = 2, row = 1, padx = 5, pady = 0, ipadx = 9, sticky = EW)

# Tab 2
button_send2 = Button(tab2, text = 'Send', command = clickedSend, padx = 0, pady = 0)
button_send2.grid(column = 2, row = 0, padx = 5, pady = 0, sticky = EW)

# Tab 3
button_receive1 = Button(tab1, text = 'Receive', command = clickedReceive, padx = 0, pady = 0)
button_receive1.grid(column = 2, row = 0, padx = 5, pady = 0, ipadx = 1, sticky = EW)
window.mainloop()

def main() :

    print("\n=========================================\n")
    cipher = HexAES256()
    test1 = "00000444000003330000002100000001"
    test = "00000333000004280000000000000000"
    print("Example from Token Structure section:")
    print("Before encryption:")
    print(test)
    encrypted = cipher.encrypt(test)
    print("After Encryption:")
    print(encrypted)
    print("After Decryption:")
    print(cipher.decrypt(encrypted))
main()