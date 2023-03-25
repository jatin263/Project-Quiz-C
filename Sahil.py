from tkinter import *
from tkinter import ttk;
class student:
    def __init__(self,root):
        self.root=root
        self.root.title("UEM.Jaipur Student mobile number details")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="UEM.Jaipur Student mobile number details",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="black",fg="blue")
        title.pack(side=TOP,fill=X)

#=====Manage frame ======

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="blue")
        Manage_Frame.place(x=20,y=100,width=450,height=560)

        m_title=Label(Manage_Frame,text="Manage students",bg="blue",fg="black",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="blue",fg="black",font=("times new roman",15,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Roll=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(Manage_Frame,text="Name.",bg="blue",fg="black",font=("times new roman",15,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        
        lbl_mobilenumber=Label(Manage_Frame,text="Mobile number",bg="blue",fg="black",font=("times new roman",15,"bold"))
        lbl_mobilenumber.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_mobilenumber=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_mobilenumber.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_email=Label(Manage_Frame,text="E.mail.",bg="blue",fg="black",font=("times new roman",15,"bold"))
        lbl_email.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        txt_email=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        lbl_dateofbirth=Label(Manage_Frame,text="D.O.B.",bg="blue",fg="black",font=("times new roman",15,"bold"))
        lbl_dateofbirth.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_dateofbirth=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dateofbirth.grid(row=5,column=1,pady=10,padx=20,sticky="w")


#====== Butoon Frame======
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="black")
        btn_Frame.place(x=10,y=400,width=430)

        Addbtn=Button(btn_Frame,text="Add",width=10).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_Frame,text="update",width=10).grid(row=0,column=1,padx=10,pady=10)
        clearbtn=Button(btn_Frame,text="clear",width=10).grid(row=0,column=2,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="delete",width=10).grid(row=0,column=3,padx=10,pady=10)
        




#===== Details frame =====
        Details_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="blue")
        Details_Frame.place(x=500,y=100,width=800,height=560)

        lbl_search=Label(Details_Frame,text="Search By",bg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Details_Frame,width=10,font=("times new roman",13,"bold"),state='readonly')
        combo_search['values']=("Roll","Name","Contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txt_Search=Entry(Details_Frame,width=30,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Details_Frame,text="Search",width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Details_Frame,text="Show All",width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)


#====== Table_Frame=======
        Table_Frame=Frame(Details_Frame,bd=4,relief=RIDGE,bg="White")
        Table_Frame.place(x=10,y=50,width=780,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","contact","dob",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Student_table.xview)
        scroll_y.config(command=Student_table.yview)
        Student_table.heading("roll",text="Roll No.")
        Student_table.heading("name",text="Name")
        Student_table.heading("email",text="Email")
        Student_table.heading("contact",text="Contact")
        Student_table.heading("dob",text="D.O.B")
        Student_table['show']='headings'
        Student_table.column("roll",width=150,)
        Student_table.column("name",width=150,)
        Student_table.column("email",width=150,)
        Student_table.column("contact",width=150,)
        Student_table.column("dob",width=150,)




        Student_table.pack()

root=Tk()
ob=student(root)
root.mainloop()


