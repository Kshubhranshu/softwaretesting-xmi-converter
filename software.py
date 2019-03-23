import re
from tkinter import*
from tkinter import filedialog
#tkinter window
window = Tk()
window.title("XMI_MAN_v1.0")
window.geometry("900x900")
#*****************************
heading1=Label(window,text="XMI TO PSEUDO CONVERTER v1.0")
heading2=Label(window,text="--------------------------------------------------------------------------------------------------------------------------------------------")
heading1.pack()
heading2.pack()
heading1.config(font=("Courier", 20))
#upload module
def upload():
    global msg
    msg=[]
    global num
    num=[]
    window.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("xmi files","*.xmi"),("all files","*.*")))
    
    f=open(window.filename, 'r')
    text_to_search=f.read()
    pattern = re.compile(r'message name\=["][a-zA-Z_0-9().]*["]')
    pattern2 = re.compile(r'number xmi\:value\=["][.0-9]*["]')
    matches = pattern.findall(text_to_search)
    matches2 = pattern2.findall(text_to_search)
    for i in matches:
        pattern = re.compile(r'["][a-zA-z_0-9().]*["]')
        msg += pattern.findall(i)
    
    for j  in matches2:
        pattern2 = re.compile(r'["][.0-9]*["]')
        num += pattern2.findall(j)
    
    pathbox.insert(INSERT,window.filename)
    f.close()
#********************************************************************************
uploadbutton=Button(window,text="Upload XMI",width='10',command= upload,bg="green",fg="white")  #file upload button
uploadbutton.pack(pady=3)
pathbox=Text(window,width="40",height="1") #box for path name
pathbox.pack() 
pseudocode=Label(window,text="Pseudo Code") #pseudo code label
pseudocode.pack()
codebox=Text(window,width="50",height="13")  #box for pseudo code
codebox.pack(pady=1)
#xmi to pseudo code module 
def convert():
    
    for i, j in zip(range(1,len(msg)+1),msg):
        
        codebox.insert(INSERT,(i,"-->",j))
        codebox.insert(INSERT,("\n"))
    
#*************************************************************************************
convertbutton=Button(window,text="CONVERT",width='10',command=convert,bg="red",fg="white") #convert button to pseudo code
convertbutton.pack(pady=1)
attribute=Label(window,text="Attributes")  #label for attribute
attribute.pack()
attributebox=Text(window,width="70",height="15")  #box for attribute
attributebox.pack(pady=1)
attributebox.insert(INSERT,('''  LABEL    MESSAGES          SYN          ASYN          REPLY\n----------------------------------------------------------------------'''))


#attribute generate module
def attribute():
    
    for i, j in zip(num,msg):
        attributebox.insert(INSERT,(i,j))
        attributebox.insert(INSERT,("\n"))
    print(num)
    
    
#***********************************************************************************
getattributebutton=Button(window,text="Get Attributes",width='10',command=attribute,bg="red",fg="white") #get attribute button
getattributebutton.pack()
window.mainloop()
