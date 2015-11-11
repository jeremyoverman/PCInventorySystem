import wx

setup = """

<Category:

"""

class GUI(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        
        self.loadSetup()
        
    def loadSetup(self):
        self.categories = []
        
        for line in setup.split("\n"):
            print line

if __name__ == "__main__":
    app = wx.App()
    
    frame = wx.Frame(None, -1, "Grid")
    
    panel = wx.Panel(frame)
    sizer = wx.BoxSizer(wx.HORIZONTAL)
    panel.SetSizerAndFit(sizer)
    
    gui = GUI(panel)
    
    frame.Show()
    
    app.MainLoop()