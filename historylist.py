import wx

class HistoryList(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        #Build the base object
        wx.Panel.__init__(self, parent, *args, **kwargs)
        
        panel_font = self.GetFont()
        panel_font.SetPointSize(12)
        self.SetFont(panel_font)
        
        self.lc = wx.ListCtrl(self, style=wx.LC_REPORT|wx.LC_SINGLE_SEL)
         
        self.items = []
         
        #Set font size
        font = self.lc.GetFont()
        font.SetPointSize(18)
         
        self.lc.SetFont(font)
         
        #Build container sizer
        self.static_box = wx.StaticBox(self, label="History")
        self.container_sizer = wx.StaticBoxSizer(self.static_box, wx.HORIZONTAL)
        self.container_sizer.Add(self.lc, 1, wx.EXPAND|wx.ALL)
         
        #Build Buttons
        self.button_sizer = wx.BoxSizer(wx.VERTICAL)
        self.up_button = wx.Button(self, label="UP", size=(85,85))
        self.show_button = wx.Button(self, label="SHOW", size=(85,85))
        self.down_button = wx.Button(self, label="DOWN", size=(85,85))
         
        self.button_sizer.Add(self.up_button, 0)
        self.button_sizer.Add((0,0), 1, wx.EXPAND|wx.ALL)
        self.button_sizer.Add(self.show_button, 0)
        self.button_sizer.Add((0,0), 1, wx.EXPAND|wx.ALL)
        self.button_sizer.Add(self.down_button, 0)
         
        for btn in (self.up_button, self.show_button, self.down_button):
            btn.SetFont(font)
         
        #Configure List
        column_width = 148
        self.lc.InsertColumn(0, "Serial", width=column_width)
        self.lc.InsertColumn(1, "Status", width=column_width)
         
        #Bindings
        self.down_button.Bind(wx.EVT_BUTTON, lambda evt: self.moveSelection("down"))
        self.up_button.Bind(wx.EVT_BUTTON, lambda evt: self.moveSelection("up"))
         
        #Tie it all together
        self.container_sizer.Add(self.button_sizer, 0, wx.EXPAND|wx.ALL)
         
        self.SetSizerAndFit(self.container_sizer)
        
        
    def addComputer(self, serial, status):
        self.items.append(serial)
        self.lc.InsertStringItem(0, serial)
        self.setSerialStatus(serial, status)
        #self.lc.Append((serial, status))
        self.lc.Select(0)
        self.Update()
        
    def moveSelection(self, direction):
        current_selection = self.lc.GetFirstSelected()
        if direction == "down" and current_selection < len(self.items) - 1:
            self.lc.Select(current_selection, 0)
            self.lc.Select(current_selection + 1)
        elif direction == "up" and current_selection > 0:
            self.lc.Select(current_selection, 0)
            self.lc.Select(current_selection - 1)
        
        self.lc.EnsureVisible(self.lc.GetFirstSelected())
        self.lc.SetFocus()
        
    def setSerialStatus(self, serial, status):
        row = self.lc.FindItem(-1, serial)
        item = wx.ListItem()
        item.SetId(row)
        item.SetColumn(1)
        item.SetMask(wx.LIST_MASK_TEXT)
        item.SetText(status)
        self.lc.SetItem(item)
        #self.lc.SetItem(index=row, column=1, label="test", imageId=-1)
        
#     def removeSerial(self, serial):
#         row = self.items.index(serial)
#         self.lc.DeleteItem(row)
#         self.items.pop(row)
#         self.lc.SetFocus()
        
    def flagSerial(self, serial, colour=None):
        row = self.lc.FindItem(-1, serial)
        
        print serial, row
        
        if not colour:
            colour = wx.Colour(255, 255, 255)
        else:
            colour = wx.Colour(*colour)            
            
        self.lc.SetItemBackgroundColour(row, colour)
        
        self.lc.SetFocus()
        
    def getSelectedSerial(self):
        row = self.lc.GetFirstSelected()
        return self.lc.GetItemText(row)


def fillHistoryList():
    historylist.addComputer("GVN7ZQ1", "Loading...")
    historylist.addComputer("4747VV1", "Loading...")
    historylist.addComputer("AAAAAAA", "Loading...")
    historylist.addComputer("BBBBBBB", "Loading...")
    historylist.addComputer("CCCCCCC", "Loading...")
    historylist.addComputer("DDDDDDD", "Loading...")
    historylist.addComputer("EEEEEEE", "Loading...")
    historylist.addComputer("FFFFFFF", "Loading...")

if __name__ == "__main__":
    app = wx.App()
    
    frame = wx.Frame(None, -1, "History Panel", size=(400, 320))
    
    panel = wx.Panel(frame)
    sizer = wx.BoxSizer(wx.HORIZONTAL)
    
    historylist = HistoryList(panel)
    
    sizer.Add(historylist, 1, wx.EXPAND|wx.ALL)
    
    fillHistoryList()
    
    historylist.flagSerial("4747VV1", (255,0,0))
    
    panel.SetSizerAndFit(sizer)
    frame.Show()
    
    app.MainLoop()