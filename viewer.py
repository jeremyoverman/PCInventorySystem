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
        
        self.view_menu = wx.Menu()
        self.Append(self.view_menu, "&View")
        
        self.help_menu = wx.Menu()
        self.Append(self.help_menu, "&Help")

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
        self.nav_tree = NavTree(self, size=(100,1))
        
        self.main_sizer.Add(self.nav_tree, 1, wx.EXPAND|wx.BOTH)
        
        self.SetSizerAndFit(self.main_sizer)

class Grid(wx.grid.Grid):
    def __init__(self, *args, **kwargs):
        wx.grid.Grid.__init__(self, *args, **kwargs)
        
        self.CreateGrid(0,3)
        self.SetLabelBackgroundColour(wx.Colour(255,255,255))
        
        label_font = self.GetLabelFont()
        
        #Create corner label
        corner = self.GridCornerLabelWindow
        corner_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        sku_label = wx.StaticText(corner, label="SKU")
        sku_label.SetFont(label_font)
        
        corner_sizer.Add((0,0), 1, wx.EXPAND|wx.BOTH)
        corner_sizer.Add(sku_label, 0, wx.CENTER)
        corner_sizer.Add((0,0), 1, wx.EXPAND|wx.BOTH)
        
        corner.SetSizerAndFit(corner_sizer)
        
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
        self.AutoSizeColumns()
            
    def fillRow(self, row, values):
        col = 0
        for value in values:
            self.SetCellValue(row, col, value)
            col += 1

class GridPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        
        self.main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.splitter = wx.SplitterWindow(self)
        
        self.nav_panel = NavPanel(self.splitter)
        self.main_grid = Grid(self.splitter)
        
        self.splitter.SplitVertically(self.nav_panel, self.main_grid)
        self.splitter.SetMinimumPaneSize(10)
        #self.splitter.SetSashGravity(0.1)
        
        self.main_sizer.Add(self.splitter, 1, wx.EXPAND|wx.BOTH|wx.BOTTOM, 5)
        
        self.SetSizerAndFit(self.main_sizer)
        
        self.Layout()

class PropertiesNotebook(wx.Notebook):
    def __init__(self, *args, **kwargs):
        wx.Notebook.__init__(self, *args, **kwargs)
        
        panel = wx.Panel(self)
        
        self.container_sizer = wx.BoxSizer(wx.VERTICAL)
        self.container_sizer.Add(self, 1, wx.EXPAND|wx.BOTH|wx.TOP, 5)
        
        self.AddPage(panel, "View 1")
        self.AddPage(panel, "View 2")
        self.AddPage(panel, "View 3")
        
        self.Parent.SetSizerAndFit(self.container_sizer)
        
class PropertiesPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.notebook = PropertiesNotebook(self, size=(1, 150))
        
        self.main_sizer.Add(self.notebook, 1, wx.EXPAND|wx.BOTH|wx.TOP, 5)
        
        self.SetSizerAndFit(self.main_sizer)

class MainPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.hor_splitter = wx.SplitterWindow(self, style=wx.SP_NO_XP_THEME | wx.SP_3D | wx.SP_LIVE_UPDATE)
        self.grid_panel = GridPanel(self.hor_splitter)
        self.properties_panel = PropertiesPanel(self.hor_splitter)
        
        self.hor_splitter.SetSashGravity(0.85)
        
        self.hor_splitter.SplitHorizontally(self.grid_panel, self.properties_panel)
        self.hor_splitter.SetMinimumPaneSize(100)
        
        self.main_sizer.Add(self.hor_splitter,1,wx.EXPAND|wx.BOTH)
        
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
    
    gui = GUI(None, -1, "Inventory Viewer", size=(640,480))
    
    items = getItemList()
    
    gui.main_panel.grid_panel.main_grid.populateList(items)
    
    
    app.MainLoop()