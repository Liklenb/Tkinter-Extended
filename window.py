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
        self.minWidth = min_width
        self.minHeight = min_height
        self.maximized = maximized
        self.theme = theme


class Navigator:
    _pages = []
    size = (0, 0)

    @staticmethod
    def push(new_page: widget.StatefulWidget) -> None:
        new_page.first_state(Navigator.size)
        Navigator._pages.append(new_page)

    @staticmethod
    def pop() -> None:
        Navigator._pages.pop()
        Navigator.get_current().first_state(Navigator.size)

    @staticmethod
    def get_current() -> widget.StatefulWidget:
        return Navigator._pages[-1]


def run_app(settings: AppSettings = AppSettings(), child: widget.StatefulWidget = None):
    pygame.init()
    pygame.display.set_caption(settings.title)
    screen = pygame.display.set_mode((settings.width, settings.height))
    if settings.maximized:
        screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    pygame.display.set_icon(pygame.image.load("assets/icon.png"))
    clock = pygame.time.Clock()
    if child is not None:
        Navigator.size = screen.get_size()
        Navigator.push(child)
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
            image = pygame.image.frombytes(Navigator.get_current().image_bytes, Navigator.get_current().image.size,
                                           "RGBA")
            screen.blit(image, (0, 0))
            pygame.display.flip()
