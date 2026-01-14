import gi
gi.require_version("Rsvg", "2.0")
from gi.repository import Rsvg
import cairo

class DogRenderer:
    def __init__(self):
        self.handle = Rsvg.Handle.new_from_file("assets/dog.svg")

    def _get_svg_size(self):
        size = self.handle.get_intrinsic_size_in_pixels()

        # New API: (has_size, width, height, baseline)
        if isinstance(size, tuple) and len(size) >= 3:
            _, w, h, *_ = size
            return w, h

        # Old API fallback
        return size

    def draw(self, cr, width, height, state, t):
        # transparent background
        cr.set_source_rgba(0, 0, 0, 0)
        cr.set_operator(cairo.OPERATOR_SOURCE)
        cr.paint()
        cr.set_operator(cairo.OPERATOR_OVER)

        svg_w, svg_h = self._get_svg_size()

        if svg_w > 0 and svg_h > 0:
            scale = min(width / svg_w, height / svg_h)

            cr.save()
            cr.scale(scale, scale)
            self.handle.render_cairo(cr)
            cr.restore()
