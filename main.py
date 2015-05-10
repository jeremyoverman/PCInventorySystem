"""Author: Jeremy Overman"""

import wx, winsound
import sqlite3 as sql

class Text(wx.StaticText):
    def __init__(self, *args, **kwargs):
        wx.StaticText.__init__(self, *args, **kwargs)
        
        self.font = DEFAULTFONT
        
        self.SetFont(self.font)
    
    def setSize(self, pointsize):
        self.font.SetPointSize(pointsize)
        self.SetFont(self.font)
        
        return self

class InputBox(wx.TextCtrl):
    def __init__(self, *args, **kwargs):
        wx.TextCtrl.__init__(self, *args, **kwargs)
        
        self.SetFont(DEFAULTFONT)

class MainPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        
        self.current_panel = None
        
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.content_sizer = wx.BoxSizer(wx.VERTICAL)
        self.title_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.title_text = Text(self, label="IT Inventory").setSize(28)   
        self.home_button = wx.Button(self, label="Home", size=(200,50))
        self.home_button.SetFont(DEFAULTFONT)
        
        self.main_sizer.Add(self.title_sizer, 0, wx.EXPAND|wx.HORIZONTAL|wx.ALL, 15)
        self.title_sizer.Add(self.title_text, 0)
        self.title_sizer.Add((1,1), 1, wx.EXPAND|wx.HORIZONTAL)
        self.title_sizer.Add(self.home_button, 0)
        self.main_sizer.Add(self.content_sizer, 1, wx.EXPAND|wx.ALL)
        
        self.home_button.Bind(wx.EVT_BUTTON, lambda x: self.goHome())
        
        self.SetSizerAndFit(self.main_sizer)
    
    def addBodyPanel(self, panel):
        self.content_sizer.Add(panel, 1, wx.EXPAND|wx.ALL)
    
    def setBodyPanel(self, panel):
        if self.current_panel:
            self.current_panel.Hide()
        
        self.current_panel = panel
        panel.Show()
        self.Layout()
        panel.SetFocus()
        panel.makeActive()
        
    def goHome(self):
        self.setBodyPanel(gui.asset_panel)

class InventoryPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        
        self.sku = self.name = self.count = None
        
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.dummy_button = wx.Button(self, size=(1,1))
        
        self.item_label = Text(self, label="Item")
        self.count_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.count_minus = wx.Button(self, label="-", size=(80,80))
        self.item_count = Text(self, label="Count")
        self.count_plus = wx.Button(self, label="+", size=(80,80))
        
        #self.dummy_button.Hide()
        
        self.count_minus.SetFont(DEFAULTFONT)
        self.count_plus.SetFont(DEFAULTFONT)
        self.item_label.setSize(60)
        self.item_count.setSize(60)
        
        self.main_sizer.Add((0,0), 1, wx.EXPAND|wx.ALL)
        self.main_sizer.Add(self.item_label, 0, wx.CENTER)
        self.main_sizer.Add(self.count_sizer, 0, wx.CENTER)
        self.count_sizer.Add(self.count_minus)
        self.count_sizer.Add(self.item_count, 0, wx.LEFT|wx.RIGHT, 15)
        self.count_sizer.Add(self.count_plus)
        self.main_sizer.Add((0,0), 1, wx.EXPAND|wx.ALL)
        
        self.Bind(wx.EVT_CHAR_HOOK, self.handleKeys)
        self.count_minus.Bind(wx.EVT_BUTTON, lambda x: self.changeCount(-1))
        self.count_plus.Bind(wx.EVT_BUTTON, lambda x: self.changeCount(+1))
        
        self.SetSizerAndFit(self.main_sizer)
        self.Layout()
        
    def makeActive(self):
        self.dummy_button.SetDefault()
        
    def setItem(self, sku):
        self.sku = sku
        self.name = database.getNameFromSku(sku)
        self.count = database.getCountFromSku(sku)
        
        self.item_label.SetLabel(self.name)
        self.item_count.SetLabel(str(self.count))
    
    def changeCount(self, by):
        self.count += by
        self.item_count.SetLabel(str(self.count))
        database.setCountForSKU(self.sku, self.count)
    
    def handleKeys(self, e):
        if e.GetUniChar() == 61:
            self.changeCount(1)
        elif e.GetUniChar() == 45:
            self.changeCount(-1)
        else:
            if e.GetUniChar() > 0:
                character = chr(e.GetKeyCode())
                gui.asset_panel.asset_input.AppendText(character)
                gui.main_panel.setBodyPanel(gui.asset_panel)

class AssetPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.asset_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.asset_label = Text(self, label="Asset ID")
        self.asset_input = InputBox(self, size=(500,50))
        self.asset_button = wx.Button(self, label="GO", size=(72,52))
        
        self.main_sizer.Add(self.asset_sizer, 1, wx.EXPAND|wx.HORIZONTAL|wx.TOP, 100)
        self.asset_sizer.Add((0,0), 1, wx.EXPAND|wx.HORIZONTAL)
        self.asset_sizer.Add(self.asset_label, 0, wx.CENTER)
        self.asset_sizer.Add(self.asset_input, 0, wx.CENTER|wx.LEFT, 15)
        self.asset_sizer.Add(self.asset_button, 0, wx.CENTER)
        self.asset_sizer.Add((0,0), 1, wx.EXPAND|wx.HORIZONTAL)
        
        self.asset_button.SetFont(DEFAULTFONT)
        self.asset_button.Bind(wx.EVT_BUTTON, lambda x: self.handleBarcode())
        self.asset_button.SetDefault()
        
        self.SetSizerAndFit(self.main_sizer)
        self.Layout()
        
    def makeActive(self):
        self.asset_button.SetDefault()
        
    def handleBarcode(self):
        barcode = self.asset_input.GetValue()
        if len(barcode) > 0:
            self.asset_input.Clear()
            
            sku = database.getSKUFromAssetCode(barcode)
            if not sku:
                dialog = AddSKUDialog("SKU Doesn't Exist\n\nAdd SKU?", self)
                if dialog.getResponse():
                    sku = database.addSKU(barcode, barcode)
                else:
                    gui.asset_panel.asset_input.SetFocus()
                    return
            
            gui.inventory_panel.setItem(sku)
            gui.main_panel.setBodyPanel(gui.inventory_panel)

class AddSKUDialog(wx.Dialog):
    def __init__(self, text, *args, **kwargs):
        wx.Dialog.__init__(self, *args, **kwargs)
        
        self.add_sku = False
        winsound.MessageBeep(winsound.MB_OK)
        
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        title = Text(self, label=text)
                
        buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)
        no_button = wx.Button(self, label="NO (-)")
        yes_button = wx.Button(self, label="YES (+)")
        
        main_sizer.Add(title, 0, wx.ALL, 50)
        main_sizer.Add(buttons_sizer, 0, wx.EXPAND|wx.HORIZONTAL|wx.ALL, 50)
        buttons_sizer.Add(no_button, 0)
        buttons_sizer.Add(yes_button, 0)
        
        yes_button.Bind(wx.EVT_BUTTON, lambda x: self.setAddSku(True))
        no_button.Bind(wx.EVT_BUTTON, lambda x: self.setAddSku(False))
        self.Bind(wx.EVT_CHAR_HOOK, self.handleKeys)
        
        no_button.SetFont(DEFAULTFONT)
        yes_button.SetFont(DEFAULTFONT)
        
        self.SetSizerAndFit(main_sizer)
        self.Layout()
        self.ShowModal()
    
    def handleKeys(self, e):
        key = e.GetKeyCode()
        
        if key == 61:
            self.setAddSku(True)
        elif key == 45:
            self.setAddSku(False)
    
    def setAddSku(self, value):
        self.add_sku = value
        self.Close()
    
    def getResponse(self):
        return self.add_sku

class GUI(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, None, *args, **kwargs)
        
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.main_panel = MainPanel(self)
        self.asset_panel = AssetPanel(self.main_panel)
        self.inventory_panel = InventoryPanel(self.main_panel)
        
        self.main_panel.addBodyPanel(self.asset_panel)
        self.main_panel.addBodyPanel(self.inventory_panel)
        
        self.inventory_panel.Hide()
        #self.asset_panel.Hide()
        self.main_panel.setBodyPanel(self.asset_panel)
        #self.main_panel.setBodyPanel(self.inventory_panel)
                
        self.Show()

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
        
if __name__ == "__main__":
    database = Database()
    
    app = wx.App()
    
    DEFAULTFONT = wx.Font(36,
             wx.FONTFAMILY_DEFAULT,
             wx.FONTSTYLE_NORMAL,
             wx.FONTWEIGHT_BOLD)
    
    gui = GUI(size=(800,800))
    
    app.MainLoop()