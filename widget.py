from dataclasses import dataclass
from PIL import Image, ImageFont, ImageDraw, ImageTk
from colorama import Fore, Style
from color import Color, Colors
import tkinter
from sys import platform


class LayoutError(Exception):
    def __init__(self, message: str):
        self.message = message


@dataclass
class Size:
    width: int
    height: int

    def get(self) -> tuple[int, int]:
        return self.width, self.height

    def is_null(self) -> bool:
        return self.width == 0 and self.height == 0

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height


@dataclass
class Position:
    x: int
    y: int

    def set(self, axis: int, value: int):
        if axis == 0:
            self.x = value
        else:
            self.y = value


class EdgeInsets:
    def __init__(self, top: int = 0, right: int = 0, bottom: int = 0, left: int = 0):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

    def to_string(self):
        return f"Edge Insets {self.top} {self.right} {self.bottom} {self.left}"

    @staticmethod
    def all(value: int):
        return EdgeInsets(top=value, right=value, bottom=value, left=value)

    @staticmethod
    def horizontal(value: int):
        return EdgeInsets(top=0, right=value, bottom=0, left=value)

    @staticmethod
    def vertical(value: int):
        return EdgeInsets(top=value, right=0, bottom=value, left=0)

    def __eq__(self, other):
        return self.top == other.top and self.right == other.right and \
            self.bottom == other.bottom and self.left == other.left


class Event:
    registered_events = {
        "<Button-1>": [],
        "<Motion>": [],
        "<MouseWheel>": []
    }

    @staticmethod
    def on_click(event: tkinter.Event):
        for func in Event.registered_events["<Button-1>"]:
            func(event)

    @staticmethod
    def on_motion(event: tkinter.Event):
        for func in Event.registered_events["<Motion>"]:
            func(event)

    @staticmethod
    def on_scroll(event: tkinter.Event):
        for func in Event.registered_events["<MouseWheel>"]:
            func(event)

    @staticmethod
    def on_scroll_down(event: tkinter.Event):
        event.delta = -1
        for func in Event.registered_events["<MouseWheel>"]:
            func(event)

    @staticmethod
    def on_scroll_up(event: tkinter.Event):
        event.delta = 1
        for func in Event.registered_events["<MouseWheel>"]:
            func(event)

    @staticmethod
    def clear():
        Event.registered_events = {
            "<Button-1>": [],
            "<Motion>": [],
            "<MouseWheel>": []
        }


class Widget:
    def __init__(self):
        self.size: Size = Size(0, 0)
        self.image: Image = None
        self.constraints: tuple[int, int] = (0, 0)

    def before_pipeline(self):
        pass

    def layout(self, new: 'Widget' = None):
        pass

    def register_events(self, absolute_position: Position, state: 'StateFullWidget', new: 'Widget' = None):
        pass

    def draw(self, new: 'Widget' = None):
        pass

    def composite(self, new: 'Widget' = None) -> bool:
        pass


