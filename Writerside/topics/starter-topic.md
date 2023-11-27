# About Tkinter Extended

## Widgets

The library allows you to create GUI applications with widgets. It is rendered using pygame. The library is mostly inspired by Flutter.

A widget is a fragment of the user interface. It is a building block of the application. Widgets can be combined to create more complex widgets. The library provides a set of basic widgets, but you can also create your own.

## Widget tree

The library render a widget tree. Each widget can have one, multiple or no children. The children are rendered inside the parent widget.

## Stateful widgets

Stateful widgets have a build method that returns a widget tree representing a state. The state can be updated by calling the ```refresh``` method. The widget tree will be rebuilt and the changes will be rendered.

## Start an application

To start an application, you need to call the ```run_app``` function. It takes a `StatefulWidget` as an argument. The widget will be rendered as the root widget of the application.

## Minimal Example

```python
from widget import (Size, EdgeInsets, Widget, StatefulWidget, MainAxisAlignment, CrossAxisAlignment, Text, FileImage,
                    Expanded, Column, Row, Center, Container, InkWell, FilledButton, Icon, IconButton)
from window import AppSettings, run_app
from color import Color, Colors
from icon import Icons


class Example(StatefulWidget):
    def build(self) -> Widget:
        return Text("Hello world")


if __name__ == '__main__':
    run_app(child=Example())
```

Here we create an `Example` widget as a subclass of `StatefulWidget`. The `build` method returns a `Text` widget. The `run_app` function takes the `Example` widget as an argument and renders it as the root widget of the application.

## More complex example

```python
from widget import (Size, EdgeInsets, Widget, StatefulWidget, MainAxisAlignment, CrossAxisAlignment, Text, FileImage,
                    Expanded, Column, Row, Center, Container, InkWell, FilledButton, Icon, IconButton)
from window import AppSettings, run_app
from color import Color, Colors
from icon import Icons


class Example(StatefulWidget):
    def __init__(self):
        super().__init__()
        self.counter = 0
        
    def build(self) -> Widget:
        return Container(
            padding=EdgeInsets.all(20),
            child=Column(
                main_axis_alignment=MainAxisAlignment.center,
                children=[
                    Container(
                        padding=EdgeInsets.all(20),
                        child=Text(f"Counter: {self.counter}"),
                    ),
                    Row(
                        main_axis_alignment=MainAxisAlignment.center,
                        children=[
                            Container(
                                padding=EdgeInsets.all(5),
                                child=FilledButton(
                                    on_click=self.increment,
                                    text=Text("Increment"),
                                ),
                            ),
                            Container(
                                padding=EdgeInsets.all(5),
                                child=FilledButton(
                                    on_click=self.decrement,
                                    text=Text("Decrement"),
                                ),
                            )
                        ],
                    ),
                ],
            ),
        )
    
    def increment(self):
        self.counter += 1
        self.refresh()
        
    def decrement(self):
        self.counter -= 1
        self.refresh()
        
    
if __name__ == '__main__':
    run_app(child=Example())
```

Here, each time the user clicks on the increment or decrement button, the counter is incremented or decremented and the method `refresh` is called. The widget tree is rebuilt and the changes are rendered.

## Widget Gallery

See the list of [all available widgets](Widget-gallery.md) and how to use them.
