# Icon

Display an icon from the [Material Design Icons](https://fonts.google.com/icons) library.

## Usage

```python
Icon(
    icon = Icons.add
)
```

<tip>
    Do not enter the full path of the Icon but use the <code><a href="Icons.md">Icons</a></code> class instead.
    For example, to display the add icon, use <code>Icons.add</code>.
</tip>

## Properties

### icon

```str``` (required)

The icon to display.

### color

[```Color```](Color.md) (default: ```Colors.black```)

The color of the icon.

### size

```int``` (default: ```20```)

The size of the icon.

## Constraints

`Icon` isn't influenced by its parent constraints.
