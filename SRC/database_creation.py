import sqlite3

conn=sqlite3.connect('final.db')

conn.execute('''CREATE TABLE IF NOT EXISTS company 
                (tin INTEGER,
                 type TEXT,
                 name TEXT,
                 PRIMARY KEY(tin));''')
print('Table "company": ok')

conn.execute('''CREATE TABLE IF NOT EXISTS position
                (id INTEGER, 
                 id_comp INTEGER,
                 skillset TEXT,
                 loc TEXT,               
                 salary INTEGER,
                 available BOOLEAN,
                 PRIMARY KEY(id, id_comp),
                 FOREIGN KEY(id_comp) REFERENCES company(tin)
                  ON UPDATE CASCADE ON DELETE CASCADE);''')
print('Table "position": ok')

conn.execute('''CREATE TABLE IF NOT EXISTS employee
                (tin INTEGER,
                firstname TEXT,
                lastname TEXT,
                skills TEXT,
                tel INTEGER,
                mail TEXT,
                wanted_loc TEXT,
                wanted_salary INTEGER,
                PRIMARY KEY (tin));''')
print('Table "employee": ok')

conn.execute('''CREATE TABLE IF NOT EXISTS interview 
                (id_comp INTEGER,
                 id_pos INTEGER,
                 id_emp INTEGER,
                 answer BOOLEAN,
                 final_int BOOLEAN,
                 stage INTEGER,
                 PRIMARY KEY(id_comp, id_pos, id_emp),
                 FOREIGN KEY(id_comp,id_pos,id_emp) REFERENCES calling(id_comp,id_pos,id_emp)
                  ON UPDATE CASCADE ON DELETE CASCADE);''')
print('Table "interview": ok')

conn.execute('''CREATE TABLE IF NOT EXISTS hiring
                (id INTEGER,
                hire_date DATE,
                id_pos INTEGER,
                id_comp INTEGER,
                id_emp INTEGER,
                PRIMARY KEY(id_comp,id_pos,id_emp),
                FOREIGN KEY (id_emp,id_pos,id_comp) REFERENCES interview(id_emp,id_pos,id_comp)
                ON UPDATE CASCADE ON DELETE CASCADE);''')
print('Table "hiring": ok')


conn.execute('''CREATE TABLE IF NOT EXISTS contract
                (id INTEGER,
                starting_date DATE,
                ending_date DATE,
                PRIMARY KEY (id));''')
print('Table "contract": ok')

conn.execute('''CREATE TABLE IF NOT EXISTS signing
                (id_comp INTEGER,
                id_contract INTEGER,
                money_making INTEGER,
                PRIMARY KEY(id_comp,id_contract),
                FOREIGN KEY (id_comp) REFERENCES company(tin)
                ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (id_contract) REFERENCES contract(id)
                ON UPDATE CASCADE ON DELETE CASCADE);''')
print('Table "signing": ok')         

conn.execute('''CREATE TABLE IF NOT EXISTS closing
                (id_emp INTEGER,
                id_contract INTEGER,
                salary INTEGER,
                PRIMARY KEY(id_emp,id_contract),
                FOREIGN KEY (id_emp) REFERENCES employee(tin)
                ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (id_contract) REFERENCES contract(id)
                ON UPDATE CASCADE ON DELETE CASCADE);''')
print('Table "closing": ok')    

conn.execute('''CREATE TABLE IF NOT EXISTS matching
                (id_comp INTEGER,
                id_emp INTEGER,
                id_pos INTEGER,
                PRIMARY KEY(id_emp,id_pos,id_comp),
                FOREIGN KEY (id_pos,id_comp) REFERENCES position(id,id_comp)
                ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (id_emp) REFERENCES employee(tin)
                ON UPDATE CASCADE ON DELETE CASCADE);''')
print('Table "matching": ok')         

conn.execute('''CREATE TABLE IF NOT EXISTS calling
                (id_emp INTEGER,
                id_pos INTEGER,
                id_comp INTEGER,
                PRIMARY KEY(id_emp,id_pos,id_comp),
                FOREIGN KEY (id_pos,id_comp) REFERENCES position(id,id_comp)
                ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (id_emp) REFERENCES employee(tin)
                ON UPDATE CASCADE ON DELETE CASCADE);''')
print('Table "calling": ok')  