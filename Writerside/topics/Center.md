# Center

A widget that centers its child within its parent.

## Usage

```python
Center(
    child = Text('Here is a centered widget')
)
```

## Properties

### child

```Widget``` (required)

The widget to center.

## Constraints

### Width

Can be finite or infinite. If infinite, `Center` will take the minimum width possible (child width) and just place it to the left.

### Height

Can be finite or infinite. If infinite, `Center` will take the minimum height possible (child height) and just place it to the top.

### Child constraints

`Center` gives its own constraints to the child.
