# Row

A widget that displays its children in a horizontal array.

To cause a child to expand to fill the available horizontal space, wrap the child in an [`Expanded`](Expanded.md) widget.

For a vertical variant, see [Column](column.md).

## Usage

```python
Row(
    children = [
        Text('Here is a first widget'),
        Text('Here is a second widget'),
    ]
)
```

## Properties

### children

```list[Widget]``` (required)

Specifies the widgets to layout in the `Row`.

### main_axis_alignment

[```MainAxisAlignment```](MainAxisAlignment.md) (default: [```MainAxisAlignment.start```](MainAxisAlignment.md#start))

How the children should be placed along the main (horizontal) axis.


### crossAxisAlignment

[```CrossAxisAlignment```](CrossAxisAlignment.md) (default: [```CrossAxisAlignment.center```](CrossAxisAlignment.md#center))

How the children should be placed along the cross (vertical) axis.

## Constraints

### Width

Can be finite or infinite if none of the children is [`Expanded`](Expanded.md). Else, finite is needed.

<warning>
    If one of the children is <code><a href="Expanded.md">Expanded</a></code> and width constraints are infinite, Expanded will return an error: <code>LayoutError: Expanded was given unbounded width</code>.
</warning>

If infinite, `Row` will take the minimum width possible (sum of all children width).

If finite and `Row` width constraints < sum of all children widths, `Row` will overflow (```Warning: Overflow detected!```).

### Height

Can be finite or infinite.

`Row` will always take the maximum height of its children.

### Children constraints

`Row` gives unbounded width to its children and its own height constraints.
To give bounded width to a child, see [`Expanded`](Expanded.md).
