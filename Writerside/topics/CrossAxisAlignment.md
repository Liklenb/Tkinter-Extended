# CrossAxisAlignment

Defines how the children of a [Row](row.md) or [Column](column.md) or ListView should be placed along the cross axis.

## Usage

```python
Row(
    crossAxisAlignment = CrossAxisAlignment.center,
    children = [
        Text('Here is a first widget'),
        Text('Here is a second widget'),
    ]
)
```

## Properties

### start

Place the children with their start edge aligned with the start side of the cross axis.

### end

Place the children as close to the end of the cross axis as possible.

### center

Place the children so that their centers align with the middle of the cross axis.
