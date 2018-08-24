# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jul 11 2018)
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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"tinyPyCOM", pos = wx.DefaultPosition, size = wx.Size( 700,598 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.menubar = wx.MenuBar( 0 )
		self.m_menu_help = wx.Menu()
		self.m_menuItem_homPage = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"Home Page", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.Append( self.m_menuItem_homPage )

		self.m_menuItem_about = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"About Author", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.Append( self.m_menuItem_about )

		self.menubar.Append( self.m_menu_help, u"Help" )

		self.SetMenuBar( self.menubar )

		win_sizer = wx.BoxSizer( wx.VERTICAL )

		receive_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_receive = wx.StaticText( self, wx.ID_ANY, u"Receive:", wx.DefaultPosition, wx.Size( 700,25 ), 0 )
		self.m_staticText_receive.Wrap( -1 )

		self.m_staticText_receive.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Narrow" ) )
		self.m_staticText_receive.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText_receive.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		receive_win.Add( self.m_staticText_receive, 0, wx.ALL, 5 )

		self.m_staticText_recvFormat = wx.StaticText( self, wx.ID_ANY, u"Format:", wx.DefaultPosition, wx.Size( 50,15 ), 0 )
		self.m_staticText_recvFormat.Wrap( -1 )

		self.m_staticText_recvFormat.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		receive_win.Add( self.m_staticText_recvFormat, 0, wx.ALL, 5 )

		m_choice_recvFormatChoices = [ u"Char", wx.EmptyString, u"Hex" ]
		self.m_choice_recvFormat = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 50,20 ), m_choice_recvFormatChoices, 0 )
		self.m_choice_recvFormat.SetSelection( 0 )
		receive_win.Add( self.m_choice_recvFormat, 0, wx.ALL, 5 )

		self.m_staticText_null1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 480,20 ), 0 )
		self.m_staticText_null1.Wrap( -1 )

		receive_win.Add( self.m_staticText_null1, 0, wx.ALL, 5 )

		self.m_button_recvClear = wx.Button( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.Size( 50,30 ), 0 )
		self.m_button_recvClear.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		receive_win.Add( self.m_button_recvClear, 0, wx.ALL, 5 )

		self.m_textCtrl_recv = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 700,180 ), wx.TE_MULTILINE )
		self.m_textCtrl_recv.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		receive_win.Add( self.m_textCtrl_recv, 0, wx.ALL, 5 )


		win_sizer.Add( receive_win, 1, wx.EXPAND, 5 )

		edit_win = wx.GridSizer( 0, 2, 0, 0 )

		setting_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_settings = wx.StaticText( self, wx.ID_ANY, u"Settings:", wx.DefaultPosition, wx.Size( 350,25 ), 0 )
		self.m_staticText_settings.Wrap( -1 )

		self.m_staticText_settings.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Narrow" ) )
		self.m_staticText_settings.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText_settings.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		setting_win.Add( self.m_staticText_settings, 0, wx.ALL, 5 )

		self.m_staticText_comPort = wx.StaticText( self, wx.ID_ANY, u"Com Port:", wx.DefaultPosition, wx.Size( 150,15 ), wx.ALIGN_RIGHT )
		self.m_staticText_comPort.Wrap( -1 )

		self.m_staticText_comPort.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		setting_win.Add( self.m_staticText_comPort, 0, wx.ALL, 5 )

		m_choice_comPortChoices = []
		self.m_choice_comPort = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 120,20 ), m_choice_comPortChoices, 0 )
		self.m_choice_comPort.SetSelection( 0 )
		setting_win.Add( self.m_choice_comPort, 0, wx.ALL, 5 )

		self.m_staticText_baudrate = wx.StaticText( self, wx.ID_ANY, u"Baud Rate:", wx.DefaultPosition, wx.Size( 150,15 ), wx.ALIGN_RIGHT )
		self.m_staticText_baudrate.Wrap( -1 )

		self.m_staticText_baudrate.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		setting_win.Add( self.m_staticText_baudrate, 0, wx.ALL, 5 )

		m_choice_baudrateChoices = [ u"256000", u"128000", u"115200", u"57600", u"38400", u"19200", u"9600", u"4800" ]
		self.m_choice_baudrate = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 120,20 ), m_choice_baudrateChoices, 0 )
		self.m_choice_baudrate.SetSelection( 2 )
		self.m_choice_baudrate.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		setting_win.Add( self.m_choice_baudrate, 0, wx.ALL, 5 )

		self.m_staticText_dataBits = wx.StaticText( self, wx.ID_ANY, u"Data Bits:", wx.DefaultPosition, wx.Size( 150,15 ), wx.ALIGN_RIGHT )
		self.m_staticText_dataBits.Wrap( -1 )

		self.m_staticText_dataBits.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		setting_win.Add( self.m_staticText_dataBits, 0, wx.ALL, 5 )

		m_choice_dataBitsChoices = [ u"8", u"7", u"6", u"5" ]
		self.m_choice_dataBits = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 120,20 ), m_choice_dataBitsChoices, 0 )
		self.m_choice_dataBits.SetSelection( 0 )
		setting_win.Add( self.m_choice_dataBits, 0, wx.ALL, 5 )

		self.m_staticText_stopBits = wx.StaticText( self, wx.ID_ANY, u"Stop Bits:", wx.DefaultPosition, wx.Size( 150,15 ), wx.ALIGN_RIGHT )
		self.m_staticText_stopBits.Wrap( -1 )

		self.m_staticText_stopBits.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		setting_win.Add( self.m_staticText_stopBits, 0, wx.ALL, 5 )

		m_choice_stopBitsChoices = [ u"1", u"1.5", u"2" ]
		self.m_choice_stopBits = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 120,20 ), m_choice_stopBitsChoices, 0 )
		self.m_choice_stopBits.SetSelection( 0 )
		setting_win.Add( self.m_choice_stopBits, 0, wx.ALL, 5 )

		self.m_staticText_parityBits = wx.StaticText( self, wx.ID_ANY, u"Parity Bits", wx.DefaultPosition, wx.Size( 150,15 ), wx.ALIGN_RIGHT )
		self.m_staticText_parityBits.Wrap( -1 )

		self.m_staticText_parityBits.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		setting_win.Add( self.m_staticText_parityBits, 0, wx.ALL, 5 )

		m_choice_parityBitsChoices = [ u"None", u"Odd", u"Even", u"Mark", u"Space" ]
		self.m_choice_parityBits = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 120,20 ), m_choice_parityBitsChoices, 0 )
		self.m_choice_parityBits.SetSelection( 0 )
		setting_win.Add( self.m_choice_parityBits, 0, wx.ALL, 5 )

		self.m_staticText_null2 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 90,15 ), 0 )
		self.m_staticText_null2.Wrap( -1 )

		setting_win.Add( self.m_staticText_null2, 0, wx.ALL, 5 )

		self.m_bitmap_led = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		setting_win.Add( self.m_bitmap_led, 0, wx.ALL, 5 )

		self.m_button_openClose = wx.Button( self, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.Size( 80,40 ), 0 )
		self.m_button_openClose.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		setting_win.Add( self.m_button_openClose, 0, wx.ALL, 5 )


		edit_win.Add( setting_win, 1, wx.EXPAND, 5 )

		send_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_send = wx.StaticText( self, wx.ID_ANY, u"Send:", wx.DefaultPosition, wx.Size( 350,25 ), 0 )
		self.m_staticText_send.Wrap( -1 )

		self.m_staticText_send.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Narrow" ) )
		self.m_staticText_send.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		send_win.Add( self.m_staticText_send, 0, wx.ALL, 5 )

		self.m_staticText_sendFormat = wx.StaticText( self, wx.ID_ANY, u"Format:", wx.DefaultPosition, wx.Size( 50,15 ), 0 )
		self.m_staticText_sendFormat.Wrap( -1 )

		self.m_staticText_sendFormat.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		send_win.Add( self.m_staticText_sendFormat, 0, wx.ALL, 5 )

		m_choice_sendFormatChoices = [ u"Char", u"Hex" ]
		self.m_choice_sendFormat = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 50,20 ), m_choice_sendFormatChoices, 0 )
		self.m_choice_sendFormat.SetSelection( 0 )
		send_win.Add( self.m_choice_sendFormat, 0, wx.ALL, 5 )

		self.m_staticText_null3 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 130,20 ), 0 )
		self.m_staticText_null3.Wrap( -1 )

		send_win.Add( self.m_staticText_null3, 0, wx.ALL, 5 )

		self.m_button_sendClear = wx.Button( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.Size( 50,30 ), 0 )
		self.m_button_sendClear.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		send_win.Add( self.m_button_sendClear, 0, wx.ALL, 5 )

		self.m_textCtrl_send = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,105 ), wx.TE_MULTILINE )
		self.m_textCtrl_send.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		send_win.Add( self.m_textCtrl_send, 0, wx.ALL, 5 )

		self.m_staticText_null4 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,15 ), 0 )
		self.m_staticText_null4.Wrap( -1 )

		send_win.Add( self.m_staticText_null4, 0, wx.ALL, 5 )

		self.m_button_send = wx.Button( self, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.Size( 80,40 ), 0 )
		self.m_button_send.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		send_win.Add( self.m_button_send, 0, wx.ALL, 5 )


		edit_win.Add( send_win, 1, wx.EXPAND, 5 )


		win_sizer.Add( edit_win, 1, wx.EXPAND, 5 )


		self.SetSizer( win_sizer )
		self.Layout()
		self.statusBar_sizer = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

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


