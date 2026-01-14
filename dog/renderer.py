import cairo

class DogRenderer:
    def draw(self, cr, width, height, state, t):
        cr.set_source_rgba(0, 0, 0, 0)
        cr.set_operator(cairo.OPERATOR_SOURCE)
        cr.paint()
        cr.set_operator(cairo.OPERATOR_OVER)

        # Outline dog (placeholder)
        cr.set_line_width(3)
        cr.set_source_rgba(1, 1, 1, 0.9)

        # head
        cr.arc(width/2, height/2 - 20, 25, 0, 6.28)
        cr.stroke()

        # body
        cr.rectangle(width/2 - 30, height/2, 60, 50)
        cr.stroke()
