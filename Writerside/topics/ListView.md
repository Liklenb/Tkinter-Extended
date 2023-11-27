# ListView

Scrollable version of a [Column](column.md).

## Usage

```python
ListView(
    children=[Text(str(x), font_size=50) for x in range(100)]
)
```

## Properties

### children

```list[Widget]``` (required)

Specifies the widgets to layout in the `ListView`.

### cross_axis_alignment

[```CrossAxisAlignment```](CrossAxisAlignment.md) (default: [```CrossAxisAlignment.center```](CrossAxisAlignment.md#center))

How the children should be placed along the cross (horizontal) axis.

## Constraints

### Height

Height constraints must be finite.

### Width

Width constraints can be finite or infinite. `ListView` will always take the maximum width of its children.

### Children constraints

`ListView` gives unbounded height to its children and its own width constraints.
