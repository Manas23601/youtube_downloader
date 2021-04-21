from tkinter import filedialog
from tkinter import *
from pytube import YouTube

def Downloader():                    #function to download
    url =YouTube(str(link.get()))    #get file
    video = url.streams.first()      #get 144p(always first)
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)

def save(): 
    global Folder_Name              
    Folder_Name = filedialog.askdirectory()     #select foldername
    if len(Folder_Name) > 1:
        locationError.config(text=Folder_Name,fg="green")         #store it here
    else:
        locationError.config(text="Please Choose Folder!!",fg="red") #enter a folder name

root = Tk()            #create gui
root.geometry('500x300')  #dimensions
root.resizable(0,0)        #allow no reshaping
root.title("Youtube Video Downloader")     #title of app
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()      #heading
link = StringVar()
link_enter  = Entry(root, textvariable=link, width=50).pack()
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)       
Label(root,text='Choose Location', font = 'arial 20 bold').pack()  #box to place link
Button(root,text = 'Choose Path', font = 'arial 15 bold', bg = 'pale violet red', padx = 2, command = save).place(x=180,y=100)    #choose location
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)  #download file
root.mainloop()
