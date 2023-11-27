# Size

Represents a size with width and height.

## Usage

```python
FileImage(
    path = "assets/images/image.png",
    size = Size(100, 100),
)
```

## Properties

### width

`int` (required)

The width of the size.

### height

`int` (required)

The height of the size.

## Methods

### get

`tuple[int, int]`

Returns the width and height as a tuple.

### is_null

`bool`

Returns whether the height and width are both 0.
