'''
Created on May 11, 2015

@author: Jeremy
'''

import wx, wx.grid
import database

class Grid(wx.grid.Grid):
    def __init__(self, *args, **kwargs):
        wx.grid.Grid.__init__(self, *args, **kwargs)
        
        self.CreateGrid(0,3)
        
        self.SetColLabelValue(0, "Name")
        self.SetColLabelValue(1, "Quantity")
        self.SetColLabelValue(2, "Barcode")
        
    def populateList(self, items):
        i = 0
        for item in items:
            sku = str(item)
            barcode = str(items[item][0])
            name = str(items[item][1])
            count = str(items[item][2])
            self.AppendRows(1, False)
            self.SetRowLabelValue(i, sku)
            self.fillRow(i, (name, count, barcode))
            
            i += 1
            
    def fillRow(self, row, values):
        col = 0
        for value in values:
            self.SetCellValue(row, col, value)
            col += 1

class MainPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.main_grid = Grid(self)
        
        self.main_sizer.Add(self.main_grid, 1)
        
        self.SetSizerAndFit(self.main_sizer)
        self.Layout()

class GUI(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        
        self.main_panel = MainPanel(self)
        
        self.Show()

def getItemList():
    db = database.Database()
    result = db.getDatabaseItems()
    items = {}
    for item in result:
        sku = item[0]
        items[sku] = item[1:]
    return items
        

if __name__ == '__main__':
    app = wx.App()
    
    gui = GUI(None)
    
    items = getItemList()
    print items
    
    gui.main_panel.main_grid.populateList(items)
    
    
    app.MainLoop()