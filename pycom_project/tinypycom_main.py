import wx
import sys, os
sys.path.append(os.path.abspath("../wxFormBuilder"))
import tinypycom_win

class mianWin(tinypycom_win.com_win):

    def clearRecvDisplay( self, event ):
        event.Skip()

    def openClosePort( self, event ):
        event.Skip()

    def clearSendDisplay( self, event ):
        event.Skip()

    def sendData( self, event ):
        self.m_textCtrl_recv.Clear()
        self.m_textCtrl_recv.SetValue('hello world')

if __name__ == '__main__':
    app = wx.App()

    main_win = mianWin(None)
    main_win.SetTitle(u"tinyPyCOM v.0.1.0 -- https://www.cnblogs.com/henjay724/")
    main_win.Show()

    app.MainLoop()
