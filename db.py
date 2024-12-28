import sqlite3

class DataBase:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id Integer Primary Key,
            name text,
            age text,
            cat Integer,
            nots Integer
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self,name,age,cat,nots):
        self.cur.execute("insert into employees values (NULL,?,?,?,?)",(name,age,cat,nots))
        self.con.commit()
    
    def fetch(self):
        self.cur.execute("SELECT * FROM employees")
        rows = self.cur.fetchall()
        return rows
    
    def remove(self,id):
        self.cur.execute("delete from employees where id=?",(id,))
        self.con.commit()
    
    def update(self,id,name,age,cat,nots):
        self.cur.execute("update employees set name=?,age=?,cat=?,nots=? where id=?",
        (name,age,cat,nots, id))
        self.con.commit()
    