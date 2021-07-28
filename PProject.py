from tkinter import*
from PIL import Image,ImageTk
import tkinter.messagebox
import pymysql

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Form")
        self.root.geometry("1350x700+0+0")


        #image

        image=Image.open("D:/PythonProject/re.jpg")
        self.bg=ImageTk.PhotoImage(image)
        bg=Label(self.root,image=self.bg)
        bg.place(x=0,y=0,relheight=1,relwidth=1)



         #sideimage
        
        image=Image.open("D:/PythonProject/ty33.jpg")
        self.left=ImageTk.PhotoImage(image)
        bg1=Label(self.root,image=self.left)
        bg1.place(x=900,y=100,height=480,width=400)




        frame1=Frame(root,bg="white")
        frame1.place(x=100,y=100,width=800,height=480)


        title=Label(frame1,text="Employee Registration",font=("Constantia",30,"bold"),bg="white",fg="red")
        title.place(x=200,y=30)

        f_name=Label(frame1,text="First Name",font=("Constantia",15,"bold"),bg="white",fg="black")
        f_name.place(x=50,y=100)
        self.f_enter=Entry(frame1,font=("Constantia",15),bg="lightgray")
        self.f_enter.place(x=50,y=150,width=250)


        l_name=Label(frame1,text="Last Name",font=("Constantia",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)
        self.l_enter=Entry(frame1,font=("Constantia",15),bg="lightgray")
        self.l_enter.place(x=370,y=150,width=250)


        emp_id=Label(frame1,text="Employee ID",font=("Constantia",15,"bold"),bg="white",fg="black")
        emp_id.place(x=50,y=200)
        self.enter_emp_id=Entry(frame1,font=("Constantia",15),bg="lightgray")
        self.enter_emp_id.place(x=50,y=250,width=250)


        dept_name=Label(frame1,text="Department",font=("Constantia",15,"bold"),bg="white",fg="black")
        dept_name.place(x=370,y=200)
        self.enter_dept_name=Entry(frame1,font=("Constantia",15),bg="lightgray")
        self.enter_dept_name.place(x=370,y=250,width=250)


        email_id=Label(frame1,text="Email Address",font=("Constantia",15,"bold"),bg="white",fg="black")
        email_id.place(x=50,y=300)
        self.enter_email_id=Entry(frame1,font=("Constantia",15),bg="lightgray")
        self.enter_email_id.place(x=50,y=350,width=250)


        password=Label(frame1,text="Password",font=("Constantia",15,"bold"),bg="white",fg="black")
        password.place(x=370,y=300)
        self.enter_password=Entry(frame1,font=("Constantia",15),bg="lightgray")
        self.enter_password.place(x=370,y=350,width=250)



        btn_register=Button(frame1,width=20,bg='brown',fg='white',text="Register Now" ,command=lambda:[self.register_data(),self.clear()],borderwidth=5,relief='flat',font=(18))
        btn_register.place(x=250,y=400)


        # btn_left=Button(self.root,width=25,bg='brown',fg='white',text="Sign In",borderwidth=5,relief='flat',font=(20))
        # btn_left.place(x=60,y=500)

    def clear(self): 
        self.f_enter.delete(0,END) 
        self.l_enter.delete(0,END)
        self.enter_emp_id.delete(0,END)
        self.enter_dept_name.delete(0,END)
        self.enter_email_id.delete(0,END)
        self.enter_password.delete(0,END)   
    
    def register_data(self):
        if self.f_enter.get()=="" or self.l_enter.get()=="" or self.enter_emp_id.get()=="" or self.enter_dept_name.get()=="" or self.enter_emp_id.get()=="" or self.enter_password.get()=="":
           tkinter.messagebox.showerror("Error","Please enter all fields",parent=self.root)
        else:

            try:
                con = pymysql.connect(host = 'localhost', user = 'root', password = '', database = 'employee')
                cur = con.cursor()
                cur.execute("select * from employee1 where emp_id=%s", self.enter_emp_id.get())
                row = cur.fetchone()
                #print(row)

                if row != None:
                    tkinter.messagebox.showerror("Error","User already Exist, Please try with another Employee ID",parent=self.root)
                else:    
                    cur.execute("insert into employee1 (f_name,l_name,emp_id,dept_name,email_id,password) values(%s,%s,%s,%s,%s,%s)",
                                    (self.f_enter.get(),
                                    self.l_enter.get(),
                                    self.enter_emp_id.get(),
                                    self.enter_dept_name.get(),
                                    self.enter_email_id.get(),
                                    self.enter_password.get()
                                    ))
                    con.commit()
                    con.close()
                    tkinter.messagebox.showinfo("Hurrah!","Successfully Registered",parent=self.root) 
                    self.clear()
            except Exception as es:
                tkinter.messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)

    


root=Tk()
obj=Register(root)
root.mainloop()
