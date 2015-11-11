# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import virtualkeyboard
import historylist

###########################################################################
## Class NumberPad
###########################################################################

class NumberPad ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,800 ), style = 0|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		container_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.main_panel.SetFont( wx.Font( 24, 74, 90, 92, False, "Arial" ) )
		
		grid_sizer = wx.GridBagSizer( 0, 0 )
		grid_sizer.SetFlexibleDirection( wx.BOTH )
		grid_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.display_text = wx.StaticText( self.main_panel, wx.ID_ANY, u"123456", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.display_text.Wrap( -1 )
		self.display_text.SetFont( wx.Font( 36, 74, 90, 90, False, "Arial" ) )
		
		grid_sizer.Add( self.display_text, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.button_one = wx.Button( self.main_panel, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		grid_sizer.Add( self.button_one, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.button_two = wx.Button( self.main_panel, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		grid_sizer.Add( self.button_two, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.button_three = wx.Button( self.main_panel, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		grid_sizer.Add( self.button_three, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.button_four = wx.Button( self.main_panel, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		grid_sizer.Add( self.button_four, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.button_five = wx.Button( self.main_panel, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		grid_sizer.Add( self.button_five, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.button_six = wx.Button( self.main_panel, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		grid_sizer.Add( self.button_six, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.button_seven = wx.Button( self.main_panel, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
		grid_sizer.Add( self.button_seven, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.button_eight = wx.Button( self.main_panel, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
		grid_sizer.Add( self.button_eight, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.button_nine = wx.Button( self.main_panel, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
		grid_sizer.Add( self.button_nine, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.button_cancel = wx.Button( self.main_panel, wx.ID_ANY, u"ESC", wx.DefaultPosition, wx.DefaultSize, 0 )
		grid_sizer.Add( self.button_cancel, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.button_0 = wx.Button( self.main_panel, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		grid_sizer.Add( self.button_0, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.button_ok = wx.Button( self.main_panel, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		grid_sizer.Add( self.button_ok, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		
		grid_sizer.AddGrowableCol( 0 )
		grid_sizer.AddGrowableCol( 1 )
		grid_sizer.AddGrowableCol( 2 )
		grid_sizer.AddGrowableRow( 0 )
		grid_sizer.AddGrowableRow( 1 )
		grid_sizer.AddGrowableRow( 2 )
		grid_sizer.AddGrowableRow( 3 )
		grid_sizer.AddGrowableRow( 4 )
		
		self.main_panel.SetSizer( grid_sizer )
		self.main_panel.Layout()
		grid_sizer.Fit( self.main_panel )
		container_sizer.Add( self.main_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( container_sizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class Main
###########################################################################

class Main ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1280,1024 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		container_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.main_panel.Hide()
		
		chooser_sizer = wx.BoxSizer( wx.VERTICAL )
		
		
		chooser_sizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.defective_chooser = wx.Button( self.main_panel, wx.ID_ANY, u"Defective Equipment", wx.DefaultPosition, wx.Size( 400,100 ), 0 )
		chooser_sizer.Add( self.defective_chooser, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		chooser_sizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		self.main_panel.SetSizer( chooser_sizer )
		self.main_panel.Layout()
		chooser_sizer.Fit( self.main_panel )
		container_sizer.Add( self.main_panel, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.barcode_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.barcode_panel.SetFont( wx.Font( 36, 74, 90, 90, False, "Arial" ) )
		
		barcode_container_sizer = wx.BoxSizer( wx.VERTICAL )
		
		bacrode_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.barcode_label = wx.StaticText( self.barcode_panel, wx.ID_ANY, u"Asset Tag", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.barcode_label.Wrap( -1 )
		bacrode_sizer.Add( self.barcode_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.kbd_button = wx.ToggleButton( self.barcode_panel, wx.ID_ANY, u"KBD", wx.DefaultPosition, wx.DefaultSize, 0 )
		bacrode_sizer.Add( self.kbd_button, 0, wx.ALL, 5 )
		
		self.barcode_input = wx.TextCtrl( self.barcode_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,80 ), 0 )
		bacrode_sizer.Add( self.barcode_input, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.barcode_button = wx.Button( self.barcode_panel, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bacrode_sizer.Add( self.barcode_button, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		barcode_container_sizer.Add( bacrode_sizer, 1, wx.EXPAND, 5 )
		
		self.virtual_keyboard = virtualkeyboard.Keyboard(self.barcode_panel)
		self.virtual_keyboard.Hide()
		
		barcode_container_sizer.Add( self.virtual_keyboard, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.barcode_panel.SetSizer( barcode_container_sizer )
		self.barcode_panel.Layout()
		barcode_container_sizer.Fit( self.barcode_panel )
		container_sizer.Add( self.barcode_panel, 0, wx.EXPAND |wx.ALL, 0 )
		
		self.defect_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.defect_panel.SetFont( wx.Font( 36, 74, 90, 90, False, "Arial" ) )
		
		defect_container_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.defect_warranty_loading = wx.StaticText( self.defect_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.defect_warranty_loading.Wrap( -1 )
		defect_container_sizer.Add( self.defect_warranty_loading, 0, wx.ALL, 5 )
		
		defect_sizer = wx.BoxSizer( wx.VERTICAL )
		
		defect_top_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		defect_info_sizer = wx.GridBagSizer( 0, 0 )
		defect_info_sizer.SetFlexibleDirection( wx.BOTH )
		defect_info_sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.defect_serial_label = wx.StaticText( self.defect_panel, wx.ID_ANY, u"Service Tag/Serial:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.defect_serial_label.Wrap( -1 )
		defect_info_sizer.Add( self.defect_serial_label, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.defect_serial_value = wx.StaticText( self.defect_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.defect_serial_value.Wrap( -1 )
		defect_info_sizer.Add( self.defect_serial_value, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.defect_model_name_label = wx.StaticText( self.defect_panel, wx.ID_ANY, u"Machine Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.defect_model_name_label.Wrap( -1 )
		defect_info_sizer.Add( self.defect_model_name_label, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.defect_model_name_value = wx.StaticText( self.defect_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.defect_model_name_value.Wrap( -1 )
		defect_info_sizer.Add( self.defect_model_name_value, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.defect_warranty_end_label = wx.StaticText( self.defect_panel, wx.ID_ANY, u"Warranty Expires:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.defect_warranty_end_label.Wrap( -1 )
		defect_info_sizer.Add( self.defect_warranty_end_label, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.defect_warranty_end_value = wx.StaticText( self.defect_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.defect_warranty_end_value.Wrap( -1 )
		defect_info_sizer.Add( self.defect_warranty_end_value, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.defect_order_number_label = wx.StaticText( self.defect_panel, wx.ID_ANY, u"Dell Order Number:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.defect_order_number_label.Wrap( -1 )
		defect_info_sizer.Add( self.defect_order_number_label, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.defect_order_number_value = wx.StaticText( self.defect_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.defect_order_number_value.Wrap( -1 )
		defect_info_sizer.Add( self.defect_order_number_value, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		defect_top_sizer.Add( defect_info_sizer, 2, wx.EXPAND, 5 )
		
		self.defect_history_list = historylist.HistoryList(self.defect_panel, style=wx.LC_REPORT)
		defect_top_sizer.Add( self.defect_history_list, 1, wx.ALL, 5 )
		
		
		defect_sizer.Add( defect_top_sizer, 1, wx.EXPAND, 5 )
		
		defect_feedback_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		
		defect_feedback_sizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.defect_confirm_panel = wx.Panel( self.defect_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.defect_confirm_panel.Hide()
		
		defect_confirm_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.defect_confirm_label = wx.StaticText( self.defect_confirm_panel, wx.ID_ANY, u"Mark defective?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.defect_confirm_label.Wrap( -1 )
		defect_confirm_sizer.Add( self.defect_confirm_label, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		defect_button_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		
		defect_button_sizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.defect_button_no = wx.Button( self.defect_confirm_panel, wx.ID_ANY, u"NO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.defect_button_no.SetMinSize( wx.Size( 175,175 ) )
		
		defect_button_sizer.Add( self.defect_button_no, 0, wx.ALL, 5 )
		
		self.defect_button_yes = wx.Button( self.defect_confirm_panel, wx.ID_ANY, u"YES", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.defect_button_yes.SetMinSize( wx.Size( 175,175 ) )
		
		defect_button_sizer.Add( self.defect_button_yes, 0, wx.ALL, 5 )
		
		
		defect_button_sizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		defect_confirm_sizer.Add( defect_button_sizer, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.defect_confirm_panel.SetSizer( defect_confirm_sizer )
		self.defect_confirm_panel.Layout()
		defect_confirm_sizer.Fit( self.defect_confirm_panel )
		defect_feedback_sizer.Add( self.defect_confirm_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.defect_result_panel = wx.Panel( self.defect_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.defect_result_panel.Hide()
		
		defect_result_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.defect_result_label_yes = wx.StaticText( self.defect_result_panel, wx.ID_ANY, u"MARKED DEFECTIVE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.defect_result_label_yes.Wrap( -1 )
		self.defect_result_label_yes.SetFont( wx.Font( 36, 74, 90, 90, False, "Arial" ) )
		self.defect_result_label_yes.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		defect_result_sizer.Add( self.defect_result_label_yes, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.defect_result_label_no = wx.StaticText( self.defect_result_panel, wx.ID_ANY, u"NOT MARKED DEFECTIVE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.defect_result_label_no.Wrap( -1 )
		self.defect_result_label_no.SetFont( wx.Font( 36, 74, 90, 90, False, "Arial" ) )
		self.defect_result_label_no.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.defect_result_label_no.Hide()
		
		defect_result_sizer.Add( self.defect_result_label_no, 0, wx.ALL, 5 )
		
		
		self.defect_result_panel.SetSizer( defect_result_sizer )
		self.defect_result_panel.Layout()
		defect_result_sizer.Fit( self.defect_result_panel )
		defect_feedback_sizer.Add( self.defect_result_panel, 1, wx.EXPAND|wx.ALL, 5 )
		
		
		defect_feedback_sizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		defect_sizer.Add( defect_feedback_sizer, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		defect_auto_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.defect_auto_checkbox = wx.CheckBox( self.defect_panel, wx.ID_ANY, u"Auto Defect Assets", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.defect_auto_checkbox.SetFont( wx.Font( 18, 74, 90, 90, False, "Arial" ) )
		
		defect_auto_sizer.Add( self.defect_auto_checkbox, 0, wx.ALL, 5 )
		
		
		defect_sizer.Add( defect_auto_sizer, 0, wx.EXPAND, 5 )
		
		
		defect_container_sizer.Add( defect_sizer, 1, wx.EXPAND, 5 )
		
		
		self.defect_panel.SetSizer( defect_container_sizer )
		self.defect_panel.Layout()
		defect_container_sizer.Fit( self.defect_panel )
		container_sizer.Add( self.defect_panel, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		self.SetSizer( container_sizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

