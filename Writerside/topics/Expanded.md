# Expanded

The `Expanded` widget is used to expand a child of a [`Row`](row.md) or a [`Column`](column.md), so that the child fills the available space along the main axis (e.g., horizontally for a `Row` or vertically for a `Column`).

If multiple children are `Expanded`, the available space is divided among them according to the [`flex`](#flex) factor.

As [`Column`](column.md) gives the children infinite height constraints, if a child needs a finite height constraint like a ListView, consider wrapping the child in an `Expanded` widget so the [`Column`](column.md) gives the child the height constraints it needs.

## Usage

```python
Column(
    children=[
        Expanded(
            flex=1,
            child=Container(
                background_color=Colors.red,
                child=Text("This container takes 1/6 of the available space"),
            ),
        ),
        Expanded(
            flex=2,
            child=Container(
                background_color=Colors.green,
                child=Text("This container takes 2/6 of the available space"),
            ),
        ),
        Expanded(
            flex=3,
            child=Container(
                background_color=Colors.blue,
                child=Text("This container takes 3/6 of the available space"),
            ),
        ),
    ],
)
```

## Properties

### child

```Widget``` (required)

The child contained by the `Expanded` widget.

### flex

```int```  (default: ```1```)

The flex factor to use for this child.

## Constraints

The `Expanded` widget don't have the same behavior depending on the parent widget.

In a [`Row`](row.md), the `Expanded` widget gives the child a finite width constraint (the maximum width of the [`Row`](row.md)) and an infinite height constraint.

In a [`Column`](column.md), the `Expanded` widget gives the child an infinite width constraint and a finite height constraint (the maximum height of the [`Column`](column.md)).