class MultipleChildrenWidget(Widget):
    def __init__(self):
        super().__init__()
        self.children: list[Widget] = []
        self.children_position: list[Position] = []

    def tree_as_changed(self: 'MultipleChildrenWidget', new: 'MultipleChildrenWidget') -> bool:
        if new is None:
            return False
        if len(self.children) != len(new.children):
            return True
        for i in range(len(self.children)):
            if type(self.children[i]) is not type(new.children[i]):
                return True
        return False

    def layout(self, new: 'MultipleChildrenWidget' = None):
        if new is None or self.tree_as_changed(new):
            self.children_position = [Position(0, 0) for _ in range(len(self.children))]
            for child in self.children:
                child.constraints = self.constraints
                child.layout()
                self.size.width = max(self.size.width, child.size.width)
                self.size.height = max(self.size.height, child.size.height)
        else:
            for i in range(len(self.children)):
                self.children[i].constraints = self.constraints
                self.children[i].layout(new.children[i])
                self.size.width = max(self.size.width, self.children[i].size.width)
                self.size.height = max(self.size.height, self.children[i].size.height)

    def register_events(self, absolute_position: Position, state: 'StateFullWidget',
                        new: 'MultipleChildrenWidget' = None):
        if new is not None:
            if self.tree_as_changed(new):
                for i in range(len(new.children)):
                    new.children[i].register_events(Position(absolute_position.x + new.children_position[i].x,
                                                             absolute_position.y + new.children_position[i].y),
                                                    state,
                                                    new.children[i])
            else:
                for i in range(len(self.children)):
                    self.children[i].register_events(Position(absolute_position.x + new.children_position[i].x,
                                                              absolute_position.y + new.children_position[i].y),
                                                     state,
                                                     new.children[i])
        else:
            for i in range(len(self.children)):
                self.children[i].register_events(Position(absolute_position.x + self.children_position[i].x,
                                                          absolute_position.y + self.children_position[i].y),
                                                 state)

    def draw(self, new: 'Column' = None):
        if new is None or self.tree_as_changed(new):
            for child in (self.children if new is None or not self.tree_as_changed(new) else new.children):
                child.draw()
        else:
            for i in range(len(self.children)):
                self.children[i].draw(new.children[i])

    def composite(self, new: 'MultipleChildrenWidget' = None) -> bool:
        if new is None:
            self.image = Image.new("RGBA", (self.size.width, self.size.height), (0, 0, 0, 0))
            for i in range(len(self.children)):
                self.children[i].composite()
                self.image.alpha_composite(self.children[i].image,
                                           (self.children_position[i].x, self.children_position[i].y))
            return True
        elif self.tree_as_changed(new):
            self.image = Image.new("RGBA", (new.size.width, new.size.height), (0, 0, 0, 0))
            for i in range(len(new.children)):
                new.children[i].composite()
                self.image.alpha_composite(new.children[i].image,
                                           (new.children_position[i].x, new.children_position[i].y))
            self.children = new.children
            return True
        else:
            need_composite = False
            for i in range(len(self.children)):
                if self.children[i].composite(new.children[i]):
                    need_composite = True
            if need_composite:
                self.image = Image.new("RGBA", (new.size.width, new.size.height), (0, 0, 0, 0))
                for i in range(len(self.children)):
                    self.image.alpha_composite(self.children[i].image, (new.children_position[i].x,
                                                                        new.children_position[i].y))
                return True
            return False


class SingleChildWidget(Widget):
    def __init__(self):
        super().__init__()
        self.child: Widget | None = None
        self.child_position: Position = Position(0, 0)

    def layout(self, new: 'SingleChildWidget' = None):
        if new is None:
            self.child.constraints = self.constraints
            self.child.layout()
            self.size = self.child.size
        else:
            self.child.constraints = self.constraints
            self.child.layout(new.child)
            new.size = new.child.size

    def register_events(self, absolute_position: Position, state: 'StateFullWidget', new: 'SingleChildWidget' = None):
        if new is not None:
            new.child.register_events(Position(absolute_position.x + self.child_position.x,
                                               absolute_position.y + self.child_position.y), state, new.child)
        else:
            self.child.register_events(Position(absolute_position.x + self.child_position.x,
                                                absolute_position.y + self.child_position.y), state)

    def draw(self, new: 'SingleChildWidget' = None):
        self.child.draw(new.child if new is not None else None)

    def composite(self, new: 'SingleChildWidget' = None) -> bool:
        if new is None:
            self.child.composite()
            self.image = self.child.image
            return True
        elif type(self.child) is not type(new.child):
            if new.child.composite():
                self.image = new.child.image
                self.child = new.child
                return True
            return False
        else:
            if self.child.composite(new.child):
                self.image = self.child.image
                return True
            return False


