# MainAxisAlignment

Defines how the children of a [Row](row.md) or a [Column](column.md) should be placed along the main axis.

<tip>
    If one or more children are wrapped in a <code><a href="Expanded.md">Expanded</a></code>, remaining space will be 0 so the MainAxisAlignment will have no effect.
</tip>

## Usage

```python
Row(
    main_axis_alignment = MainAxisAlignment.spaceBetween,
    children = [
        Text('Here is a first widget'),
        Text('Here is a second widget'),
    ]
)
```

## Properties

### start

Place the children as close to the start of the main axis as possible.

### end

Place the children as close to the end of the main axis as possible.

### center

Place the children as close to the middle of the main axis as possible.

### spaceBetween

Place the free space evenly between the children.

### spaceAround

Place the free space evenly between the children as well as half of that space before and after the first and last child.

### spaceEvenly

Place the free space evenly between the children as well as before and after the first and last child.
