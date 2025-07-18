# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class com_win
###########################################################################

class com_win ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"pzh-com", pos = wx.DefaultPosition, size = wx.Size( 700,598 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		self.menubar = wx.MenuBar( 0 )
		self.m_menu_help = wx.Menu()
		self.m_menuItem_homPage = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"Home Page", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.Append( self.m_menuItem_homPage )

		self.m_menuItem_about = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"About Author", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.Append( self.m_menuItem_about )

		self.menubar.Append( self.m_menu_help, u"Help" )

		self.SetMenuBar( self.menubar )

		win_sizer = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook_recv = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_recv = wx.Panel( self.m_notebook_recv, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		receive_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_recvFormat = wx.StaticText( self.m_panel_recv, wx.ID_ANY, u"RX Format:", wx.DefaultPosition, wx.Size( 70,15 ), 0 )
		self.m_staticText_recvFormat.Wrap( -1 )

		self.m_staticText_recvFormat.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		receive_win.Add( self.m_staticText_recvFormat, 0, wx.ALL, 5 )

		m_choice_recvFormatChoices = [ u"Char", u"Hex" ]
		self.m_choice_recvFormat = wx.Choice( self.m_panel_recv, wx.ID_ANY, wx.DefaultPosition, wx.Size( 50,20 ), m_choice_recvFormatChoices, 0 )
		self.m_choice_recvFormat.SetSelection( 0 )
		receive_win.Add( self.m_choice_recvFormat, 0, wx.ALL, 5 )

		self.m_staticText_null1 = wx.StaticText( self.m_panel_recv, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 450,20 ), 0 )
		self.m_staticText_null1.Wrap( -1 )

		receive_win.Add( self.m_staticText_null1, 0, wx.ALL, 5 )

		self.m_button_recvClear = wx.Button( self.m_panel_recv, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.Size( 50,30 ), 0 )
		self.m_button_recvClear.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		receive_win.Add( self.m_button_recvClear, 0, wx.ALL, 5 )

		self.m_textCtrl_recv = wx.TextCtrl( self.m_panel_recv, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 700,180 ), wx.TE_MULTILINE )
		self.m_textCtrl_recv.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_textCtrl_recv.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		receive_win.Add( self.m_textCtrl_recv, 0, wx.ALL, 5 )


		self.m_panel_recv.SetSizer( receive_win )
		self.m_panel_recv.Layout()
		receive_win.Fit( self.m_panel_recv )
		self.m_notebook_recv.AddPage( self.m_panel_recv, u"Receive", False )

		win_sizer.Add( self.m_notebook_recv, 1, wx.EXPAND |wx.ALL, 5 )

		edit_win = wx.GridSizer( 0, 2, 0, 0 )

		self.m_notebook_settings = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_settings = wx.Panel( self.m_notebook_settings, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		setting_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_comPort = wx.StaticText( self.m_panel_settings, wx.ID_ANY, u"Com Port:", wx.DefaultPosition, wx.Size( 130,15 ), wx.ALIGN_RIGHT )
		self.m_staticText_comPort.Wrap( -1 )

		self.m_staticText_comPort.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		setting_win.Add( self.m_staticText_comPort, 0, wx.ALL, 5 )

		m_choice_comPortChoices = []
		self.m_choice_comPort = wx.Choice( self.m_panel_settings, wx.ID_ANY, wx.DefaultPosition, wx.Size( 120,20 ), m_choice_comPortChoices, 0 )
		self.m_choice_comPort.SetSelection( 0 )
		setting_win.Add( self.m_choice_comPort, 0, wx.ALL, 5 )

		self.m_staticText_baudrate = wx.StaticText( self.m_panel_settings, wx.ID_ANY, u"Baud Rate:", wx.DefaultPosition, wx.Size( 130,15 ), wx.ALIGN_RIGHT )
		self.m_staticText_baudrate.Wrap( -1 )

		self.m_staticText_baudrate.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		setting_win.Add( self.m_staticText_baudrate, 0, wx.ALL, 5 )

		m_choice_baudrateChoices = [ u"256000", u"128000", u"115200", u"57600", u"38400", u"19200", u"9600", u"4800" ]
		self.m_choice_baudrate = wx.Choice( self.m_panel_settings, wx.ID_ANY, wx.DefaultPosition, wx.Size( 120,20 ), m_choice_baudrateChoices, 0 )
		self.m_choice_baudrate.SetSelection( 2 )
		self.m_choice_baudrate.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		setting_win.Add( self.m_choice_baudrate, 0, wx.ALL, 5 )

		self.m_staticText_dataBits = wx.StaticText( self.m_panel_settings, wx.ID_ANY, u"Data Bits:", wx.DefaultPosition, wx.Size( 130,15 ), wx.ALIGN_RIGHT )
		self.m_staticText_dataBits.Wrap( -1 )

		self.m_staticText_dataBits.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		setting_win.Add( self.m_staticText_dataBits, 0, wx.ALL, 5 )

		m_choice_dataBitsChoices = [ u"8", u"7", u"6", u"5" ]
		self.m_choice_dataBits = wx.Choice( self.m_panel_settings, wx.ID_ANY, wx.DefaultPosition, wx.Size( 120,20 ), m_choice_dataBitsChoices, 0 )
		self.m_choice_dataBits.SetSelection( 0 )
		setting_win.Add( self.m_choice_dataBits, 0, wx.ALL, 5 )

		self.m_staticText_stopBits = wx.StaticText( self.m_panel_settings, wx.ID_ANY, u"Stop Bits:", wx.DefaultPosition, wx.Size( 130,15 ), wx.ALIGN_RIGHT )
		self.m_staticText_stopBits.Wrap( -1 )

		self.m_staticText_stopBits.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		setting_win.Add( self.m_staticText_stopBits, 0, wx.ALL, 5 )

		m_choice_stopBitsChoices = [ u"1", u"1.5", u"2" ]
		self.m_choice_stopBits = wx.Choice( self.m_panel_settings, wx.ID_ANY, wx.DefaultPosition, wx.Size( 120,20 ), m_choice_stopBitsChoices, 0 )
		self.m_choice_stopBits.SetSelection( 0 )
		setting_win.Add( self.m_choice_stopBits, 0, wx.ALL, 5 )

		self.m_staticText_parityBits = wx.StaticText( self.m_panel_settings, wx.ID_ANY, u"Parity Bits", wx.DefaultPosition, wx.Size( 130,15 ), wx.ALIGN_RIGHT )
		self.m_staticText_parityBits.Wrap( -1 )

		self.m_staticText_parityBits.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		setting_win.Add( self.m_staticText_parityBits, 0, wx.ALL, 5 )

		m_choice_parityBitsChoices = [ u"None", u"Odd", u"Even", u"Mark", u"Space" ]
		self.m_choice_parityBits = wx.Choice( self.m_panel_settings, wx.ID_ANY, wx.DefaultPosition, wx.Size( 120,20 ), m_choice_parityBitsChoices, 0 )
		self.m_choice_parityBits.SetSelection( 0 )
		setting_win.Add( self.m_choice_parityBits, 0, wx.ALL, 5 )

		self.m_staticText_null2 = wx.StaticText( self.m_panel_settings, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,15 ), 0 )
		self.m_staticText_null2.Wrap( -1 )

		setting_win.Add( self.m_staticText_null2, 0, wx.ALL, 5 )

		self.m_bitmap_led = wx.StaticBitmap( self.m_panel_settings, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 40,40 ), 0 )
		setting_win.Add( self.m_bitmap_led, 0, wx.ALL, 5 )

		self.m_button_openClose = wx.Button( self.m_panel_settings, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.Size( 80,40 ), 0 )
		self.m_button_openClose.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		setting_win.Add( self.m_button_openClose, 0, wx.ALL, 5 )


		self.m_panel_settings.SetSizer( setting_win )
		self.m_panel_settings.Layout()
		setting_win.Fit( self.m_panel_settings )
		self.m_notebook_settings.AddPage( self.m_panel_settings, u"Settings", False )

		edit_win.Add( self.m_notebook_settings, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_notebook_send = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_send = wx.Panel( self.m_notebook_send, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		send_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_sendFormat = wx.StaticText( self.m_panel_send, wx.ID_ANY, u"TX Format:", wx.DefaultPosition, wx.Size( 70,15 ), 0 )
		self.m_staticText_sendFormat.Wrap( -1 )

		self.m_staticText_sendFormat.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		send_win.Add( self.m_staticText_sendFormat, 0, wx.ALL, 5 )

		m_choice_sendFormatChoices = [ u"Char", u"Hex" ]
		self.m_choice_sendFormat = wx.Choice( self.m_panel_send, wx.ID_ANY, wx.DefaultPosition, wx.Size( 50,20 ), m_choice_sendFormatChoices, 0 )
		self.m_choice_sendFormat.SetSelection( 0 )
		send_win.Add( self.m_choice_sendFormat, 0, wx.ALL, 5 )

		self.m_staticText_null3 = wx.StaticText( self.m_panel_send, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,20 ), 0 )
		self.m_staticText_null3.Wrap( -1 )

		send_win.Add( self.m_staticText_null3, 0, wx.ALL, 5 )

		self.m_button_sendClear = wx.Button( self.m_panel_send, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.Size( 50,30 ), 0 )
		self.m_button_sendClear.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		send_win.Add( self.m_button_sendClear, 0, wx.ALL, 5 )

		self.m_textCtrl_send = wx.TextCtrl( self.m_panel_send, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,105 ), wx.TE_MULTILINE )
		self.m_textCtrl_send.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.m_textCtrl_send.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		send_win.Add( self.m_textCtrl_send, 0, wx.ALL, 5 )

		self.m_staticText_null4 = wx.StaticText( self.m_panel_send, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,15 ), 0 )
		self.m_staticText_null4.Wrap( -1 )

		send_win.Add( self.m_staticText_null4, 0, wx.ALL, 5 )

		self.m_button_send = wx.Button( self.m_panel_send, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.Size( 80,40 ), 0 )
		self.m_button_send.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		send_win.Add( self.m_button_send, 0, wx.ALL, 5 )


		self.m_panel_send.SetSizer( send_win )
		self.m_panel_send.Layout()
		send_win.Fit( self.m_panel_send )
		self.m_notebook_send.AddPage( self.m_panel_send, u"Send", False )

		edit_win.Add( self.m_notebook_send, 1, wx.EXPAND |wx.ALL, 5 )


		win_sizer.Add( edit_win, 1, wx.EXPAND, 5 )


		self.SetSizer( win_sizer )
		self.Layout()
		self.statusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.showHomepageMessage, id = self.m_menuItem_homPage.GetId() )
		self.Bind( wx.EVT_MENU, self.showAboutMessage, id = self.m_menuItem_about.GetId() )
		self.m_choice_recvFormat.Bind( wx.EVT_CHOICE, self.setRecvFormat )
		self.m_button_recvClear.Bind( wx.EVT_BUTTON, self.clearRecvDisplay )
		self.m_choice_comPort.Bind( wx.EVT_ENTER_WINDOW, self.refreshComPort )
		self.m_button_openClose.Bind( wx.EVT_BUTTON, self.openClosePort )
		self.m_choice_sendFormat.Bind( wx.EVT_CHOICE, self.setSendFormat )
		self.m_button_sendClear.Bind( wx.EVT_BUTTON, self.clearSendDisplay )
		self.m_button_send.Bind( wx.EVT_BUTTON, self.sendData )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def showHomepageMessage( self, event ):
		event.Skip()

	def showAboutMessage( self, event ):
		event.Skip()

	def setRecvFormat( self, event ):
		event.Skip()

	def clearRecvDisplay( self, event ):
		event.Skip()

	def refreshComPort( self, event ):
		event.Skip()

	def openClosePort( self, event ):
		event.Skip()

	def setSendFormat( self, event ):
		event.Skip()

	def clearSendDisplay( self, event ):
		event.Skip()

	def sendData( self, event ):
		event.Skip()


