
import gi, time
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

from window import DogWindow
from dog.renderer import DogRenderer
from dog.dog import Dog

class App:
    def __init__(self):
        self.window = DogWindow()
        self.dog = Dog()
        self.renderer = DogRenderer()

        self.area = Gtk.DrawingArea()
        self.area.connect("draw", self.on_draw)
        self.window.add(self.area)
        self.window.show_all()

        # position top-right
        screen = self.window.get_screen()
        sw = screen.get_width()
        self.window.move(sw - 220, 20)

        # 10 FPS → VERY light
        GLib.timeout_add(100, self.tick)

    def tick(self):
        self.dog.update()
        self.area.queue_draw()
        return True

    def on_draw(self, widget, cr):
        alloc = widget.get_allocation()
        self.renderer.draw(
            cr,
            alloc.width,
            alloc.height,
            self.dog.state,
            time.time()
        )

App()
Gtk.main()
