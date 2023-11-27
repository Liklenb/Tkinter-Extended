# IconButton

A button with an [`Icon`](Icon.md).

## Usage

```python
IconButton(
    on_click = lambda: print("Pressed"),
    icon = Icon(Icons.add),
)
```

## Properties

### icon

[```Icon```](Icon.md) (required)

The icon to display on the button.

### on_click

```callable``` (default: ```lambda: None```)

The function to call when the button is clicked.

### color

[```Color```](Color.md) (default: ```Colors.blue```)

The color of the hover effect.

<tip>
    You can change the color of the icon with the <code><a href="Icon.md" anchor="color">color</a></code> property of the <code><a href="Icon.md">Icon</a></code> widget.
</tip>
