'''
Created on May 11, 2015

@author: Jeremy
'''

import wx, wx.grid
import database

class MenuBar(wx.MenuBar):
    def __init__(self, *args, **kwargs):
        wx.MenuBar.__init__(self, *args, **kwargs)
        
        self.file_menu = wx.Menu()
        file_exit = self.file_menu.Append(wx.ID_EXIT, "E&xit", "Close the application.")
        self.Append(self.file_menu, "&File")
        
        self.filter_menu = wx.Menu()
        self.Append(self.filter_menu, "Fi&lters")

class Icons():
    def __init__(self):
        self.ADD = wx.Bitmap("icons/add.png")
        self.REMOVE = wx.Bitmap("icons/remove.png")

class ToolBar(wx.ToolBar):
    def __init__(self, *args, **kwargs):
        wx.ToolBar.__init__(self, *args, **kwargs)
        
        self.AddTool(-1, icons.ADD)
        self.AddTool(-1, icons.REMOVE)
        
        self.Realize()

class NavTree(wx.TreeCtrl):
    def __init__(self, *args, **kwargs):
        wx.TreeCtrl.__init__(self, *args, **kwargs)
        
        self.root = self.AddRoot("Navigation")
        
class NavPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.nav_tree = NavTree(self, size=(150,1))
        
        self.main_sizer.Add(self.nav_tree, 1, wx.EXPAND|wx.BOTH)
        
        self.SetSizerAndFit(self.main_sizer)

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

class GridPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.main_grid = Grid(self)
        
        self.main_sizer.Add(self.main_grid, 1)
        
        self.SetSizerAndFit(self.main_sizer)
        
        self.Layout()

class PropertiesPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.SetSizer(self.main_sizer)
        self.Layout()

class MainPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.top_hor_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.nav_panel = NavPanel(self)
        self.grid_panel = GridPanel(self)
        self.properties_panel = PropertiesPanel(self, size=(200, 200))
        
        self.main_sizer.Add(self.top_hor_sizer, 1, wx.EXPAND|wx.BOTH)
        self.top_hor_sizer.Add(self.nav_panel, 0, wx.EXPAND|wx.VERTICAL|wx.RIGHT, 5)
        self.top_hor_sizer.Add(self.grid_panel, 1, wx.EXPAND|wx.BOTH)
        self.main_sizer.Add(self.properties_panel, 0, wx.EXPAND|wx.BOTH)
        
        self.SetSizerAndFit(self.main_sizer)
        self.Layout()

class GUI(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        
        self.menubar = MenuBar()
        self.toolbar = ToolBar(self)
        self.main_panel = MainPanel(self)
        
        self.SetToolBar(self.toolbar)
        self.SetMenuBar(self.menubar)
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
    
    icons = Icons()
    
    gui = GUI(None, size=(640,480))
    
    items = getItemList()
    
    gui.main_panel.grid_panel.main_grid.populateList(items)
    
    
    app.MainLoop()