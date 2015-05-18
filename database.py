'''
Created on May 11, 2015

@author: Jeremy
'''

import sqlite3 as sql

class Database():
    def __init__(self):
        self.conn = sql.connect("database.db")

    def addSKU(self, assetcode, name):
        result = self.conn.execute("INSERT INTO AssetTags VALUES (NULL, '%s', '%s', 0)" % (assetcode, name))
        self.conn.commit()
        return result.lastrowid
        
        
    def getSKUFromAssetCode(self, assetcode):
        result = self.conn.execute("SELECT sku FROM AssetTags WHERE AssetTags.assetcode = '%s'" % assetcode)
        sku = result.fetchone()
        if sku:
            return sku[0]
        else:
            return None
    
    def getNameFromSku(self, sku):
        result = self.conn.execute("SELECT name FROM AssetTags WHERE AssetTags.sku = '%s'" % sku)
        name = result.fetchone()
        return name[0]
    
    def getCountFromSku(self, sku):
        result = self.conn.execute("SELECT count FROM AssetTags WHERE AssetTags.sku = '%s'" % sku)
        count = result.fetchone()
        return count[0]
    
    def setCountForSKU(self, sku, count):
        result = self.conn.execute("UPDATE AssetTags SET count='%s' WHERE sku='%s'" % (count, sku))
        self.conn.commit()
    
    def getDatabaseItems(self):
        result = self.conn.execute("SELECT * from AssetTags")
        return result.fetchall()

if __name__ == '__main__':
    db = Database()
    items = db.getDatabaseItems()
    
    