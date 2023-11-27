# FilledButton

Use a `FilledButton` for important, final actions like "Save" or "Delete".

## Usage

```python
FilledButton(
    on_click = lambda: print("Pressed"),
    text = Text("Click me"),
)
```

## Properties

### text

[```Text```](Text.md) (required)

The text to display on the button.

### on_click

```callable``` (default: ```lambda: None```)

The function to call when the button is clicked.

### color

[```Color```](Color.md) (default: ```Colors.blue```)

The color of the button.

## Constraints

`FilledButton` isn't influenced by its parent constraints.