class StateFullWidget(SingleChildWidget):
    new_child: Widget = None
    main_state: 'StateFullWidget'

    garbage: ImageTk.PhotoImage
    canvas: tkinter.Canvas
    root: tkinter.Tk

    def build(self) -> Widget:
        pass

    def set_state(self):
        self.layout()
        Event.clear()
        self.register_events(Position(0, 0), self)
        self.draw()
        self.composite()
        self.canvas.delete("all")
        self.garbage = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=self.garbage, anchor=tkinter.NW)
        self.root.update()

    def first_state(self, constraints: tuple[int, int], root: tkinter.Tk, canvas: tkinter.Canvas):
        self.canvas = canvas
        self.root = root
        self.constraints = constraints
        self.layout()
        self.register_events(Position(0, 0), self)
        # register events
        self.canvas.bind("<Button-1>", Event.on_click)
        self.canvas.bind("<Motion>", Event.on_motion)
        if platform == "linux" or platform == "linux2":
            root.bind("<5>", Event.on_scroll_up)
            root.bind("<4>", Event.on_scroll_down)
        else:
            root.bind("<MouseWheel>", Event.on_scroll)
        self.draw()
        self.composite()
        self.garbage = ImageTk.PhotoImage(self.child.image)
        self.canvas.create_image(0, 0, image=self.garbage, anchor=tkinter.NW)

    def layout(self, new: 'Widget' = None):
        if self.child is None:
            self.child = self.build()
        else:
            self.new_child = self.build()
        self.child.constraints = self.constraints
        self.child.layout(self.new_child)
        if new is None:
            self.size = self.child.size
        else:
            new.size = self.child.size

    def register_events(self, absolute_position: Position, state: 'StateFullWidget', new: 'Widget' = None):
        self.main_state = state
        self.child.register_events(absolute_position, state, self.new_child)

    def draw(self, new: 'Widget' = None):
        self.child.draw(self.new_child)

    def composite(self, new: 'Widget' = None) -> bool:
        if new is not None:
            self.size = new.size
        if self.child.composite(self.new_child):
            self.image = self.child.image
            return True
        return False

    def refresh(self):
        self.main_state.set_state()


class MainAxisAlignment:
    @staticmethod
    def check_overflow(children: list[Widget], constraints: tuple[int, int], axis: int):
        min_size = 0
        for child in children:
            min_size += child.size.get()[axis]
        if min_size > constraints[axis] > 0:
            print(f"{Fore.YELLOW}Warning: Overflow detected!{Style.RESET_ALL}")

    @staticmethod
    def get_children_size(children: list[Widget], axis: int) -> int:
        size = 0
        for child in children:
            size += child.size.get()[axis]
        return size

    @staticmethod
    def start(children: list[Widget], children_position: list[Position], constraints: tuple[int, int], axis: int):
        MainAxisAlignment.check_overflow(children, constraints, axis)
        position = 0
        for i in range(len(children)):
            children_position[i].set(axis, position)
            position += children[i].size.get()[axis]

    @staticmethod
    def center(children: list[Widget], children_position: list[Position], constraints: tuple[int, int], axis: int):
        MainAxisAlignment.check_overflow(children, constraints, axis)
        children_size = MainAxisAlignment.get_children_size(children, axis)
        position = constraints[axis] // 2 - children_size // 2
        for i in range(len(children)):
            children_position[i].set(axis, position)
            position += children[i].size.get()[axis]

    @staticmethod
    def end(children: list[Widget], children_position: list[Position], constraints: tuple[int, int], axis: int):
        MainAxisAlignment.check_overflow(children, constraints, axis)
        children_size = MainAxisAlignment.get_children_size(children, axis)
        position = constraints[axis] - children_size
        for i in range(len(children)):
            children_position[i].set(axis, position)
            position += children[i].size.get()[axis]

    @staticmethod
    def space_around(children: list[Widget],
                     children_position: list[Position],
                     constraints: tuple[int, int],
                     axis: int):
        MainAxisAlignment.check_overflow(children, constraints, axis)
        space = constraints[axis] - MainAxisAlignment.get_children_size(children, axis)
        space_between = space // (len(children) + 3)
        position = space_between * 2
        for i in range(len(children)):
            children_position[i].set(axis, position)
            position += children[i].size.get()[axis] + space_between

    @staticmethod
    def space_between(children: list[Widget],
                      children_position: list[Position],
                      constraints: tuple[int, int],
                      axis: int):
        MainAxisAlignment.check_overflow(children, constraints, axis)
        space = constraints[axis] - MainAxisAlignment.get_children_size(children, axis)
        space_between = space // (len(children) - 1)
        position = 0
        for i in range(len(children)):
            children_position[i].set(axis, position)
            position += children[i].size.get()[axis] + space_between

    @staticmethod
    def space_evenly(children: list[Widget],
                     children_position: list[Position],
                     constraints: tuple[int, int],
                     axis: int):
        MainAxisAlignment.check_overflow(children, constraints, axis)
        space = constraints[axis] - MainAxisAlignment.get_children_size(children, axis)
        space_between = space // (len(children) + 1)
        position = space_between
        for i in range(len(children)):
            children_position[i].set(axis, position)
            position += children[i].size.get()[axis] + space_between


