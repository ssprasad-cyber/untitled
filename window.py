
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class DogWindow(Gtk.Window):
    def __init__(self, width=200, height=200):
        super().__init__(type=Gtk.WindowType.POPUP)

        self.set_default_size(width, height)
        self.set_decorated(False)
        self.set_keep_above(True)
        self.set_skip_taskbar_hint(True)
        self.set_skip_pager_hint(True)
        self.set_app_paintable(True)

        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual:
            self.set_visual(visual)

        self.connect("destroy", Gtk.main_quit)
