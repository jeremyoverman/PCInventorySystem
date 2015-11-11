import _mssql, decimal, uuid
import pymssql, datetime

class Dell():
    def __init__(self, parent):
        self.parent = parent
        self.conn = parent.conn
        self.cursor = parent.cursor
        
    def addPC(self, serial, enddate, ordernum, model):
        enddate = self.parent.convertDate(enddate)
        self.cursor.execute(
            "INSERT INTO dell_assets VALUES ('%s', '%s', '%s', '%s')" %
            (serial, enddate, ordernum, model)
        )
        self.conn.commit()
        
    def getInfo(self, serial):
        self.cursor.execute("SELECT warranty_expires, order_number, model FROM dell_assets WHERE service_tag = '%s'" % serial)
        row = self.cursor.fetchone()
        return row[0], row[1], row[2]

class Database():
    def __init__(self):
        self.conn = pymssql.connect("tireid2.wilson.com", "bfusa\overmanjerem", "Swf1067pw12", "ITInventory")
        
        self.cursor = self.conn.cursor()
        
        self.Dell = Dell(self)
        
    def isDefective(self, serial):
        self.cursor.execute("SELECT date FROM defects WHERE serial = '%s'" % serial)
        row = self.cursor.fetchone()
        
        if row: return True
        else: return False
        
    def markDefective(self, serial):
        date = self.convertDate(datetime.date.today())
        self.cursor.execute("INSERT INTO defects VALUES ('%s', '%s')" % (serial, date))
        self.conn.commit()
        
    def convertDate(self, date):
        return date.strftime("%Y%m%d")

    def getManufacturer(self, serial):
        self.cursor.execute("SELECT manufacturer FROM pc_assets WHERE serial='%s'" % serial)
        row = self.cursor.fetchone()
        
        if row:
            return row[0]
        else:
            return None

    def addPC(self, serial, manufacturer):
        self.cursor.execute("INSERT INTO pc_assets VALUES ('%s', '%s')" % (serial, manufacturer))
        self.conn.commit()

if __name__ == "__main__":
    database = Database()
    print database.getManufacturer("gvn7zq1")