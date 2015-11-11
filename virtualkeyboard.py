import wx

class Keyboard(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        
        self.buttons = {}
        
        self.container_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.character_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.container_sizer.Add(self.character_sizer, 1, wx.EXPAND|wx.ALL)
        
        self.fillCharacters()
        
        self.SetSizerAndFit(self.container_sizer)
        
    def fillCharacters(self):
        num_row = wx.BoxSizer(wx.HORIZONTAL)
        num_row.Add((42,85))
        for c in "1234567890":
            btn = wx.Button(self, label=c, size=(85,85))
            num_row.Add(btn)
        
        top_row = wx.BoxSizer(wx.HORIZONTAL)
        for c in "QWERTYUIOP":
            btn = wx.Button(self, label=c, size=(85,85))
            top_row.Add(btn)
        
        mid_row = wx.BoxSizer(wx.HORIZONTAL)
        mid_row.Add((42,85))
        for c in "ASDFGHJKL":
            btn = wx.Button(self, label=c, size=(85,85))
            mid_row.Add(btn)
            
        bot_row = wx.BoxSizer(wx.HORIZONTAL)
        bot_row.Add((85,85))
        for c in "ZXCVBNM":
            btn = wx.Button(self, label=c, size=(85,85))
            bot_row.Add(btn)
            
        bksp = wx.Button(self, label="BKSP", size=(200,85))
        num_row.Add(bksp)
        
        clear = wx.Button(self, label="CLEAR", size=(200,85))
        top_row.Add(clear)
        
        ok = wx.Button(self, label="OK", size=(200,85))
        mid_row.Add(ok)
        
        hide = wx.Button(self, label="HIDE KBD", size=(285,85))
        bot_row.Add(hide)
        
        self.character_sizer.Add(num_row, 0)    
        self.character_sizer.Add(top_row, 0)
        self.character_sizer.Add(mid_row, 0)
        self.character_sizer.Add(bot_row, 0)
        

if __name__ == "__main__":
    app = wx.App()
    
    frame = wx.Frame(None, -1, "Virtual Keyboard")
    
    panel = wx.Panel(frame)
    
    sizer = wx.BoxSizer(wx.VERTICAL)
    
    keyboard = Keyboard(panel)
    
    sizer.Add(keyboard, 1, wx.EXPAND|wx.ALL)
    
    panel.SetSizerAndFit(sizer)
    
    frame.Show()
    
    app.MainLoop()