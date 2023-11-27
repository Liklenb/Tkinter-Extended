from widget import (Size, EdgeInsets, Widget, StatefulWidget, MainAxisAlignment, CrossAxisAlignment, Text, FileImage,
                    Expanded, Column, Row, Center, Container, InkWell, FilledButton, Icon, IconButton)
from window import AppSettings, run_app
from color import Color, Colors
from icon import Icons


class Example(StatefulWidget):
    def build(self) -> Widget:
        return Text("Hello world", color=Colors.blue, font_size=50)


if __name__ == '__main__':
    run_app(settings=AppSettings(maximized=True), child=Example())
