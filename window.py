import tkinter
import widget
from color import Color, Colors


class FontFamilies:
    open_sans: str = "assets/font_families/OpenSans/OpenSans.ttf"


class Theme:
    def __init__(self,
                 background_color: Color = Colors.white,
                 foreground_color: Color = Colors.black,
                 font_family: str = FontFamilies.open_sans):
        self.background_color = background_color
        self.foreground_color = foreground_color
        self.font_family = font_family


class AppSettings:
    def __init__(self,
                 title: str = "Tkinter Extended",
                 width: int = 400,
                 height: int = 400,
                 min_width: int = 200,
                 min_height: int = 200,
                 maximized: bool = False,
                 theme: Theme = Theme(),
                 ):
        self.title = title
        self.width = width
        self.height = height
        self.geometry = f"{width}x{height}"
        self.minWidth = min_width
        self.minHeight = min_height
        self.maximized = maximized
        self.theme = theme


def run_app(settings: AppSettings = AppSettings(), child: widget.StateFullWidget = None):
    root = tkinter.Tk()
    root.title(settings.title)
    # set the window size
    root.geometry(settings.geometry)
    if settings.maximized:
        root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        root.attributes('-zoomed', True)
    root.minsize(settings.minWidth, settings.minHeight)

    canvas = tkinter.Canvas(root, width=root.winfo_screenwidth(),
                            height=root.winfo_screenheight(),
                            bg=settings.theme.background_color.hexadecimal,
                            highlightthickness=0)
    canvas.pack()
    root.update()
    if child is not None:
        child.first_state((root.winfo_width(), root.winfo_height()), canvas)

    root.mainloop()


class Test(widget.StateFullWidget):
    def __init__(self):
        super().__init__()
        self.value = 20

    def build(self) -> widget.Widget:
        return widget.Column(
            main_axis_alignment=widget.MainAxisAlignment.space_between,
            cross_axis_alignment=widget.CrossAxisAlignment.start,
            children=[
                widget.Text("Coucou", font_size=self.value),
                widget.FilledButton(
                    on_click=self.plus,
                    text=widget.Text("Click me"),
                )
            ]
        )

    def plus(self):
        self.value += 1
        self.refresh()


if __name__ == '__main__':
    run_app(child=Test(), settings=AppSettings(
        maximized=True,
    ))
