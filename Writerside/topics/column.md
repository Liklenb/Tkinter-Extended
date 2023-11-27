# Column

A widget that displays its children in a vertical array.

To cause a child to expand to fill the available vertical space, wrap the child in an [`Expanded`](Expanded.md) widget.

The `Column` widget does not scroll. If you want to scroll, consider using a [`ListView`](ListView.md).

For a horizontal variant, see [Row](row.md).

## Usage

```python
Column(
    children = [
        Text('Here is a first widget'),
        Text('Here is a second widget'),
    ]
)
```

## Properties

### children

```list[Widget]``` (required)

Specifies the widgets to layout in the `Column`.

### main_axis_alignment

[```MainAxisAlignment```](MainAxisAlignment.md) (default: [```MainAxisAlignment.start```](MainAxisAlignment.md#start))

How the children should be placed along the main (vertical) axis.


### crossAxisAlignment

[```CrossAxisAlignment```](CrossAxisAlignment.md) (default: [```CrossAxisAlignment.center```](CrossAxisAlignment.md#center))

How the children should be placed along the cross (horizontal) axis.

## Constraints

### Height

Can be finite or infinite if none of the children is [`Expanded`](Expanded.md). Else, finite is needed.

<warning>
    If one of the children is <code><a href="Expanded.md">Expanded</a></code> and height constraints are infinite, Expanded will return an error: <code>LayoutError: Expanded was given unbounded height</code>.
</warning>

If infinite, `Column` will take the minimum height possible (sum of all children heights).

If finite and `Column` height constraints < sum of all children heights, `Column` will overflow (```Warning: Overflow detected!```).

### Width

Can be finite or infinite.

`Column` will always take the maximum width of its children.

### Children constraints

`Column` gives unbounded height to its children and its own width constraints.
To give bounded height to a child, see [`Expanded`](Expanded.md).