class CrossAxisAlignment:
    @staticmethod
    def start(*args):
        pass

    @staticmethod
    def center(children: list[Widget], children_position: list[Position], constraints: tuple[int, int], axis: int):
        for i in range(len(children)):
            children_position[i].set(axis, constraints[axis] // 2 - children[i].size.get()[axis] // 2)

    @staticmethod
    def end(children: list[Widget], children_position: list[Position], constraints: tuple[int, int], axis: int):
        for i in range(len(children)):
            children_position[i].set(axis, constraints[axis] - children[i].size.get()[axis])


class Text(Widget):
    def __init__(self, text: str, color: Color = Colors.black, font_size: int = 15):
        super().__init__()
        self.text = text
        self.color = color
        self.font_size = font_size
        self.font = ImageFont.truetype("assets/font_families/OpenSans/OpenSans.ttf", font_size)
        self.text_position: Position = Position(0, 0)

    def layout(self, new: 'Text' = None):
        if new is not None and (self.text != new.text or self.font_size != new.font_size):
            if self.font_size != new.font_size:
                self.font = ImageFont.truetype("assets/font_families/OpenSans/OpenSans.ttf", new.font_size)
            box = self.font.getbbox(new.text)
            new.size = Size(box[2] - box[0], box[3] - box[1])
            new.text_position = Position(-box[0], -box[1])
        elif new is None:
            box = self.font.getbbox(self.text)
            self.size = Size(box[2] - box[0], box[3] - box[1])
            self.text_position = Position(-box[0], -box[1])
        else:
            new.size = self.size
            new.text_position = self.text_position

    def draw(self, new: 'Text' = None):
        if new is None or self.text != new.text or self.color != new.color or self.font_size != new.font_size:
            if new is not None:
                provider = new
            else:
                provider = self
            self.image = Image.new("RGBA", (provider.size.width, provider.size.height), (255, 255, 255, 0))
            draw = ImageDraw.Draw(self.image)
            draw.text((provider.text_position.x, provider.text_position.y), provider.text,
                      font=self.font, fill=provider.color.hexadecimal)

    def composite(self, new: 'Text' = None) -> bool:
        if new is not None and (self.text != new.text or self.color != new.color or self.font_size != new.font_size):
            self.text = new.text
            self.color = new.color
            self.font_size = new.font_size
            self.size = new.size
            self.text_position = new.text_position
            return True
        if new is None:
            return True
        return False


class FileImage(Widget):
    def __init__(self, path: str, size: Size = Size(0, 0)):
        super().__init__()
        self.path = path
        self._size = size
        if not size.is_null():
            self.size = size

    def as_changed(self, new: 'FileImage'):
        return new.path != self.path or new._size != self._size

    def layout(self, new: 'FileImage' = None):
        if new is None:
            self.image = Image.open(self.path).convert("RGBA")
            if not self.size.is_null():
                self.image = self.image.resize(self.size.get())
            else:
                self.size = Size(self.image.width, self.image.height)
        else:
            if new.path != self.path:
                self.image = Image.open(new.path).convert("RGBA")
                if new._size.is_null():
                    new.size = Size(self.image.width, self.image.height)
                else:
                    new.size = new._size
                    self.image.resize(new._size.get())
            elif new._size != self._size:
                if not new.size.is_null():
                    self.image = self.image.resize(new.size.get())
                else:
                    new.size = Size(self.image.width, self.image.height)
            else:
                new.size = self.size

    def composite(self, new: 'FileImage' = None) -> bool:
        if new is None:
            return True
        if self.as_changed(new):
            if self.size != new.size:
                self.size = new.size
            elif self.path != new.path:
                self.path = new.path
            return True
        return False


class Icon(FileImage):
    def __init__(self, icon: str, size: int = 20, color: Color = Colors.black):
        super().__init__(icon, size=Size(size, size))
        self.color = color

    def as_changed(self, new: 'Icon'):
        return super().as_changed(new) or self.color != new.color

    def draw(self, new: 'Icon' = None):
        super().draw(new)
        if new is None or self.as_changed(new):
            if new is None:
                provider = self
            else:
                provider = new
            color_mask = Image.new("RGBA", (provider.size.get()),
                                   color=provider.color.rgb)
            self.image.paste(color_mask, (0, 0), self.image)

    def composite(self, new: 'Icon' = None) -> bool:
        value = super().composite(new)
        if new is not None and self.color != new.color:
            self.color = new.color
        return value


class Expanded(SingleChildWidget):
    def __init__(self, child: Widget, flex: int = 1):
        super().__init__()
        self.child = child
        self.axis = 1
        self.flex = flex

    def layout(self, new: 'SingleChildWidget' = None):
        if self.constraints[self.axis] == 0:
            raise LayoutError(f"Expanded was given unbounded {['width', 'height'][self.axis]}")
        if new is None:
            self.child.constraints = self.constraints
            self.child.layout()
        else:
            self.child.constraints = self.constraints
            self.child.layout(new.child)
        if self.axis == 0:
            if new is None:
                self.size = Size(max(self.child.size.width, self.constraints[0]),
                                 self.child.size.height)
            else:
                new.size = Size(max(new.child.size.width, self.constraints[0]),
                                new.child.size.height)
        else:
            if new is None:
                self.size = Size(self.child.size.width,
                                 max(self.child.size.height, self.constraints[1]))
            else:
                new.size = Size(new.child.size.width,
                                max(new.child.size.height, self.constraints[1]))

    def composite(self, new: 'SingleChildWidget' = None) -> bool:
        if new is None:
            self.child.composite()
            self.image = Image.new("RGBA", (self.size.width, self.size.height), (0, 0, 0, 0))
            self.image.alpha_composite(self.child.image, (0, 0))
            return True
        elif type(self.child) is not type(new.child):
            if new.child.composite():
                self.image = Image.new("RGBA", (new.size.width, new.size.height), (0, 0, 0, 0))
                self.image.alpha_composite(new.child.image, (0, 0))
                self.child = new.child
                return True
            return False
        else:
            if self.child.composite(new.child) or self.flex != new.flex:
                self.flex = new.flex
                self.image = Image.new("RGBA", (new.size.width, new.size.height), (0, 0, 0, 0))
                self.image.alpha_composite(self.child.image, (0, 0))
                return True
            return False


class Column(MultipleChildrenWidget):
    def __init__(self,
                 children: list[Widget],
                 main_axis_alignment: callable = MainAxisAlignment.start,
                 cross_axis_alignment: callable = CrossAxisAlignment.center):
        super().__init__()
        self.children = children
        self.children_position = [Position(0, 0) for _ in range(len(self.children))]
        self.main_axis_alignement = main_axis_alignment
        self.cross_axis_alignement = cross_axis_alignment

    def layout(self, new: 'Column' = None):
        if new is not None:
            provider = new
            if self.tree_as_changed(new):
                modifier = new
            else:
                modifier = self
        else:
            modifier = provider = self

        provider.size.height = self.constraints[1]

        flexs = []
        for child in modifier.children:
            if isinstance(child, Expanded):
                flexs.append(child.flex)

        # layout all non expanded children
        min_size = 0
        for i in range(len(modifier.children)):
            if isinstance(modifier.children[i], Expanded):
                continue
            modifier.children[i].constraints = (self.constraints[0], 0)
            modifier.children[i].layout(
                provider.children[i] if new is not None and not self.tree_as_changed(new) else None)
            provider.size.width = max(provider.size.width, provider.children[i].size.width)
            min_size += provider.children[i].size.height

        # layout all expanded children
        j = 0
        for i in range(len(modifier.children)):
            if not isinstance(modifier.children[i], Expanded):
                continue
            modifier.children[i].constraints = (self.constraints[0], (
                0 if not isinstance(modifier.children[i], Expanded) else (self.constraints[1] - min_size) * flexs[
                    j] // sum(flexs)))
            modifier.children[i].layout(
                provider.children[i] if new is not None and not self.tree_as_changed(new) else None)
            provider.size.width = max(provider.size.width, provider.children[i].size.width)
            if isinstance(modifier.children[i], Expanded):
                j += 1

        if provider.size.height == 0:
            for child in provider.children:
                provider.size.height += child.size.height
        provider.main_axis_alignement(provider.children, provider.children_position,
                                      (provider.size.width, provider.size.height), 1)
        provider.cross_axis_alignement(provider.children, provider.children_position,
                                       (provider.size.width, provider.size.height), 0)


class UnboundedColumn(MultipleChildrenWidget):
    def __init__(self,
                 children: list[Widget],
                 scroll_position: int = 0,
                 cross_axis_alignment: callable = CrossAxisAlignment.center):
        super().__init__()
        self.children = children
        self._children_position = [Position(0, 0) for _ in range(len(self.children))]
        self.children_position = [Position(0, 0) for _ in range(len(self.children))]
        self.cross_axis_alignement = cross_axis_alignment
        self.scroll_position = scroll_position

    def layout(self, new: 'Column' = None):
        if new is not None:
            provider = new
            if self.tree_as_changed(new):
                modifier = new
            else:
                modifier = self
        else:
            modifier = provider = self

        provider.size.height = self.constraints[1]
        if provider.size.height == 0:
            raise LayoutError("ListView was given unbounded height")

        for i in range(len(modifier.children)):
            modifier.children[i].constraints = (self.constraints[0], 0)
            modifier.children[i].layout(
                provider.children[i] if new is not None and not self.tree_as_changed(new) else None)
            provider.size.width = max(provider.size.width, provider.children[i].size.width)

        MainAxisAlignment.start(provider.children, provider._children_position,
                                (provider.size.width, 0), 1)
        provider.cross_axis_alignement(provider.children, provider._children_position,
                                       (provider.size.width, provider.size.height), 0)
        for y in range(len(provider.children)):
            provider.children_position[y].set(1, provider._children_position[y].y - provider.scroll_position)

    def composite(self, new: 'UnboundedColumn' = None) -> bool:
        value = super().composite(new)
        if new is not None:
            if not value and self.scroll_position != new.scroll_position:
                self.image = Image.new("RGBA", (new.size.width, new.size.height), (0, 0, 0, 0))
                for i in range(len(self.children)):
                    self.image.alpha_composite(self.children[i].image, (new.children_position[i].x,
                                                                        new.children_position[i].y))
                return True
        return value


class ListView(StateFullWidget):
    def __init__(self, children: list[Widget]):
        super().__init__()
        self.scroll_position = 0
        self.children = children

    def build(self) -> Widget:
        return UnboundedColumn(
            children=self.children,
            scroll_position=self.scroll_position,
        )

    def register_events(self, absolute_position: Position, state: 'StateFullWidget',
                        new: 'ListView' = None):
        Event.registered_events["<MouseWheel>"].append(self.on_scroll)
        super().register_events(absolute_position, state, new)

    def on_scroll(self, event):
        self.scroll_position += event.delta * 10
        self.main_state.set_state()


class Row(Column):
    def layout(self, new: 'Row' = None):
        if new is not None:
            provider = new
            if self.tree_as_changed(new):
                modifier = new
            else:
                modifier = self
        else:
            modifier = provider = self

        provider.size.width = self.constraints[0]

        flexs = []
        for child in modifier.children:
            if isinstance(child, Expanded):
                flexs.append(child.flex)

        # layout all non expanded children
        min_size = 0
        for i in range(len(modifier.children)):
            if isinstance(modifier.children[i], Expanded):
                continue
            modifier.children[i].constraints = (0, self.constraints[1])
            modifier.children[i].layout(
                provider.children[i] if new is not None and not self.tree_as_changed(new) else None)
            provider.size.height = max(provider.size.height, provider.children[i].size.height)
            min_size += provider.children[i].size.width

        # layout all expanded children
        j = 0
        for i in range(len(modifier.children)):
            if not isinstance(modifier.children[i], Expanded):
                continue
            modifier.children[i].axis = 0
            modifier.children[i].constraints = ((self.constraints[0] - min_size) * flexs[j] // sum(flexs),
                                                self.constraints[1])
            modifier.children[i].layout(
                provider.children[i] if new is not None and not self.tree_as_changed(new) else None)
            provider.size.height = max(provider.size.height, provider.children[i].size.height)
            if isinstance(modifier.children[i], Expanded):
                j += 1
        if provider.size.width == 0:
            for child in provider.children:
                provider.size.width += child.size.width
        provider.main_axis_alignement(provider.children, provider.children_position,
                                      (provider.size.width, provider.size.height), 0)
        provider.cross_axis_alignement(provider.children, provider.children_position,
                                       (provider.size.width, provider.size.height), 1)


class Center(SingleChildWidget):
    def __init__(self, child):
        super().__init__()
        self.child = child

    def layout(self, new: 'Center' = None):
        if new is None:
            self.child.constraints = self.constraints
            self.child.layout()
            self.size = Size(self.constraints[0], self.constraints[1])
        else:
            self.child.constraints = self.constraints
            self.child.layout(new.child)
            new.size = Size(self.constraints[0], self.constraints[1])

    def register_events(self, absolute_position: Position, state: 'StateFullWidget', new: 'Center' = None):
        self.child.register_events(
            Position(absolute_position.x + (
                    (new if new is not None else self).size.width - self.child.size.width) // 2,
                     absolute_position.y + (
                             (new if new is not None else self).size.height - self.child.size.height) // 2), state,
            new.child if new is not None else None)

    def draw(self, new: 'Center' = None):
        self.child.draw(new.child if new is not None else None)

    def composite(self, new: 'Center' = None):
        if self.child.composite(new.child if new is not None else None):
            provider = new if new is not None else self
            self.image = Image.new("RGBA", (provider.size.width, provider.size.height), (0, 0, 0, 0))
            self.image.alpha_composite(self.child.image,
                                       ((provider.size.width - provider.child.size.width) // 2,
                                        (provider.size.height - provider.child.size.height) // 2))
            if new is not None:
                self.size = new.size
            return True
        return False


class Container(SingleChildWidget):
    def __init__(self,
                 child: Widget,
                 background_color: Color = Colors.transparent,
                 padding: EdgeInsets = EdgeInsets.all(0),
                 border_radius: int = 0,
                 border_width: int = 0,
                 border_color: Color = Colors.transparent):
        super().__init__()
        self.child = child
        self.child_position = Position(0, 0)
        self.background_color = background_color
        self.padding = padding
        self.border_radius = border_radius
        self.border_width = border_width
        self.border_color = border_color
        self._image = None

    def as_changed(self, new: 'Container'):
        return (self.background_color != new.background_color
                or self.padding != new.padding
                or self.border_radius != new.border_radius
                or self.border_width != new.border_width
                or self.border_color != new.border_color
                or self.size != new.size)

    def layout(self, new: 'Container' = None):
        provider = new if new is not None else self
        modifier = self
        if new is not None and type(self.child) is not type(new.child):
            modifier = new
        modifier.child.constraints = (max(0, self.constraints[
            0] - provider.padding.left - provider.padding.right - provider.border_width * 2 - provider.border_radius),
                                      max(0, self.constraints[
                                          1] - provider.padding.top
                                          - provider.padding.bottom - provider.border_width * 2
                                          - provider.border_radius))
        modifier.child.layout(provider.child if new is not None and type(self.child) is type(new.child) else None)
        if 0 in self.constraints:
            provider.size = Size(
                modifier.child.size.width + provider.padding.left + provider.padding.right +
                provider.border_width * 2 + provider.border_radius,
                modifier.child.size.height + provider.padding.top + provider.padding.bottom +
                provider.border_width * 2 + provider.border_radius)
        else:
            provider.size = Size(self.constraints[0], self.constraints[1])
        provider.child_position = Position(provider.padding.left + provider.border_width + provider.border_radius // 2,
                                           provider.padding.top + provider.border_width + provider.border_radius // 2)

    def register_events(self, absolute_position: Position, state: 'StateFullWidget', new: 'Container' = None):
        self.child.register_events(Position(absolute_position.x + self.child_position.x,
                                            absolute_position.y + self.child_position.y), state,
                                   new.child if new is not None else None)

    def draw(self, new: 'Container' = None):
        if new is None:
            self._image = Image.new("RGBA", (self.size.width, self.size.height), (0, 0, 0, 0))
            draw = ImageDraw.Draw(self._image)
            draw.rounded_rectangle((0, 0, self.size.width - 1, self.size.height - 1),
                                   self.border_radius, fill=self.background_color.rgb, outline=self.border_color.rgb,
                                   width=self.border_width)
        elif self.as_changed(new):
            self._image = Image.new("RGBA", (new.size.width, new.size.height), (0, 0, 0, 0))
            draw = ImageDraw.Draw(self._image)
            draw.rounded_rectangle((0, 0, new.size.width - 1, new.size.height - 1),
                                   new.border_radius, fill=new.background_color.rgb, outline=new.border_color.rgb,
                                   width=new.border_width)
        self.child.draw(new.child if new is not None else None)

    def composite(self, new: 'Container' = None):
        result = False
        if self.child.composite(new.child if new is not None else None) or new is None or self.as_changed(new):
            if new is not None:
                self.background_color = new.background_color
                self.padding = new.padding
                self.border_radius = new.border_radius
                self.border_width = new.border_width
                self.border_color = new.border_color
                self.size = new.size
            self.image = self._image.copy()
            self.image.alpha_composite(self.child.image, (self.child_position.x, self.child_position.y))
            result = True
        return result


class InkWell(SingleChildWidget):
    absolute_position: Position

    def __init__(self, child: Widget, on_click: callable = None, on_hover: callable = None):
        super().__init__()
        self.child = child
        self.on_click = on_click
        self.on_hover = on_hover
        self.hover = False

    def _on_hover(self, event: tkinter.Event):
        if self.on_hover is not None and not self.hover and \
                self.child.size.width + self.absolute_position.x > event.x > self.absolute_position.x and \
                self.child.size.height + self.absolute_position.y > event.y > self.absolute_position.y:
            self.hover = True
            self.on_hover(True)
        elif self.on_hover is not None and self.hover and not \
                (self.child.size.width + self.absolute_position.x > event.x > self.absolute_position.x and
                 self.child.size.height + self.absolute_position.y > event.y > self.absolute_position.y):
            self.hover = False
            self.on_hover(False)

    def _on_click(self, event: tkinter.Event):
        if self.on_click is not None and \
                self.child.size.width + self.absolute_position.x > event.x > self.absolute_position.x and \
                self.child.size.height + self.absolute_position.y > event.y > self.absolute_position.y:
            self.on_click()

    def layout(self, new: 'InkWell' = None):
        self.child.constraints = self.constraints
        self.child.layout(new.child if new is not None else None)
        if new is not None:
            new.size = new.child.size
        else:
            self.size = self.child.size

    def register_events(self, absolute_position: Position, state: 'StateFullWidget', new: 'InkWell' = None):
        if new is not None and new.on_hover != self.on_hover:
            new.absolute_position = absolute_position
            Event.registered_events["<Button-1>"].append(new._on_click)
            Event.registered_events["<Motion>"].append(new._on_hover)
        else:
            self.absolute_position = absolute_position
            Event.registered_events["<Button-1>"].append(self._on_click)
            Event.registered_events["<Motion>"].append(self._on_hover)
        self.child.register_events(absolute_position, state, new.child if new is not None else None)

    def draw(self, new: 'InkWell' = None):
        self.child.draw(new.child if new is not None else None)

    def composite(self, new: 'InkWell' = None):
        if self.child.composite(new.child if new is not None else None) or new is None:
            self.image = self.child.image
            return True
        return False


class FilledButton(StateFullWidget):
    def __init__(self, text: Text, on_click: callable = lambda: None, color: Color = Colors.blue):
        super().__init__()
        self.color = color
        self.background_color = Color.alpha_blend(self.color, Colors.white.with_opacity(0.2))
        self.text = text
        self.on_click = on_click

    def build(self) -> Widget:
        return InkWell(
            child=Container(
                child=self.text,
                background_color=self.background_color,
                padding=EdgeInsets.horizontal(16),
                border_radius=20
            ),
            on_hover=self._on_hover,
            on_click=self._on_click
        )

    def _on_click(self):
        self.on_click()
        self.main_state.set_state()

    def _on_hover(self, hover: bool):
        if hover:
            self.background_color = self.color
        else:
            self.background_color = Color.alpha_blend(self.color, Colors.white.with_opacity(0.2))
        self.main_state.set_state()


class IconButton(StateFullWidget):
    def __init__(self, icon: Icon, on_click: callable = lambda: None, color: Color = Colors.blue):
        super().__init__()
        self.color = color
        self.background_color = Colors.transparent
        self.icon = icon
        self.on_click = on_click

    def build(self) -> Widget:
        return InkWell(
            child=Container(
                child=self.icon,
                background_color=self.background_color,
                border_radius=20
            ),
            on_hover=self._on_hover,
            on_click=self._on_click
        )

    def layout(self, new: 'Widget' = None):
        self.constraints = (0, 0)
        super().layout(new)

    def _on_click(self):
        self.on_click()
        self.main_state.set_state()

    def _on_hover(self, hover: bool):
        if hover:
            self.background_color = self.color.with_opacity(0.1)
        else:
            self.background_color = Colors.transparent
        self.main_state.set_state()
