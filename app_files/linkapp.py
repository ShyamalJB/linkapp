import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk as gtk

class mainapp:
    def __init__(self):
     self.builder=gtk.Builder()
     self.builder.add_from_file("linkapp.glade")
     self.builder.connect_signals(self)


     win=self.builder.get_object("mainwin")
     win.connect("delete-event", gtk.main_quit)
     win.show()




myapp=mainapp()
gtk.main()
