import wx, wx.lib.newevent
from gui import NumberPad, Main
import database
import warrantylookup
import datetime
import threading

barcode_evt, EVT_BARCODE = wx.lib.newevent.NewEvent()

class GUI(Main):
    def __init__(self, parent):
        Main.__init__(self, parent)
        
        self.barcode_button.Bind(wx.EVT_BUTTON, self.handleBarcode)
        self.defect_panel.Bind(wx.EVT_CHAR_HOOK, self.focusBarcode)
        self.barcode_panel.Bind(wx.EVT_CHAR_HOOK, self.focusBarcode)
        self.kbd_button.Bind(wx.EVT_TOGGLEBUTTON, self.toggleKeyboard)
        
        self.handleVirtualKeyboard()
        
        self.Show()

    def handleBarcode(self, evt=None):
        barcode = self.barcode_input.GetValue()
        barcode = barcode.upper()
        self.barcode_input.Clear()
        self.barcode_input.SetValue(barcode)
        self.barcode_input.Clear()
        
        evt = barcode_evt(barcode=barcode)
        wx.PostEvent(self.defect_panel, evt)
        
    def focusBarcode(self, evt):
        unichar = evt.GetUniChar()
        if not self.barcode_input.HasFocus():
            self.barcode_input.SetFocus()
            if unichar != 13:
                if not evt.ShiftDown(): char = chr(unichar).lower()
                else: char = chr(unichar)
                self.barcode_input.AppendText(char)
            else:
                 self.handleBarcode()
        else:
            if unichar == 13:
                self.handleBarcode()
            else:
                evt.Skip()
    
    def toggleKeyboard(self, evt=None):
        if not self.virtual_keyboard.IsShown():
            self.virtual_keyboard.Show()
            self.kbd_button.SetValue(True)
        else:
            self.virtual_keyboard.Show(False)
            self.kbd_button.SetValue(False)
        self.Layout()
        self.barcode_panel.Layout()
    
    def handleButton(self, evt):
        btn = evt.GetEventObject()
        label = btn.GetLabel()
        if len(label) == 1:
            self.barcode_input.AppendText(label)
        elif label == "BKSP":
            size = len(self.barcode_input.GetValue())
            self.barcode_input.Remove(size - 1, size)
        elif label == "CLEAR":
            self.barcode_input.Clear()
        elif label == "OK":
            self.handleBarcode()
        elif label == "HIDE KBD":
            self.toggleKeyboard()
    
    def handleVirtualKeyboard(self):
        buttons = self.virtual_keyboard.GetChildren()
        for button in buttons:
            button.Bind(wx.EVT_BUTTON, self.handleButton)

class Defect:
    def __init__(self):
        gui.defect_panel.Bind(EVT_BARCODE, self.handleBarcode)
        gui.defect_confirm_panel.Show(False)
        gui.defect_result_panel.Show(False)
        
        self.serial = None
        
        gui.defect_button_yes.Bind(wx.EVT_BUTTON, lambda evt: self.markDefective())
        gui.defect_button_no.Bind(wx.EVT_BUTTON, lambda evt: self.markDefective(defect=False))
        
        gui.defect_history_list.show_button.Bind(wx.EVT_BUTTON, lambda evt: self.showSerial())
    
    def showSerial(self):
        serial = gui.defect_history_list.getSelectedSerial()
        self.serial = serial
        self.handleBarcode(barcode=serial)
    
    def markDefective(self, defect=True):
        gui.defect_confirm_panel.Show(False)
        gui.defect_result_panel.Show(True)
        
        if defect:
            gui.defect_result_label_yes.Show(True)
            db.markDefective(self.serial)
        else:
            gui.defect_result_label_no.Show(True)
        gui.defect_panel.Layout()
        if gui.defect_history_list.lc.FindItem(-1, self.serial) == -1:
            gui.defect_history_list.addComputer(self.serial, "Done.")
        gui.defect_history_list.flagSerial(self.serial, (128,128,128))
        
    def cancel(self):
        gui.defect_result_label_no.Show(True)
    
    def dellLookup(self, serial):
        wx.CallAfter(gui.defect_history_list.addComputer, serial, "Loading...")
        enddate, ordernum, model = delllookup.getWarrantyInfo(serial)
        if not model:
            db.addPC(serial, "NA")
            wx.CallAfter(gui.defect_history_list.setSerialStatus, serial, "Done w/ no info.")
        else:
            db.addPC(serial, "DELL")
            db.Dell.addPC(serial, enddate, ordernum, model)
            wx.CallAfter(gui.defect_history_list.setSerialStatus, serial, "Done.")
        if self.serial == serial:
            wx.CallAfter(self.getDellInformation, serial)
    
    def getDellInformation(self, serial):
        manufacturer = db.getManufacturer(serial)
        if not manufacturer:
            thread = threading.Thread(target=self.dellLookup, args=(serial, ))
            thread.start()
        elif manufacturer == "DELL":
            enddate, ordernum, model = db.Dell.getInfo(serial)
            self.showPCInfo(serial, enddate, ordernum, model)
        else:
            self.showPCInfo(serial, None, None, None)
    
    def showPCInfo(self, serial, enddate=None, ordernum=None, model=None):
        if not enddate: enddate_text = "N/A"
        else: enddate_text = enddate_text = enddate
        
        if not ordernum: ordernum_text = "N/A"
        else: ordernum_text = ordernum
        
        if not model: model_text = "N/A"
        else: model_text = model

        gui.defect_model_name_value.SetLabel(model_text)
        gui.defect_warranty_end_value.SetLabel(enddate_text)
        gui.defect_order_number_value.SetLabel(ordernum_text)
        
        if not enddate:
            enddt = datetime.date(2000, 1, 1)
        else:
            dtsplit = enddate.split("-")
            enddt = datetime.date(int(dtsplit[0]), int(dtsplit[1]), int(dtsplit[2]))    
        
        if not db.isDefective(self.serial):
            if  gui.defect_auto_checkbox.IsChecked():
                self.markDefective()
            elif enddt < datetime.date.today():
                gui.defect_result_panel.Show(False)
                gui.defect_confirm_panel.Show(True)
                gui.defect_panel.Layout()
        else:
            gui.defect_confirm_panel.Show(False)
            gui.defect_result_panel.Show(True)
            gui.defect_result_label_yes.Show(True)
            gui.defect_panel.Layout()
    
    def handleBarcode(self, evt=None, barcode=None):
        if not evt:
            self.serial=barcode
        else:
            self.serial = evt.barcode
        
        gui.defect_result_label_yes.Show(False)
        gui.defect_result_label_no.Show(False)
        
        self.getDellInformation(self.serial)
        
        gui.defect_serial_value.SetLabel(self.serial)
        
    
if __name__ == "__main__":
    app = wx.App()
    
    db = database.Database()
    
    gui = GUI(None)
    numpad = NumberPad(gui)
    defect = Defect()
    delllookup = warrantylookup.Dell()
    
    #batch()
    
    #numpad.Show()
    
    app.MainLoop()