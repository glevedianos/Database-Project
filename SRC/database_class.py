from os import name
from select import select
import sqlite3
from sqlite3.dbapi2 import Cursor
import time
import csv
from datetime import date 

class DataModel():
    def __init__(self, filename):
        self.filename = filename
        try:
            self.con = sqlite3.connect(filename)
            self.con.row_factory = sqlite3.Row  
            self.cursor = self.con.cursor()
            print("Successfully connected to database")
            self.cursor.execute("PRAGMA foreign_keys = ON;")
        except sqlite3.Error as error:
            print("Couldn't connect to database")

    def close(self):
        self.con.commit()
        self.con.close()

    def create_company(self,tin,type,name):
        query = f'insert into company values ("{tin}","{type}","{name}")'
        self.con.execute(query)
        self.con.commit()

    def get_all_comps_name(self):
        r = self.con.execute("select name,type,tin from company order by name").fetchall()
        d = []
        for i in r:
            d.append(dict(i))
        return d

    def get_all_comps_type(self):
        r = self.con.execute("select name,type,tin from company order by type").fetchall()
        d = []
        for i in r:
            d.append(dict(i))
        return d

    def get_comp_info(self, tin):
        r = self.con.execute("select * from company where tin=?",(tin,)).fetchone()
        d = dict(r)
        return d

    def get_companys_pos(self, id_comp):
        r = self.con.execute("select * from position where id_comp=? and available=TRUE",(id_comp,)).fetchall()
        d = []
        for i in r:
            d.append(dict(i))
        return d

    def get_pos_info(self, id, id_comp):
        r = self.con.execute("select salary,name,loc,skillset,available from position,company where position.id=? and position.id_comp=company.tin and position.id_comp=?",(id,id_comp,)).fetchone()
        d = dict(r)
        return d

    def create_position(self,id_comp,skillset,loc,salary):
        num_of_pos = len(self.cursor.execute("select * from position").fetchall())
        avail = 1
        query = f'insert into position values ("{num_of_pos}","{id_comp}","{skillset}","{loc}","{salary}","{avail}")'
        self.con.execute(query)
        self.con.commit()
        r = self.con.execute("select tin from employee where employee.skills= ? and employee.wanted_loc= ? and employee.wanted_salary<= ? ",(skillset,loc,salary))
        while True:
            row=r.fetchone()
            if row== None: break
            else:
                query2 = f'insert into matching values ("{id_comp}","{row[0]}","{num_of_pos}")'    
                self.con.execute(query2)
                self.con.commit()
    
    def create_employee(self,tin,firstname,lastname,skills,tel,mail,wanted_loc,wanted_sal):
        query = f'''insert into employee values ("{tin}","{firstname}","{lastname}","{skills}"
        ,"{tel}","{mail}","{wanted_loc}","{wanted_sal}")'''
        self.con.execute(query)
        self.con.commit()
        r = self.con.execute("select id_comp,id from position where position.skillset= ? and position.loc= ? and position.salary>= ? and available=TRUE",(skills,wanted_loc,wanted_sal))
        while True:
            row=r.fetchone()
            if row== None: break
            else:
                query2 = f'insert into matching values ("{row[0]}","{row[1]}","{tin}")'    
                self.con.execute(query2)
                self.con.commit()

    def get_all_employee_name(self):
        r = self.con.execute("select tin,firstname, lastname, skills from employee order by firstname,lastname").fetchall()
        d = []
        for i in r:
            d.append(dict(i))
        return d

    def get_all_employee_job(self):
        r = self.con.execute("select tin,skills, firstname, lastname from employee order by skills,firstname,lastname").fetchall()
        d = []
        for i in r:
            d.append(dict(i))
        return d
    
    def get_distinct_jobs(self):
        r = self.con.execute("select distinct skills from employee order by skills").fetchall()
        d = []
        for i in r:
            d.append(dict(i))
        return d

    def get_emp_info(self,tin):
        r = self.con.execute("select * from employee where tin=? ",(tin,)).fetchone()
        d = dict(r)
        return d
    
    def get_employee_job(self,skill):
        r = self.con.execute("select tin,skills, firstname, lastname from employee where skills=? order by firstname,lastname",(skill,)).fetchall()
        d = []
        for i in r:
            d.append(dict(i))
        return d
    
    def update_employee(self,tin,firstname,lastname,skills,tel,mail,wanted_loc,wanted_salary):
        self.con.execute("update employee set firstname = ?, lastname = ?, skills = ?, tel = ?, mail = ?, wanted_loc = ?, wanted_salary = ? where tin=?",(firstname,lastname,skills,tel,mail,wanted_loc,wanted_salary,tin))
        self.con.commit()
        self.con.execute("delete from matching where id_emp=?", (tin,))
        self.con.commit()
        r = self.con.execute("select id_comp,id from position where position.skillset= ? and position.loc= ? and position.salary>= ? and available=TRUE",(skills,wanted_loc,wanted_salary))
        while True:
            row=r.fetchone()
            if row== None: break
            else:
                query2 = f'insert into matching values ("{row[0]}","{row[1]}","{tin}")'    
                self.con.execute(query2)
                self.con.commit()
    
    def update_position(self, id, id_comp, skillset, loc, salary):
        self.con.execute("update position set skillset = ?, loc = ?, salary=? where id=? and id_comp=?",(skillset, loc, salary, id ,id_comp))
        self.con.commit()
        self.con.execute("delete from matching where id_pos=? and id_comp=?", (id,id_comp))
        self.con.commit()
        r = self.con.execute("select tin from employee where employee.skills= ? and employee.wanted_loc= ? and employee.wanted_salary<= ? ",(skillset,loc,salary))
        while True:
            row=r.fetchone()
            if row== None: break
            else:
                query2 = f'insert into matching values ("{id_comp}","{id}","{row[0]}")'    
                self.con.execute(query2)
                self.con.commit()

    def delete_company(self, tin):
        self.con.execute("delete from company where tin=?", (tin,))
        self.con.commit()
 
    def update_company(self,type,name,tin):
        self.con.execute("update company set type = ?, name = ? where tin=?",(type, name,tin))
        self.con.commit()

    def delete_employee(self, tin):
        self.con.execute("delete from employee where tin=?", (tin,))
        self.con.commit()
    
    def create_contract(self,id,st_date,end_date):
        query = f'''insert into contract values ("{id}","{st_date}","{end_date}")'''
        self.con.execute(query)
        self.con.commit()

    def create_signing(self,id_contract,id_comp,money):
        query = f'''insert into signing values ("{id_comp}","{id_contract}","{money}")'''
        self.con.execute(query)
        self.con.commit()

    def create_closing(self,id_contract,id_emp,salary):
        query = f'''insert into closing values ("{id_emp}","{id_contract}","{salary}")'''
        self.con.execute(query)
        self.con.commit()
    
    def get_comp_contr(self):
        r = self.con.execute("select id_contract,name, starting_date from company,signing,contract where signing.id_contract=contract.id and signing.id_comp=company.tin").fetchall()
        d = []
        for i in r:
            d.append(dict(i))
        return d
    
    def get_emp_contr(self):
        r = self.con.execute("select id_contract, firstname, lastname, starting_date from closing,contract,employee where closing.id_contract=contract.id and closing.id_emp=employee.tin").fetchall()
        d = []
        for i in r:
            d.append(dict(i))
        return d

    def get_pos_match_emp(self,id_emp):
        r = self.con.execute("select name,loc,salary from position,company,matching,employee where company.tin=position.id_comp and matching.id_comp=position.id_comp and matching.id_pos=position.id and matching.id_emp=employee.tin and employee.tin=? and available=TRUE",(id_emp,)).fetchall()
        d = []
        for i in r:
            d.append(dict(i))
        return d
    
    def get_emps_match_pos(self,id_pos,id_comp):
        r = self.con.execute("select firstname,lastname,tel from position,company,matching,employee where company.tin=position.id_comp and matching.id_comp=position.id_comp and matching.id_pos=position.id and matching.id_emp=employee.tin and company.tin=? and position.id=? and available=TRUE",(id_comp,id_pos,)).fetchall()
        d = []
        for i in r:
            d.append(dict(i))
        return d
    
    def not_avail(self,id,id_comp):
        self.con.execute("update position set available=FALSE where id=? and id_comp=?",(id ,id_comp))
        self.con.commit()







