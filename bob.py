import wx
import numpy
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas
#from wx import *

from wx.lib.embeddedimage import PyEmbeddedImage

# ***************** Catalog starts here *******************

catalog = {}
index = []


#----------------------------------------------------------------------
roi_del = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAA3NCSVQICAjb4U/gAAAAdUlE"
    "QVQokZWSUQ7AIAhDlZNx9B5tH2wESyVZfxbZq1hxA1h/ZPHxTwMaf01We9Hd4yyvoR6MPLFM"
    "YFOGpKNOtDD0DgRwBiL6dsJQO/Q7uN4SgBpDGyjxOqOzodNyaURLAUiAM9yeVtaPSc8PMZqI"
    "wc0Sc5j1ALwIRF2R+/MWAAAAAElFTkSuQmCC")
index.append('roi_del')
catalog['roi_del'] = roi_del
getroi_delData = roi_del.GetData
getroi_delImage = roi_del.GetImage
getroi_delBitmap = roi_del.GetBitmap
getroi_delIcon = roi_del.GetIcon

#----------------------------------------------------------------------
roi_dot_active = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAA3NCSVQICAjb4U/gAAAAMElE"
    "QVQokWM8cOAAAymAiSTVoxqQgb29g729A8k2YI0iFqxKDx48gCtCGUdjmggAAN4BDN9YFA/8"
    "AAAAAElFTkSuQmCC")
index.append('roi_dot_active')
catalog['roi_dot_active'] = roi_dot_active
getroi_dot_activeData = roi_dot_active.GetData
getroi_dot_activeImage = roi_dot_active.GetImage
getroi_dot_activeBitmap = roi_dot_active.GetBitmap
getroi_dot_activeIcon = roi_dot_active.GetIcon

#----------------------------------------------------------------------
roi_ellipse = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAA3NCSVQICAjb4U/gAAAAc0lE"
    "QVQokbWRUQ7AIAhDq9nBejSO1qP5QXQMzRaX2D+0D6QWSdhR3XL/Aa5Uk4qlGUiuAbeaIQGA"
    "IlZ8aVJzs9hr3NZPNwCJZvDW51OqaeJS/mZXGT5PSWKyokfnS96xSpQ0/0MnmScE8nGS0lsA"
    "7zofawNITTlivXWLXwAAAABJRU5ErkJggg==")
index.append('roi_ellipse')
catalog['roi_ellipse'] = roi_ellipse
getroi_ellipseData = roi_ellipse.GetData
getroi_ellipseImage = roi_ellipse.GetImage
getroi_ellipseBitmap = roi_ellipse.GetBitmap
getroi_ellipseIcon = roi_ellipse.GetIcon

#----------------------------------------------------------------------
roi_ellipse_active = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAA3NCSVQICAjb4U/gAAAAeUlE"
    "QVQokbVQQQ7AIAhD47/kZ+jPys92IHOMmS0usSeBtkgTAFpBXmL/EZRQ18q+7L0x3zolUHtv"
    "fizSgizZ0bXy08x7jWn+ZBORKkSaWe9PKYeNU9if7Z0Gz1JSRaDSGZ0decWqCgAi7AXDOMbq"
    "ETohvYngHftjPQCtpjyk+9GRUAAAAABJRU5ErkJggg==")
index.append('roi_ellipse_active')
catalog['roi_ellipse_active'] = roi_ellipse_active
getroi_ellipse_activeData = roi_ellipse_active.GetData
getroi_ellipse_activeImage = roi_ellipse_active.GetImage
getroi_ellipse_activeBitmap = roi_ellipse_active.GetBitmap
getroi_ellipse_activeIcon = roi_ellipse_active.GetIcon

#----------------------------------------------------------------------
roi_free = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAA3NCSVQICAjb4U/gAAAAdUlE"
    "QVQokbVSQQ7AIAirxof1aTytT9uBxXTOGT2sJ8Q2UKBIwgnqERtAG97kpKDEHhdviVTEgxqB"
    "zJAcKyS7f7jek/WLbbJHsq7Zb4ymHRJJAYL5XgmcRyrjgz3kPI8XtyXwqdweIpDmpvAZNgAS"
    "90+w/H6tF6NBMqpgM5TPAAAAAElFTkSuQmCC")
index.append('roi_free')
catalog['roi_free'] = roi_free
getroi_freeData = roi_free.GetData
getroi_freeImage = roi_free.GetImage
getroi_freeBitmap = roi_free.GetBitmap
getroi_freeIcon = roi_free.GetIcon

#----------------------------------------------------------------------
roi_dot = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAA3NCSVQICAjb4U/gAAAALklE"
    "QVQokWM8cOAAAymAiSTVoxqQgYPDAQeHAyTbgDWKWHAodcAVoYyjMU0EAADiEw1hU2m1LwAA"
    "AABJRU5ErkJggg==")
