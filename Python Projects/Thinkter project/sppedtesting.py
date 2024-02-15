from tkinter import *
import speedtest

def speedcheck():
    sp=speedtest.Speedtest()#speedtest class contain function Speedtest()
    sp.get_servers()
    down=str(round(sp.download()/(10**6),3))+"Mbps" #give spped in mbps(10**6) normally gives in bit/second
    up=str(round(sp.upload()/(10**6),3))+"Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp=Tk()
sp.title("  Internet Speed Test ")
sp.geometry("500x650")
sp.config(bg="Blue")
lab=Label(sp,text=" Internet Speed Test ",font=("Times New Roman",30,"bold"),bg="Blue",fg="Red")
lab.place(x=65,y=50,height=50,width=380)#height and wdth for box

lab=Label(sp,text=" Downloading Speed ",font=("Times New Roman",30,"bold"))
lab.place(x=65,y=130,height=50,width=380)

lab_down=Label(sp,text=" 00 ",font=("Times New Roman",30,"bold"))
lab_down.place(x=65,y=200,height=50,width=380)

lab=Label(sp,text=" Uploading Speed ",font=("Times New Roman",30,"bold"))
lab.place(x=65,y=290,height=50,width=380)

lab_up=Label(sp,text=" 00 ",font=("Times New Roman",30,"bold"))
lab_up.place(x=65,y=360,height=50,width=380)

button=Button(sp,text="Check Speed",font=("Times New Roman",30,"bold"),relief=RAISED,bg="RED",command=speedcheck)
button.place(x=65,y=460,height=50,width=380)

sp.mainloop()