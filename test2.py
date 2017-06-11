import wx
class App(wx.App):
    def __init__(self):
        wx.App.__init__(self)
    def OnInit(self):
        image = wx.Image('1.png', wx.BITMAP_TYPE_PNG)
        self.frame = main_frame(parent=None,title='antitroll',image=image)
        self.SetTopWindow(self.frame) 
	return True
   

class main_frame(wx.Frame):
    def __init__(self,parent,title,image=None):
        wx.Frame.__init__(self,parent,title=title)
        
        if image:
            temp = image.ConvertToBitmap()
            #TODO: check the code here for key bindings. Not working. 
            self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)
            #self.bmp.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
            #self.bmp.Bind(wx.EVT_CHAR, self.OnKeyDown)
            self.bmp.Bind(wx.EVT_LEFT_DCLICK,self.OnMouseClick)
            #self.bmp.SetFocus()
        self.ShowFullScreen(True)
	self.Show()
   
    def OnMouseClick(self,event):
        wx.MessageBox('mouse event %s captured'%event.GetEventType(), 'Info', 
                            wx.OK | wx.ICON_INFORMATION)
        event.Skip()
   
    def OnKeyDown(self, event):
        keycode = event.GetKeyCode()
        print keycode
        if keycode == wx.WXK_SPACE:
            print "you pressed the spacebar!"
        event.Skip() 
	

if __name__=='__main__':
    app=App()
    app.MainLoop()


