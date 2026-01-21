import tkinter as tk
from tkinter import ttk
from tkinter.ttk import*
import os
from database_class import DataModel


class AppGUI: 
    def __init__(self, root):
        self.root = root
        
        screen_w = self.root.winfo_screenwidth()    
        screen_h = self.root.winfo_screenheight()    
        x = screen_w/2 - 550/2
        y = screen_h/2 - 650/2
        self.root.geometry("%dx%d+%d+%d" % (550,650,x,y))
        self.root.minsize(550,650)
        self.root.maxsize(550,650)
        
        self.root.title("MyGUI")

        if not os.path.exists('final.db'):
            print('Run database_creation.py first.')
            exit()

        self.db = DataModel("final.db")

        self.startPage()

    #Pages#    
    def startPage(self):
        self.startP = tk.Frame(self.root, background="#faf0dc")
        self.startP.pack(side = "top", fill = "both", expand = True)
        
        self.startP.columnconfigure(0,weight=1)
        self.startP.rowconfigure(0,weight=2)
        self.startP.rowconfigure(1,weight=1)
        self.startP.rowconfigure(2,weight=1)
        self.startP.rowconfigure(3,weight=1)
        self.startP.rowconfigure(4,weight=6)

        self.title1 = tk.Label(self.startP, text="Recruitment Agency", font="Helvetica 25 bold", bg="#faf0dc")
        self.title1.grid(row=0,column=0,pady=10)

        st = Style()
        st.configure('W.TButton', background='#345', foreground='black', font=('Helvetica', 20), padding=[0, 10, 0, 10])
        
        self.btnComps = ttk.Button(self.startP,text="Companies", style="W.TButton",
        command = self.startP_to_comps)
        self.btnComps.grid(row=1,column=0)

        self.btnEmps = ttk.Button(self.startP,text="Employees", style="W.TButton",
        command = self.startP_to_employees)
        self.btnEmps.grid(row=2,column=0)

        self.btnContr = ttk.Button(self.startP,text="Contracts", style="W.TButton",
        command = self.startP_to_contracts)
        self.btnContr.grid(row=3,column=0)

    def startP_to_comps(self):
        self.startP.destroy()
        self.companies()

    def comps_to_StartP(self):
        self.allComps.destroy()
        self.startPage()

    def startP_to_employees(self):
        self.startP.destroy()
        self.employees()
    
    def employees_to_StartP(self):
        self.allEmps.destroy()
        self.startPage()

    def startP_to_contracts(self):
        self.startP.destroy()
        self.contracts()

    def contracts_to_StartP(self):
        self.contrPage.destroy()
        self.startPage()
   
    #COMPANY
    def companies(self):

        def create_frame():
            self.companies_by_name = self.db.get_all_comps_name()
            self.companies_by_type = self.db.get_all_comps_type()
            self.allComps = tk.Frame(self.root, background="#faf0dc")
            self.allComps.pack(side = "top", fill = "both", expand = True)
            
            self.allComps.columnconfigure(0,weight=1)
            self.allComps.columnconfigure(1,weight=4)
            self.allComps.columnconfigure(2,weight=4)
            self.allComps.columnconfigure(3,weight=1)

            st = Style()
            st.configure('M.TButton', background='#345', foreground='black', font=('Helvetica', 10), padding=[0,0,0,0])
            st.configure('Order.TButton', background='#345', foreground='black', font=('Helvetica', 15))

            self.btnBack1 = ttk.Button(self.allComps,text="Back", style="M.TButton", width=1,
            command = self.comps_to_StartP)
            self.btnBack1.grid(row=0,column=0,padx=5,pady=5,sticky='nwse')
            
            self.btnAddComp = ttk.Button(self.allComps,text="Add", style="M.TButton", width=8,
            command = self.companies_to_addComp)
            self.btnAddComp.grid(row=0,column=3,padx=5,pady=5,sticky='swse')

            self.title2 = tk.Label(self.allComps, text="Companies", font="Helvetica 22 bold", bg="#faf0dc")
            self.title2.grid(row=1,columnspan=4,pady=30)

            self.btnName = ttk.Button(self.allComps,text="By Name", style="Order.TButton",
            command = lambda: displayCompanies(self.companies_by_name))
            self.btnName.grid(row=3,columnspan=2,pady=10)  
            self.btnType = ttk.Button(self.allComps,text="By Type", style="Order.TButton",
            command = lambda: displayCompanies(self.companies_by_type))
            self.btnType.grid(row=3,column=2,columnspan=2,pady=10) 

        def displayCompanies(complist):
            self.allComps.destroy()
            create_frame()
            row_c=4
            counter=0
            for i in complist:
                tk.Button(self.allComps,text=i["name"], font=('Helvetica', 15), bg="#faf0dc", relief="flat", activebackground="#faf0dc", activeforeground="blue", 
                pady=0, bd=0 , command = lambda c=counter: self.companies_to_company(complist[c]["tin"])).grid(row=row_c,column=0,columnspan=2)
                tk.Label(self.allComps, text=i["type"], font="Helvetica 15", bg="#faf0dc").grid(row=row_c,column=2,columnspan=2)
                row_c = row_c+1
                counter = counter + 1
                
        create_frame()
        displayCompanies(self.companies_by_name)

    def companies_to_addComp(self):
        self.allComps.destroy()
        self.addComp()

    def addComp_to_companies(self):
        self.addNewComp.destroy()
        self.companies()

    def addComp(self):
        self.addNewComp = tk.Frame(self.root, background="#faf0dc")
        self.addNewComp.pack(side = "top", fill = "both", expand = True)

        self.addNewComp.columnconfigure(0,weight=1)
        self.addNewComp.columnconfigure(1,weight=4)
        self.addNewComp.columnconfigure(2,weight=4)
        self.addNewComp.columnconfigure(3,weight=1)
    
        st = Style()
        st.configure('M.TButton', background='#345', foreground='black', font=('Helvetica', 10), padding=[0,0,0,0])
        st.configure('Save.TButton', background='black', foreground='black', font=('Helvetica', 14),padding=[5,1,5,1])
        
        self.btnBack2 = ttk.Button(self.addNewComp,text="Back", style="M.TButton", width=1,
        command = self.addComp_to_companies)
        self.btnBack2.grid(row=0,column=0,padx=5,pady=5,sticky='nwse')

        self.titleAddComp = tk.Label(self.addNewComp,text="Add Company",font="Helvetica 18 bold",background="#faf0dc")
        self.titleAddComp.grid(row=1,column=0,columnspan=4,pady=30)

        self.labelCompName = tk.Label(self.addNewComp,text="Name:",font=("Helvetica",15),background="#faf0dc")
        self.labelCompName.grid(row=2,column=0,columnspan=2,pady=5)

        self.entryCompName = ttk.Entry(self.addNewComp,width=20,font=("Helvetica",15))
        self.entryCompName.grid(row=2,column=2,columnspan=2,pady=5)

        self.labelCompTIN = tk.Label(self.addNewComp,text="TIN:",font=("Helvetica",15),background="#faf0dc")
        self.labelCompTIN.grid(row=3,column=0,columnspan=2,pady=5)

        self.entryCompTIN = ttk.Entry(self.addNewComp,width=20,font=("Helvetica",15))
        self.entryCompTIN.grid(row=3,column=2,columnspan=2,pady=5)

        self.labelCompType = tk.Label(self.addNewComp,text="Type:",font=("Helvetica",15),background="#faf0dc")
        self.labelCompType.grid(row=4,column=0,columnspan=2,pady=5)

        self.entryCompType = ttk.Entry(self.addNewComp,width=20,font=("Helvetica",15))
        self.entryCompType.grid(row=4,column=2,columnspan=2,pady=5)

        def save_entries3():    
            entries = []
            entries1 = [self.entryCompName,self.entryCompTIN,self.entryCompType]
            for i in entries1:
                entries.append(i.get())
                i.delete(0,"end")
            self.db.create_company(entries[1],entries[2],entries[0])
            print(entries)

        self.btnSave3 = Button(self.addNewComp,text="Save",style="Save.TButton", command=save_entries3)  
        self.btnSave3.grid(row=9,column=0,columnspan=4,pady=15)
    
    def addPos_to_company(self,id_comp):
        self.addNewPos.destroy()
        self.company(id_comp)

    def addPos(self,id):
        comp_name = self.db.get_comp_info(id)["name"]
        self.addNewPos = tk.Frame(self.root, background="#faf0dc")
        self.addNewPos.pack(side = "top", fill = "both", expand = True)

        self.addNewPos.columnconfigure(0,weight=1)
        self.addNewPos.columnconfigure(1,weight=4)
        self.addNewPos.columnconfigure(2,weight=4)
        self.addNewPos.columnconfigure(3,weight=1)

        st = Style()
        st.configure('M.TButton', background='#345', foreground='black', font=('Helvetica', 12), padding=[0,0,0,0])
        st.configure('Save.TButton', background='black', foreground='black', font=('Helvetica', 12),padding=[5,1,5,1])
        
        self.btnCompanies = ttk.Button(self.addNewPos,text="Back", style="M.TButton", width=5,
        command = lambda: self.addPos_to_company(self.db.get_comp_info(id)["tin"]))
        self.btnCompanies.grid(row=0,column=0,padx=5,pady=5,sticky='nwse')

        self.compName = tk.Label(self.addNewPos,text=comp_name,font="Helvetica 22 bold",background="#faf0dc")
        self.compName.grid(row=1,column=0,columnspan=4,pady=10)

        self.titleAddPos = tk.Label(self.addNewPos,text="Add Open Job Position",font="Helvetica 17 bold underline",background="#faf0dc")
        self.titleAddPos.grid(row=2,column=0,columnspan=4,pady=10)

        self.labelPos = tk.Label(self.addNewPos,text="Target Occupation:",font=("Helvetica",15),background="#faf0dc")
        self.labelPos.grid(row=3,column=0,columnspan=2,pady=5)

        self.entryPos = ttk.Entry(self.addNewPos,width=20,font=("Helvetica",15))
        self.entryPos.grid(row=3,column=2,columnspan=2,pady=5)

        self.labelPosLoc = tk.Label(self.addNewPos,text="Location:",font=("Helvetica",15),background="#faf0dc")
        self.labelPosLoc.grid(row=4,column=0,columnspan=2,pady=5)

        self.entryPosLoc = ttk.Entry(self.addNewPos,width=20,font=("Helvetica",15))
        self.entryPosLoc.grid(row=4,column=2,columnspan=2,pady=5)
        
        self.labelPosPay = tk.Label(self.addNewPos,text="Salary:",font=("Helvetica",15),background="#faf0dc")
        self.labelPosPay.grid(row=5,column=0,columnspan=2,pady=5)

        self.entryPosPay = ttk.Entry(self.addNewPos,width=20,font=("Helvetica",15))
        self.entryPosPay.grid(row=5,column=2,columnspan=2,pady=5)

        def save_entries():  
            entries = []
            entries1 = [self.entryPos,self.entryPosLoc,self.entryPosPay]
            for i in entries1:
                entries.append(i.get())
                i.delete(0,"end")
            self.db.create_position(id,entries[0],entries[1],entries[2])

        self.btnSave = Button(self.addNewPos,text="Save",style="Save.TButton", command=save_entries)  
        self.btnSave.grid(row=6,column=0,columnspan=4,pady=15) 

    def companies_to_company(self,id):
        self.allComps.destroy()
        self.company(id)
    
    def company_to_companies(self):
        self.compPage.destroy()
        self.companies()
    
    def company(self,id):
        comp_info = self.db.get_comp_info(id)
        comp_name = comp_info["name"]
        comp_type = comp_info["type"]
        positions = self.db.get_companys_pos(id)

        self.compPage = tk.Frame(self.root, background="#faf0dc")
        self.compPage.pack(side = "top", fill = "both", expand = True)

        self.compPage.columnconfigure(0,weight=1)
        self.compPage.columnconfigure(1,weight=4)
        self.compPage.columnconfigure(2,weight=4)
        self.compPage.columnconfigure(3,weight=1)
        
        st = Style()
        st.configure('M.TButton', background='#345', foreground='black', font=('Helvetica', 10), padding=[0,0,0,0])

        self.btnBack3 = ttk.Button(self.compPage,text="Back", style="M.TButton", width=1,
        command = self.company_to_companies)
        self.btnBack3.grid(row=0,column=0,padx=5,pady=5,sticky='nwse')

        self.btnEditComp = ttk.Button(self.compPage,text="Edit", style="M.TButton", width=10,
        command = lambda: self.company_to_editComp(id))
        self.btnEditComp.grid(row=0,column=3,padx=5,pady=5,sticky='swse')

        self.titleComp = tk.Label(self.compPage,text=comp_name,font="Helvetica 30 bold",background="#faf0dc")
        self.titleComp.grid(row=1,column=0,columnspan=4,pady=15)
        
        self.labelc2 = tk.Label(self.compPage,text="TIN:",font=("Helvetica",15),background="#faf0dc")
        self.labelc2.grid(row=2,column=0,columnspan=2,pady=5)

        self.compTIN = tk.Label(self.compPage,text=id,font=("Helvetica",15),background="#faf0dc")
        self.compTIN.grid(row=2,column=2,columnspan=2,pady=5)

        self.labelc3 = tk.Label(self.compPage,text="Type:",font=("Helvetica",15),background="#faf0dc")
        self.labelc3.grid(row=3,column=0,columnspan=2,pady=5)

        self.compProf = tk.Label(self.compPage,text=comp_type,font=("Helvetica",15),background="#faf0dc")
        self.compProf.grid(row=3,column=2,columnspan=2,pady=5)
        
        self.labelc4 = tk.Label(self.compPage,text="Job Positions",font="Helvetica 20 underline",background="#faf0dc")
        self.labelc4.grid(row=4,column=0,columnspan=4,pady=5)

        row_c=5
        counter=0
        for i in positions:
            tk.Button(self.compPage,text="•"+i["skillset"]+","+i["loc"]+","+str(i["salary"])+"€", font="Helvetica 15",bg="#faf0dc", relief="flat", activebackground="#faf0dc", activeforeground="blue", 
            pady=0, bd=0 , command = lambda c=counter: self.company_to_position(positions[c]["id"],id)).grid(row=row_c,column=0,columnspan=4)
            row_c = row_c +1
            counter = counter + 1

    def company_to_position(self,id,id_comp):
        self.compPage.destroy()
        self.position(id,id_comp)

    def position_to_company(self,id):
        self.posPage.destroy()
        self.company(id)

    def position(self,id,id_comp):
        info = self.db.get_pos_info(id,id_comp)
        comp_name = info["name"]
        pos_loc = info["loc"]
        pos_pay = info["salary"]
        pos_job = info["skillset"]

        matchings = self.db.get_emps_match_pos(id,id_comp)

        self.posPage = tk.Frame(self.root, background="#faf0dc")
        self.posPage.pack(side = "top", fill = "both", expand = True)

        self.posPage.columnconfigure(0,weight=1)
        self.posPage.columnconfigure(1,weight=4)
        self.posPage.columnconfigure(2,weight=4)
        self.posPage.columnconfigure(3,weight=1)
        
        st = Style()
        st.configure('M.TButton', background='#345', foreground='black', font=('Helvetica', 10), padding=[0,0,0,0])

        self.btnBack10 = ttk.Button(self.posPage,text="Back", style="M.TButton", width=1,
        command = lambda: self.position_to_company(id_comp))
        self.btnBack10.grid(row=0,column=0,padx=5,pady=5,sticky='nwse')

        self.btnEditPos = ttk.Button(self.posPage,text="Edit", style="M.TButton", width=8,
        command = lambda: self.position_to_editPos(id,id_comp))
        self.btnEditPos.grid(row=0,column=3,padx=5,pady=5,sticky='swse')
        
        self.titlePos = tk.Label(self.posPage,text="Job Description",font="Helvetica 20 underline bold",background="#faf0dc")
        self.titlePos.grid(row=1,column=0,columnspan=4,pady=15)

        self.labelp1 = tk.Label(self.posPage,text="Company:",font=("Helvetica",15),background="#faf0dc")
        self.labelp1.grid(row=2,column=0,columnspan=2,pady=5)

        self.pCompName = tk.Label(self.posPage,text=comp_name,font=("Helvetica",15),background="#faf0dc")
        self.pCompName.grid(row=2,column=2,columnspan=2,pady=5)
        
        self.labelp2 = tk.Label(self.posPage,text="Profession:",font=("Helvetica",15),background="#faf0dc")
        self.labelp2.grid(row=3,column=0,columnspan=2,pady=5)

        self.posJob = tk.Label(self.posPage,text=pos_job,font=("Helvetica",15),background="#faf0dc")
        self.posJob.grid(row=3,column=2,columnspan=2,pady=5)

        self.labelp3 = tk.Label(self.posPage,text="Location:",font=("Helvetica",15),background="#faf0dc")
        self.labelp3.grid(row=4,column=0,columnspan=2,pady=5)

        self.posLoc = tk.Label(self.posPage,text=pos_loc,font=("Helvetica",15),background="#faf0dc")
        self.posLoc.grid(row=4,column=2,columnspan=2,pady=5)
        
        self.labelp4 = tk.Label(self.posPage,text="Salary",font=("Helvetica",15),background="#faf0dc")
        self.labelp4.grid(row=5,column=0,columnspan=2,pady=5)
        
        self.posPay = tk.Label(self.posPage,text=str(pos_pay)+"€",font=("Helvetica",15),background="#faf0dc")
        self.posPay.grid(row=5,column=2,columnspan=2,pady=5)

        self.labelMatchings = tk.Label(self.posPage,text="Potential Employees:",font="Helvetica 15 underline",background="#faf0dc")
        self.labelMatchings.grid(row=6,column=0,columnspan=2,pady=10)

        row_counter = 7
        for i in matchings:
            tk.Label(self.posPage,text="•"+i["firstname"]+" "+i["lastname"]+", "+str(i["tel"]),font=("Helvetica",15),background="#faf0dc").grid(row=row_counter,column=1,columnspan=3,pady=3)
            row_counter=row_counter+1

    def position_to_editPos(self,id,id_comp):
        self.posPage.destroy()
        self.editPos(id,id_comp)

    def editPos_to_position(self,id,id_comp):
        self.editPosPage.destroy()
        self.position(id,id_comp)

    def not_available(self,id,id_comp):
        self.editPosPage.destroy()
        self.db.not_avail(id,id_comp)
        self.editPos_to_company(id_comp)
    
    def editPos_to_company(self,id_comp):
        self.editPosPage.destroy()
        self.company(id_comp)

    def editPos(self,id,id_comp):
        info = self.db.get_pos_info(id,id_comp)
        pos_loc = info["loc"]
        pos_pay = info["salary"]
        pos_job = info["skillset"]
        inf = [pos_job,pos_loc,pos_pay]

        self.editPosPage = tk.Frame(self.root, background="#faf0dc")
        self.editPosPage.pack(side = "top", fill = "both", expand = True)

        self.editPosPage.columnconfigure(0,weight=1)
        self.editPosPage.columnconfigure(1,weight=4)
        self.editPosPage.columnconfigure(2,weight=4)
        self.editPosPage.columnconfigure(3,weight=1)
        
        st = Style()
        st.configure('M.TButton', background='#345', foreground='black', font=('Helvetica', 10), padding=[0,0,0,0])
        st.configure('Save.TButton', background='black', foreground='black', font=('Helvetica', 15),padding=[5,1,5,1])
        st.configure('delete.TButton', background='red', foreground='red', color="red", font=('Helvetica', 10), padding=[0,0,0,0])

        self.btnBack11 = ttk.Button(self.editPosPage,text="Back", style="M.TButton", width=1,
        command = lambda: self.editPos_to_position(id,id_comp))
        self.btnBack11.grid(row=0,column=0,padx=5,pady=5,sticky='nwse')

        self.btnDelete2 = ttk.Button(self.editPosPage,text="Unavailable", style="delete.TButton", width=5,
        command = lambda: self.not_available(id,id_comp))
        self.btnDelete2.grid(row=0,column=3,padx=5,pady=5,sticky='swse')

        self.titleEd = tk.Label(self.editPosPage,text="Edit Description",font="Helvetica 18 bold",background="#faf0dc")
        self.titleEd.grid(row=1,column=0,columnspan=4,pady=30)

        self.labeledPosJ = tk.Label(self.editPosPage,text="Profession:",font=("Helvetica",15),background="#faf0dc")
        self.labeledPosJ.grid(row=2,column=0,columnspan=2,pady=5)

        self.labeledPosL = tk.Label(self.editPosPage,text="Location:",font=("Helvetica",15),background="#faf0dc")
        self.labeledPosL.grid(row=3,column=0,columnspan=2,pady=5)

        self.labeledPosP = tk.Label(self.editPosPage,text="Salary:",font=("Helvetica",15),background="#faf0dc")
        self.labeledPosP.grid(row=4,column=0,columnspan=2,pady=5)
        
        def create_entries4(pos_inf):
            self.editJob = ttk.Entry(self.editPosPage,width=20,font=("Helvetica",15))
            self.editJob.insert(0,pos_inf[0])
            self.editJob.grid(row=2,column=2,columnspan=2,pady=5)

            self.editLoc = ttk.Entry(self.editPosPage,width=20,font=("Helvetica",15))
            self.editLoc.insert(0,pos_inf[1])
            self.editLoc.grid(row=3,column=2,columnspan=2,pady=5)

            self.editPay = ttk.Entry(self.editPosPage,width=20,font=("Helvetica",15))
            self.editPay.insert(0,pos_inf[2])
            self.editPay.grid(row=4,column=2,columnspan=2,pady=5)

        def save_changes():
            entries = []
            entries1 = [self.editJob,self.editLoc,self.editPay]
            for i in entries1:
                entries.append(i.get())
                i.destroy()
            create_entries4(entries)
            self.db.update_position(id,id_comp,entries[0],entries[1],entries[2])
        create_entries4(inf)

        self.btnSave3 = Button(self.editPosPage,text="Save",style="Save.TButton", command=save_changes)  
        self.btnSave3.grid(row=9,column=0,columnspan=4,pady=15)

    def company_to_editComp(self,id):
        self.compPage.destroy()
        self.editComp(id)
    
    def editComp_to_company(self,id):
        self.editCompInfo.destroy()
        self.company(id)

    def delete_comp(self,id):
        self.editCompInfo.destroy()
        self.db.delete_company(id)
        self.companies()   

    def editComp(self,id):
        comp_info = self.db.get_comp_info(id)
        comp_name = comp_info["name"]
        comp_type = comp_info["type"]
        inf = [comp_name,comp_type]

        self.editCompInfo = tk.Frame(self.root, background="#faf0dc")
        self.editCompInfo.pack(side = "top", fill = "both", expand = True)
        
        st = Style()
        st.configure('M.TButton', background='#345', foreground='black', font=('Helvetica', 10), padding=[0,0,0,0])
        st.configure('Save.TButton', background='black', foreground='black', font=('Helvetica', 15),padding=[5,1,5,1])
        st.configure('delete.TButton', background='red', foreground='red', color="red", font=('Helvetica', 10), padding=[0,0,0,0])


        self.btnBack4 = ttk.Button(self.editCompInfo,text="Back", style="M.TButton", width=8,
        command = lambda: self.editComp_to_company(id))
        self.btnBack4.grid(row=0,column=0,padx=5,pady=5,sticky='nwse')

        self.editCompInfo.columnconfigure(0,weight=1)
        self.editCompInfo.columnconfigure(1,weight=4)
        self.editCompInfo.columnconfigure(2,weight=4)
        self.editCompInfo.columnconfigure(3,weight=1)

        self.btnDelete2 = ttk.Button(self.editCompInfo,text="Delete", style="delete.TButton", width=2,
        command = lambda: self.delete_comp(id))
        self.btnDelete2.grid(row=0,column=3,padx=5,pady=5,sticky='swse')

        self.titleEdComp = tk.Label(self.editCompInfo,text="Edit Information",font="Helvetica 18 bold",background="#faf0dc")
        self.titleEdComp.grid(row=1,column=0,columnspan=4,pady=30)

        self.labelNameC = tk.Label(self.editCompInfo,text="Name:",font=("Helvetica",15),background="#faf0dc")
        self.labelNameC.grid(row=2,column=0,columnspan=2,pady=5)

        self.labelTypeC = tk.Label(self.editCompInfo,text="Type:",font=("Helvetica",15),background="#faf0dc")
        self.labelTypeC.grid(row=3,column=0,columnspan=2,pady=5)
        
        def create_entries(pos_inf):
            self.editNameC = ttk.Entry(self.editCompInfo,width=20,font=("Helvetica",15))
            self.editNameC.insert(0,pos_inf[0])
            self.editNameC.grid(row=2,column=2,columnspan=2,pady=5)

            self.editTypeC = ttk.Entry(self.editCompInfo,width=20,font=("Helvetica",15))
            self.editTypeC.insert(0,pos_inf[1])
            self.editTypeC.grid(row=3,column=2,columnspan=2,pady=5)

        def save_changes():
            entries = []
            entries1 = [self.editNameC,self.editTypeC]
            for i in entries1:
                entries.append(i.get())
                i.destroy()
            self.db.update_company(entries[1],entries[0],id)
            create_entries(entries)

        create_entries(inf)

        self.btnSave5 = Button(self.editCompInfo,text="Save",style="Save.TButton", command=save_changes)  
        self.btnSave5.grid(row=9,column=0,columnspan=4,pady=15)

        self.btnAddPos2 = Button(self.editCompInfo,text="Add new Position",style="Save.TButton", command= lambda: self.editComp_to_addPos(id))  
        self.btnAddPos2.grid(row=10,column=0,columnspan=4,pady=15)

    
    def editComp_to_addPos(self,id):
        self.editCompInfo.destroy()
        self.addPos(id)

    #PEOPLE
    def employees(self):
        self.jobs=[]
        for i in self.db.get_distinct_jobs():
            self.jobs.append(i["skills"])
              
        def create_frame():
            self.emps_by_name=self.db.get_all_employee_name()
            self.emps_by_job=self.db.get_all_employee_job()
            
            self.allEmps = tk.Frame(self.root, background="#faf0dc")
            self.allEmps.pack(side = "top", fill = "both", expand = True)
            
            self.allEmps.columnconfigure(0,weight=1)
            self.allEmps.columnconfigure(1,weight=4)
            self.allEmps.columnconfigure(2,weight=4)
            self.allEmps.columnconfigure(3,weight=1)

            st = Style()
            st.configure('M.TButton', background='#345', foreground='black', font=('Helvetica', 10), padding=[0,0,0,0])
            st.configure('Order.TButton', background='#345', foreground='black', font=('Helvetica', 15))
            st.configure("TMenubutton", background="light grey",foreground="black", font=('Helvetica', 15),border="black")

            self.btnBack5 = ttk.Button(self.allEmps,text="Back", style="M.TButton", width=1,
            command = self.employees_to_StartP)
            self.btnBack5.grid(row=0,column=0,padx=5,pady=5,sticky='nwse')
            
            self.btnAddEmp = ttk.Button(self.allEmps,text="Add", style="M.TButton", width=8,
            command = self.employees_to_addEmp)
            self.btnAddEmp.grid(row=0,column=3,padx=5,pady=5,sticky='swse')

            self.title2 = tk.Label(self.allEmps, text="Employees", font="Helvetica 22 bold", bg="#faf0dc")
            self.title2.grid(row=1,columnspan=4,pady=20)

            var = tk.StringVar(self.allEmps)

            def change_dropdown(*args):
                specific_job = self.db.get_employee_job(var.get())
                displayEmployees(specific_job)

            self.jobsMenu = ttk.OptionMenu(self.allEmps,var,"Professions",*self.jobs,style="TMenubutton",command=change_dropdown).grid(row=2,column=0,columnspan=4,pady=20)

            self.btnName2 = ttk.Button(self.allEmps,text="By Name", style="Order.TButton",
            command = lambda: displayEmployees(self.emps_by_name))
            self.btnName2.grid(row=3,columnspan=2,pady=10)  
            self.btnJob = ttk.Button(self.allEmps,text="By Profession", style="Order.TButton",
            command = lambda: displayEmployees(self.emps_by_job))
            self.btnJob.grid(row=3,column=2,columnspan=2,pady=10) 

        def displayEmployees(emplist):
            self.allEmps.destroy()
            create_frame()
            row_c=4
            counter=0
            for i in emplist:
                tk.Button(self.allEmps,text=i["firstname"]+" "+i["lastname"], font=('Helvetica', 15), bg="#faf0dc", relief="flat", activebackground="#faf0dc", activeforeground="blue", 
                pady=0, bd=0 , command = lambda c=counter: self.employees_to_employee(emplist[c]["tin"])).grid(row=row_c,column=0,columnspan=2)
                tk.Label(self.allEmps, text=i["skills"], font="Helvetica 15", bg="#faf0dc").grid(row=row_c,column=2,columnspan=2)
                row_c = row_c+1
                counter = counter + 1
        
        create_frame()
        displayEmployees(self.emps_by_name)

    def employees_to_addEmp(self):
        self.allEmps.destroy()
        self.addEmp()

    def addEmp_to_employess(self):
        self.addNewEmp.destroy()
        self.employees()

    def addEmp(self):
        self.addNewEmp = tk.Frame(self.root, background="#faf0dc")
        self.addNewEmp.pack(side = "top", fill = "both", expand = True)
        
        self.addNewEmp.columnconfigure(0,weight=1)
        self.addNewEmp.columnconfigure(1,weight=4)
        self.addNewEmp.columnconfigure(2,weight=4)
        self.addNewEmp.columnconfigure(3,weight=2)
        
        st = Style()
        st.configure('M.TButton', background='#345', foreground='black', font=('Helvetica', 10), padding=[0,0,0,0])
        st.configure('Save.TButton', background='black', foreground='black', font=('Helvetica', 15),padding=[5,1,5,1])
 
        self.btnBack6 = Button(self.addNewEmp,text="Back", style="M.TButton", width=1,
        command = self.addEmp_to_employess)
        self.btnBack6.grid(row=0,column=0,padx=5,pady=5,sticky='nwse')

        self.titleAdd = tk.Label(self.addNewEmp,text="Add Potential Employee",font="Helvetica 18 bold",background="#faf0dc")
        self.titleAdd.grid(row=1,column=0,columnspan=4,pady=30)

        self.labelLName = tk.Label(self.addNewEmp,text="Last Name:",font=("Helvetica",15),background="#faf0dc")
        self.labelLName.grid(row=2,column=0,columnspan=2,pady=5)

        self.entryLName = ttk.Entry(self.addNewEmp,width=20,font=("Helvetica",15))
        self.entryLName.grid(row=2,column=2,columnspan=2,pady=5)

        self.labelFName = tk.Label(self.addNewEmp,text="First Name:",font=("Helvetica",15),background="#faf0dc")
        self.labelFName.grid(row=3,column=0,columnspan=2,pady=5)

        self.entryFName = ttk.Entry(self.addNewEmp,width=20,font=("Helvetica",15))
        self.entryFName.grid(row=3,column=2,columnspan=2,pady=5)

        self.labelTIN = tk.Label(self.addNewEmp,text="TIN:",font=("Helvetica",15),background="#faf0dc")
        self.labelTIN.grid(row=4,column=0,columnspan=2,pady=5)

        self.entryTIN = ttk.Entry(self.addNewEmp,width=20,font=("Helvetica",15))
        self.entryTIN.grid(row=4,column=2,columnspan=2,pady=5)

        self.labelProf = tk.Label(self.addNewEmp,text="Profession:",font=("Helvetica",15),background="#faf0dc")
        self.labelProf.grid(row=5,column=0,columnspan=2,pady=5)

        self.entryProf = ttk.Entry(self.addNewEmp,width=20,font=("Helvetica",15))
        self.entryProf.grid(row=5,column=2,columnspan=2,pady=5)
        
        self.labelPhone = tk.Label(self.addNewEmp,text="Phone Number:",font=("Helvetica",15),background="#faf0dc")
        self.labelPhone.grid(row=6,column=0,columnspan=2,pady=5)

        self.entryPhone = ttk.Entry(self.addNewEmp,width=20,font=("Helvetica",15))
        self.entryPhone.grid(row=6,column=2,columnspan=2,pady=5)

        self.labelmail = tk.Label(self.addNewEmp,text="email:",font=("Helvetica",15),background="#faf0dc")
        self.labelmail.grid(row=7,column=0,columnspan=2,pady=5)

        self.entrymail = ttk.Entry(self.addNewEmp,width=20,font=("Helvetica",15))
        self.entrymail.grid(row=7,column=2,columnspan=2,pady=5)

        self.labelLoc = tk.Label(self.addNewEmp,text="Preferred Location:",font=("Helvetica",15),background="#faf0dc")
        self.labelLoc.grid(row=8,column=0,columnspan=2,pady=5)

        self.entryLoc = ttk.Entry(self.addNewEmp,width=20,font=("Helvetica",15))
        self.entryLoc.grid(row=8,column=2,columnspan=2,pady=5)

        self.labelPay = tk.Label(self.addNewEmp,text="Preferred Salary:",font=("Helvetica",15),background="#faf0dc")
        self.labelPay.grid(row=9,column=0,columnspan=2,pady=5)

        self.entryPay = ttk.Entry(self.addNewEmp,width=20,font=("Helvetica",15))
        self.entryPay.grid(row=9,column=2,columnspan=2,pady=5)

        def save_entries():   
            entries = []
            entries1 = [self.entryLName,self.entryFName,self.entryTIN,self.entryProf,self.entryPhone,
            self.entrymail,self.entryLoc,self.entryPay]
            for i in entries1:
                entries.append(i.get())
                i.delete(0,"end")
            self.db.create_employee(entries[2],entries[1],entries[0],entries[3],entries[4],entries[5],
            entries[6],entries[7])

        self.btnSave = Button(self.addNewEmp,text="Save",style="Save.TButton", command=save_entries)  
        self.btnSave.grid(row=10,column=0,columnspan=4,pady=15) 

    def employees_to_employee(self,id):
        self.allEmps.destroy()
        self.employee(id)
    
    def employee_to_employees(self):
        self.empPage.destroy()
        self.employees()

    def employee(self,id):
        emp_inf = self.db.get_emp_info(id)
        emp_lname = emp_inf["lastname"]
        emp_fname = emp_inf["firstname"]
        emp_tin = id
        emp_job = emp_inf["skills"]
        emp_phone = emp_inf["tel"]
        emp_mail = emp_inf["mail"]
        emp_loc = emp_inf["wanted_loc"]
        emp_pay = emp_inf["wanted_salary"]

        match_jobs = self.db.get_pos_match_emp(id)
        
        self.empPage = tk.Frame(self.root, background="#faf0dc")
        self.empPage.pack(side = "top", fill = "both", expand = True)

        self.empPage.columnconfigure(0,weight=1)
        self.empPage.columnconfigure(1,weight=4)
        self.empPage.columnconfigure(2,weight=4)
        self.empPage.columnconfigure(3,weight=1)
        
        st = Style()
        st.configure('M.TButton', background='#345', foreground='black', font=('Helvetica', 10), padding=[0,0,0,0])
        st.configure('Save.TButton', background='black', foreground='black', font=('Helvetica', 15),padding=[5,1,5,1])

        self.btnBack7 = ttk.Button(self.empPage,text="Back", style="M.TButton", width=2,
        command = self.employee_to_employees)
        self.btnBack7.grid(row=0,column=0,padx=5,pady=5,sticky='nwse')

        self.btnEditEmp = ttk.Button(self.empPage,text="Edit", style="M.TButton", width=10,
        command = lambda: self.employee_to_editEmp(id))
        self.btnEditEmp.grid(row=0,column=3,padx=5,pady=5,sticky='swse') 

        self.titleEmp = tk.Label(self.empPage, text=emp_fname+" "+emp_lname,font="Helvetica 22 bold", bg="#faf0dc")
        self.titleEmp.grid(row=1,column=0,columnspan=4,pady=20)
        
        self.label2 = tk.Label(self.empPage,text="TIN:",font=("Helvetica",15),background="#faf0dc")
        self.label2.grid(row=2,column=0,columnspan=2,pady=5)

        self.empTIN = tk.Label(self.empPage,text=emp_tin,font=("Helvetica",15),background="#faf0dc")
        self.empTIN.grid(row=2,column=2,columnspan=2,pady=5)

        self.label3 = tk.Label(self.empPage,text="Profession:",font=("Helvetica",15),background="#faf0dc")
        self.label3.grid(row=3,column=0,columnspan=2,pady=5)

        self.empProf = tk.Label(self.empPage,text=emp_job,font=("Helvetica",15),background="#faf0dc")
        self.empProf.grid(row=3,column=2,columnspan=2,pady=5)
        
        self.label4 = tk.Label(self.empPage,text="Phone Number:",font=("Helvetica",15),background="#faf0dc")
        self.label4.grid(row=4,column=0,columnspan=2,pady=5)

        self.empPhone = tk.Label(self.empPage,text=emp_phone,font=("Helvetica",15),background="#faf0dc")
        self.empPhone.grid(row=4,column=2,columnspan=2,pady=5)

        self.label5 = tk.Label(self.empPage,text="email:",font=("Helvetica",15),background="#faf0dc")
        self.label5.grid(row=5,column=0,columnspan=2,pady=5)

        self.empmail = tk.Label(self.empPage,text=emp_mail,font=("Helvetica",15),background="#faf0dc")
        self.empmail.grid(row=5,column=2,columnspan=2,pady=5)

        self.label6 = tk.Label(self.empPage,text="Preferred Location:",font=("Helvetica",15),background="#faf0dc")
        self.label6.grid(row=6,column=0,columnspan=2,pady=5)

        self.empLoc = tk.Label(self.empPage,text=emp_loc,font=("Helvetica",15),background="#faf0dc")
        self.empLoc.grid(row=6,column=2,columnspan=2,pady=5)

        self.label7 = tk.Label(self.empPage,text="Preferred Salary:",font=("Helvetica",15),background="#faf0dc")
        self.label7.grid(row=7,column=0,columnspan=2,pady=5)

        self.empPay = tk.Label(self.empPage,text=str(emp_pay)+"€",font=("Helvetica",15),background="#faf0dc")
        self.empPay.grid(row=7,column=2,columnspan=2,pady=5)

        self.jobLists = tk.Label(self.empPage,text="Potentional Ocupation:",font="Helvetica 15 underline",background="#faf0dc")
        self.jobLists.grid(row=8,column=0,columnspan=4,pady=10)

        count = 9
        for i in match_jobs:
            tk.Label(self.empPage,text="•"+i["name"]+","+i["loc"]+","+str(i["salary"])+"€",font=("Helvetica",15),background="#faf0dc").grid(row=count,column=0,columnspan=4)
            count = count+1
        
    def employee_to_editEmp(self,id):
        self.empPage.destroy()
        self.editEmployee(id)
    
    def editEmp_to_employee(self,id):
        self.editEmp.destroy()
        self.employee(id)

    def delete_emp(self,id):
        self.editEmp.destroy()
        self.db.delete_employee(id)
        self.employees()   

    def editEmployee(self,id):
        emp_inf = self.db.get_emp_info(id)
        emp_lname = emp_inf["lastname"]
        emp_fname = emp_inf["firstname"]
        emp_job = emp_inf["skills"]
        emp_phone = emp_inf["tel"]
        emp_mail = emp_inf["mail"]
        emp_loc = emp_inf["wanted_loc"]
        emp_pay = emp_inf["wanted_salary"]
        inf = [emp_lname,emp_fname,emp_job,emp_phone,emp_mail,emp_loc,emp_pay]       

        self.editEmp = tk.Frame(self.root, background="#faf0dc")
        self.editEmp.pack(side = "top", fill = "both", expand = True)

        self.editEmp.columnconfigure(0,weight=1)
        self.editEmp.columnconfigure(1,weight=4)
        self.editEmp.columnconfigure(2,weight=4)
        self.editEmp.columnconfigure(3,weight=1)
        
        st = Style()
        st.configure('M.TButton', background='#345', foreground='black', font=('Helvetica', 10), padding=[0,0,0,0])
        st.configure('Save.TButton', background='black', foreground='black', font=('Helvetica', 15),padding=[5,1,5,1])
        st.configure('delete.TButton', background='red', foreground='red', color="red", font=('Helvetica', 10), padding=[0,0,0,0])


        self.btnBack8 = ttk.Button(self.editEmp,text="Back", style="M.TButton", width=1,
        command = lambda: self.editEmp_to_employee(id))
        self.btnBack8.grid(row=0,column=0,padx=5,pady=5,sticky='nwse')

        self.btnDelete = ttk.Button(self.editEmp,text="Delete", style="delete.TButton", width=3,
        command = lambda: self.delete_emp(id))
        self.btnDelete.grid(row=0,column=3,padx=5,pady=5,sticky='swse')

        self.titleEdit = tk.Label(self.editEmp,text="Edit Information",font="Helvetica 18 bold",background="#faf0dc")
        self.titleEdit.grid(row=1,column=0,columnspan=4,pady=30)

        self.labelLName2 = tk.Label(self.editEmp,text="Last Name:",font=("Helvetica",15),background="#faf0dc")
        self.labelLName2.grid(row=2,column=0,columnspan=2,pady=5)
        
        self.labelFName2 = tk.Label(self.editEmp,text="First Name:",font=("Helvetica",15),background="#faf0dc")
        self.labelFName2.grid(row=3,column=0,columnspan=2,pady=5)

        self.labelProf2 = tk.Label(self.editEmp,text="Profession:",font=("Helvetica",15),background="#faf0dc")
        self.labelProf2.grid(row=4,column=0,columnspan=2,pady=5)
        
        self.labelPhone2 = tk.Label(self.editEmp,text="Phone Number:",font=("Helvetica",15),background="#faf0dc")
        self.labelPhone2.grid(row=5,column=0,columnspan=2,pady=5)

        self.labelmail2 = tk.Label(self.editEmp,text="email:",font=("Helvetica",15),background="#faf0dc")
        self.labelmail2.grid(row=6,column=0,columnspan=2,pady=5)

        self.labelLoc2 = tk.Label(self.editEmp,text="Preferred Location:",font=("Helvetica",15),background="#faf0dc")
        self.labelLoc2.grid(row=7,column=0,columnspan=2,pady=5)

        self.labelPay2 = tk.Label(self.editEmp,text="Preferred Salary:",font=("Helvetica",15),background="#faf0dc")
        self.labelPay2.grid(row=8,column=0,columnspan=2,pady=5)

        def create_entries(emp_inf):
            self.editLName = ttk.Entry(self.editEmp,width=20,font=("Helvetica",15))
            self.editLName.insert(0,emp_inf[0])
            self.editLName.grid(row=2,column=2,columnspan=2,pady=5)

            self.editFName = ttk.Entry(self.editEmp,width=20,font=("Helvetica",15))
            self.editFName.insert(0,emp_inf[1])
            self.editFName.grid(row=3,column=2,columnspan=2,pady=5)

            self.editProf = ttk.Entry(self.editEmp,width=20,font=("Helvetica",15))
            self.editProf.insert(0,emp_inf[2])
            self.editProf.grid(row=4,column=2,columnspan=2,pady=5)

            self.editPhone = ttk.Entry(self.editEmp,width=20,font=("Helvetica",15))
            self.editPhone.insert(0,emp_inf[3])
            self.editPhone.grid(row=5,column=2,columnspan=2,pady=5)

            self.editmail = ttk.Entry(self.editEmp,width=20,font=("Helvetica",15))
            self.editmail.insert(0,emp_inf[4])
            self.editmail.grid(row=6,column=2,columnspan=2,pady=5)

            self.editLoc = ttk.Entry(self.editEmp,width=20,font=("Helvetica",15))
            self.editLoc.insert(0,emp_inf[5])
            self.editLoc.grid(row=7,column=2,columnspan=2,pady=5)
            
            self.editPay = ttk.Entry(self.editEmp,width=20,font=("Helvetica",15))
            self.editPay.insert(0,emp_inf[6])
            self.editPay.grid(row=8,column=2,columnspan=2,pady=5)

        def save_changes():
            entries = []
            entries1 = [self.editLName,self.editFName,self.editProf,self.editPhone,
            self.editmail,self.editLoc,self.editPay]
            for i in entries1:
                entries.append(i.get())
                i.destroy()
            self.db.update_employee(id,entries[1],entries[0],entries[2],entries[3],
            entries[4],entries[5],entries[6])
            create_entries(entries)
        create_entries(inf)

        self.btnSave = Button(self.editEmp,text="Save",style="Save.TButton", command=save_changes)  
        self.btnSave.grid(row=10,column=0,columnspan=4,pady=15)

    #Contracts
    def contracts(self):
        comp_contrs = self.db.get_comp_contr()
        emp_contrs = self.db.get_emp_contr()
        
        self.contrPage = tk.Frame(self.root, background="#faf0dc")
        self.contrPage.pack(side = "top", fill = "both", expand = True)

        self.contrPage.columnconfigure(0,weight=1)
        self.contrPage.columnconfigure(1,weight=4)
        self.contrPage.columnconfigure(2,weight=4)
        self.contrPage.columnconfigure(3,weight=1)

        st = Style()
        st.configure('M.TButton', background='#345', foreground='black', font=('Helvetica', 10), padding=[0,0,0,0])

        self.btnBack9 = ttk.Button(self.contrPage,text="Back", style="M.TButton", width=1,
        command = self.contracts_to_StartP)
        self.btnBack9.grid(row=0,column=0,padx=5,pady=5,sticky='nwse')

        self.btnAddContr = ttk.Button(self.contrPage,text="Add", style="M.TButton", width=8,
        command = self.contracts_to_addContr)
        self.btnAddContr.grid(row=0,column=3,padx=5,pady=5,sticky='swse')

        self.titleContrs = tk.Label(self.contrPage,text="Contracts",font="Helvetica 22 bold",background="#faf0dc")
        self.titleContrs.grid(row=1,column=0,columnspan=4,pady=25)

        self.compsLabel = tk.Label(self.contrPage,text="With Companies",font="Helvetica 18 bold",background="#faf0dc")
        self.compsLabel.grid(row=2,column=0,columnspan=2,pady=10)

        self.empsLabel = tk.Label(self.contrPage,text="With Individuals",font="Helvetica 18 bold",background="#faf0dc")
        self.empsLabel.grid(row=2,column=2,columnspan=2,pady=10)

        row_count1 = 3
        for i in comp_contrs:
            tk.Label(self.contrPage,text=i["name"]+" "+i["starting_date"],font="Helvetica 12",background="#faf0dc").grid(row=row_count1,column=0,columnspan=2,pady=5)
            row_count1=row_count1+1

        row_count2 = 3
        for i in emp_contrs:
            tk.Label(self.contrPage,text=i["firstname"]+" "+i["lastname"]+" "+i["starting_date"],font="Helvetica 12",background="#faf0dc").grid(row=row_count2,column=2,columnspan=2,pady=5)
            row_count2=row_count2+1

    def contracts_to_addContr(self):
        self.contrPage.destroy()
        self.addContract()
    
    def addContr_to_contracts(self):
        self.addContr.destroy()
        self.contracts()
   
    def addContract(self):
        self.addContr = tk.Frame(self.root, background="#faf0dc")
        self.addContr.pack(side = "top", fill = "both", expand = True)

        self.addContr.columnconfigure(0,weight=1)
        self.addContr.columnconfigure(1,weight=4)
        self.addContr.columnconfigure(2,weight=4)
        self.addContr.columnconfigure(3,weight=1)

        st = Style()
        st.configure('M.TButton', background='#345', foreground='black', font=('Helvetica', 10), padding=[0,0,0,0])
        st.configure('Save.TButton', background='black', foreground='black', font=('Helvetica', 15),padding=[5,1,5,1])

        self.btnBack9 = ttk.Button(self.addContr,text="Back", style="M.TButton", width=1,
        command = self.addContr_to_contracts)
        self.btnBack9.grid(row=0,column=0,padx=5,pady=5,sticky='nwse')

        self.titleAdd = tk.Label(self.addContr,text="Add Contract",font="Helvetica 18 bold",background="#faf0dc")
        self.titleAdd.grid(row=1,column=0,columnspan=4,pady=30)


        def selection():
            return self.varChoice.get()

        self.varChoice= tk.IntVar()
        self.r1 = tk.Radiobutton(self.addContr, bg="#faf0dc",activebackground="#faf0dc", font="Helvetica 15" ,text="Company", variable=self.varChoice, value=1, command=selection)
        self.r1.grid(row=2,column=0,columnspan=2,pady=5)
        self.r2 = tk.Radiobutton(self.addContr, bg="#faf0dc",activebackground="#faf0dc", font="Helvetica 15", text="Individual", variable=self.varChoice, value=2, command=selection)
        self.r2.grid(row=2,column=2,columnspan=2,pady=5)

        self.labelNumber = tk.Label(self.addContr,text="Contract ID:",font=("Helvetica",15),background="#faf0dc")
        self.labelNumber.grid(row=3,column=0,columnspan=2,pady=5)

        self.entryNumber = ttk.Entry(self.addContr,width=20,font=("Helvetica",15))
        self.entryNumber.grid(row=3,column=2,columnspan=2,pady=5)

        self.labelTIN2 = tk.Label(self.addContr,text="TIN:",font=("Helvetica",15),background="#faf0dc")
        self.labelTIN2.grid(row=4,column=0,columnspan=2,pady=5)

        self.entryTIN2 = ttk.Entry(self.addContr,width=20,font=("Helvetica",15))
        self.entryTIN2.grid(row=4,column=2,columnspan=2,pady=5)
        
        self.labelStDate = tk.Label(self.addContr,text="Date of Signature:",font=("Helvetica",15),background="#faf0dc")
        self.labelStDate.grid(row=5,column=0,columnspan=2,pady=5)

        self.entryStDate = ttk.Entry(self.addContr,width=20,font=("Helvetica",15))
        self.entryStDate.insert(0,"DD-MM-YYYY")
        self.entryStDate.grid(row=5,column=2,columnspan=2,pady=5)

        self.labelEdDate = tk.Label(self.addContr,text="Exparation Date:",font=("Helvetica",15),background="#faf0dc")
        self.labelEdDate.grid(row=6,column=0,columnspan=2,pady=5)

        self.entryEdDate = ttk.Entry(self.addContr,width=20,font=("Helvetica",15))
        self.entryEdDate.insert(0,"DD-MM-YYYY")
        self.entryEdDate.grid(row=6,column=2,columnspan=2,pady=5)

        self.labelPay= tk.Label(self.addContr,text="Salary:",font=("Helvetica",15),background="#faf0dc")
        self.labelPay.grid(row=7,column=0,columnspan=2,pady=5)

        self.entryPay= ttk.Entry(self.addContr,width=20,font=("Helvetica",15))
        self.entryPay.grid(row=7,column=2,columnspan=2,pady=5)
        
        def save_entries():
            entries = []
            entries1 = [self.entryNumber,self.entryTIN2,self.entryStDate,self.entryEdDate,self.entryPay]
            for i in entries1:
                entries.append(i.get())
                i.delete(0,"end")
            self.entryEdDate.insert(0,"DD-MM-YYYY")
            self.entryEdDate.grid(row=5,column=2,columnspan=2,pady=5)
            self.entryStDate.insert(0,"DD-MM-YYYY")
            self.entryStDate.grid(row=6,column=2,columnspan=2,pady=5)
            if selection()==1:
                self.db.create_contract(entries[0],entries[2],entries[3])
                self.db.create_signing(entries[0],entries[1],entries[4])
            else:
                self.db.create_contract(entries[0],entries[2],entries[3])
                self.db.create_closing(entries[0],entries[1],entries[4])   
        
        self.btnSave2 = Button(self.addContr,text="Save",style="Save.TButton", command=save_entries)  
        self.btnSave2.grid(row=8,column=0,columnspan=4,pady=15) 

if __name__ == '__main__':
    root = tk.Tk()
    gui = AppGUI(root)
    root.mainloop()

