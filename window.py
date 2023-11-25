import widget
from color import Color, Colors
from icon import Icons
import pygame


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
    pygame.init()
    pygame.display.set_caption(settings.title)
    screen = pygame.display.set_mode((settings.width, settings.height))
    if settings.maximized:
        screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    if child is not None:
        child.first_state(screen.get_size())
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    widget.Event.on_click(event)
                if event.type == pygame.MOUSEMOTION:
                    widget.Event.on_motion(event)
                if event.type == pygame.MOUSEWHEEL:
                    # print(event)
                    widget.Event.on_scroll(event)
            screen.fill((255, 255, 255))
            image = pygame.image.frombytes(child.image_bytes, child.image.size, "RGBA")
            screen.blit(image, (0, 0))
            pygame.display.flip()


class Test(widget.StateFullWidget):
    def __init__(self):
        super().__init__()
        self.children = [
            widget.Text("0", font_size=50)
        ]
        self.count = 0

    def build(self) -> widget.Widget:
        return widget.Container(
            padding=widget.EdgeInsets.all(10),
            child=widget.Column(
                children=[
                    widget.FilledButton(text=widget.Text("ah"), on_click=self.add),
                    widget.Expanded(
                        child=widget.ListView(
                            children=self.children
                        )
                    )
                ]
            )
        )

    def add(self):
        self.count += 1
        self.children.append(widget.Text(str(self.count), font_size=50))
        self.refresh()


if __name__ == '__main__':
    run_app(child=Test(), settings=AppSettings(
        maximized=True,
    ))
