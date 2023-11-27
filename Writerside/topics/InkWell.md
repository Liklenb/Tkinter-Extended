# InkWell

These widget allows you to handle tap and hover events.

## Usage

```python
InkWell(
    on_click = lambda: print("Tapped"),
    on_hover = lambda is_hover: print(is_hover),
    child = Text("Click me"),
)
```

## Properties

### child

```Widget``` (required)

The widget to display inside the `InkWell` and to handle events for.

### on_click

```callable``` (default: ```lambda: None```)

The function to call when the `InkWell` is clicked.

### on_hover

```callable``` (default: ```lambda: None```)

The function to call when the InkWell is hovered.

The function will be called with a single boolean argument, which is True if the `InkWell` is hovered and False otherwise.

## Constraints

`InkWell` gives its child the same constraints it receives from its parent.
