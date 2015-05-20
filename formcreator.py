'''
Created on May 19, 2015

@author: jeremy
'''

import wx

class FormItem(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, size=(180,35))
        
        self.container_sizer = wx.BoxSizer(wx.VERTICAL)
        self.blank_panel = wx.Panel(self, *args, **kwargs)
        self.container_sizer.Add(self.blank_panel, 1, wx.EXPAND|wx.BOTH)
        
        self.SetSizer(self.container_sizer)
        self.Layout()
    
    def showItem(self):
        self.blank_panel.Show(False)
        self.item_panel.Show(True)
        self.GetParent().Layout()
        
    def createItemAndShow(self, item, label=None, *args, **kwargs):
        self.createItem(item, label, *args, **kwargs)
        self.showItem()
    
    def createItem(self, item, label=None, *args, **kwargs):
        self.item_panel = wx.Panel(self)
        self.item_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        if label:
            self.item_label = wx.StaticText(self.item_panel, label=label)
            self.item_sizer.Add(self.item_label, 0, wx.CENTER|wx.RIGHT, 5)
            
        self.item_object = item(self.item_panel, *args, **kwargs)
        self.item_sizer.Add(self.item_object, 1, wx.CENTER)
        
        self.container_sizer.Add(self.item_panel, 1, wx.CENTER|wx.EXPAND|wx.BOTH|wx.ALL, 2)
        
        self.item_panel.SetSizerAndFit(self.item_sizer)
        self.item_panel.Show(False)

class CustomForm(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        
        self.grid = []
        
        self.form_sizer = wx.GridBagSizer()
        self.form_sizer.SetEmptyCellSize((180,35))
        
        self.createGrid(10,3)
        
        self.SetSizerAndFit(self.form_sizer)
    
    def createGrid(self, rows, cols):
        for row in range(rows):
            self.grid.append([])
            for col in range(cols):
                self.grid[row].append([])
                panel = FormItem(self, style=wx.BORDER_SIMPLE)
                self.grid[row][col] = panel
                cell = (row, col)
                self.form_sizer.Add(panel, cell)
    
    def getItemFromCell(self, cell):
        return self.grid[cell[0]][cell[1]]
    
    def addTextEntry(self, cell, label=None):
        form_item = self.getItemFromCell(cell)
        form_item.createItemAndShow(wx.TextCtrl, "Test")
        
if __name__ == "__main__":
    app = wx.App()
    frame = wx.Frame(None, -1, "Test", size=(640,480))
    
    sizer = wx.BoxSizer(wx.VERTICAL)
    
    form = CustomForm(frame)
    sizer.Add(form, 1, wx.EXPAND|wx.BOTH)
    
    form.addTextEntry((5,2), label="Test")
    
    frame.SetSizer(sizer)
    frame.Layout()
    frame.Show()
    app.MainLoop()