index.append('roi_dot')
catalog['roi_dot'] = roi_dot
getroi_dotData = roi_dot.GetData
getroi_dotImage = roi_dot.GetImage
getroi_dotBitmap = roi_dot.GetBitmap
getroi_dotIcon = roi_dot.GetIcon

#----------------------------------------------------------------------
roi_info = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAA3NCSVQICAjb4U/gAAAAcklE"
    "QVQokb2RwQ3AMAgDSdXBPJpH82h9IKWEUtR86leCuNhWhiTb0ZnuANIkvbgAAMwYJyQBROZ4"
    "bpM04zyTi+0NzCdJkyQpudVAE881Yj63lhTjuWENPMuk7S5Sud0Bb9oGig4W2n9y8NLpv36M"
    "VAONLl48Qt+soOpsAAAAAElFTkSuQmCC")
index.append('roi_info')
catalog['roi_info'] = roi_info
getroi_infoData = roi_info.GetData
getroi_infoImage = roi_info.GetImage
getroi_infoBitmap = roi_info.GetBitmap
getroi_infoIcon = roi_info.GetIcon

#----------------------------------------------------------------------
roi_pan = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAA3NCSVQICAjb4U/gAAAAnklE"
    "QVQokZWSsRKDMAxDX7gOzdjf8ciasd/ZkZVRvxTGDkDOUIcemnKKZCt2kiTuYAhZs+mGwWyC"
    "PHY8Z8OqBhZy2CeFbzCbpPKnw7FedvwcGFqSHdWfvSdJ2mt7wwkVsjQCD0Aqq2elALOP9PZR"
    "29UWSSrHGC9f3w9gCNmeeovk0WZlNkP9rXJenFQgQw7VgQGQxmdHTW/TF4h/6wW+y+E/tAQQ"
    "4TYAAAAASUVORK5CYII=")
index.append('roi_pan')
catalog['roi_pan'] = roi_pan
getroi_panData = roi_pan.GetData
getroi_panImage = roi_pan.GetImage
getroi_panBitmap = roi_pan.GetBitmap
getroi_panIcon = roi_pan.GetIcon

#----------------------------------------------------------------------
roi_rectangl = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAA3NCSVQICAjb4U/gAAAAT0lE"
    "QVQokc2SQQqAMAwEt9KHzdPytHmaB0U8aSsIzSUQZggJ29TM1DZFfxF6EnAEVU4hSdULXRUV"
    "6NcIeF5wtP+PXlC4v9VRQRlPVFsvfDvophPpstJ7HQAAAABJRU5ErkJggg==")
index.append('roi_rectangl')
catalog['roi_rectangl'] = roi_rectangl
getroi_rectanglData = roi_rectangl.GetData
getroi_rectanglImage = roi_rectangl.GetImage
getroi_rectanglBitmap = roi_rectangl.GetBitmap
getroi_rectanglIcon = roi_rectangl.GetIcon

#----------------------------------------------------------------------
roi_rotate = PyEmbeddedImage(
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAA3NCSVQICAjb4U/gAAAAaUlE"
    "QVQokZVR2xGAMAgLXcyM5mhxMz+8q1iQK/ls84BgktDBSF/JX5dEULABmB/pIA2n/5ZYJVzS"
    "ZEiUGNOSkbxr1NhOS+SbnLdUYEyPnqCd0BakDT7wG38SUs3CRqx10cRLb93Bo730DZoRMZ3M"
    "iTmuAAAAAElFTkSuQmCC")
index.append('roi_rotate')
catalog['roi_rotate'] = roi_rotate
getroi_rotateData = roi_rotate.GetData
getroi_rotateImage = roi_rotate.GetImage
getroi_rotateBitmap = roi_rotate.GetBitmap
getroi_rotateIcon = roi_rotate.GetIcon



class MatplotlibContext(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'some title')
        self.panel = wx.Panel(self)
        self.fig = Figure()
        self.canvas = FigCanvas(self.panel, -1, self.fig)
        self.axes = self.fig.add_subplot(111)
        x = numpy.linspace(0, 6.28)
        y = numpy.sin(x)
        self.axes.plot(x, y)
        self.canvas.draw()
        self.canvas.mpl_connect('button_press_event', self.context_menu)        
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.vbox.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.panel.SetSizer(self.vbox)
        self.vbox.Fit(self)

    def context_menu(self, event):
        print 'in context_menu callback: clicked at (%g, %g)' % (event.x, event.y)
        menu = wx.Menu()
        for imname in index:
            icon = catalog[imname]
            bmp  = icon.GetBitmap()
            item_id = wx.NewId()
            item = wx.MenuItem(menu, item_id, imname)
            item.SetBitmap(bmp)
            menu.AppendItem(item)
            wx.EVT_MENU(menu, item_id, self.callback)
        self.PopupMenu(menu)
        menu.Destroy()

    def callback(self, event):
        print 'menu selection: %r' % event.GetId()

app = wx.App( False )
app.frame = MatplotlibContext()
app.frame.Show()
app.MainLoop()