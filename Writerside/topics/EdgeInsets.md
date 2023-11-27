# EdgeInsets

The `EdgeInsets` class allows you to define the padding for the [`Container`](Container.md) widget.

## Usage

```python
Container(
    padding=EdgeInsets(
        top=20,
        bottom=10,
        left=15,
        right=10
    ),
    child=Text("Coucou")
)
```

## Properties

### top

```int``` (default: ```0```)

The top padding.

### bottom

```int``` (default: ```0```)

The bottom padding.

### left

```int``` (default: ```0```)

The left padding.

### right

```int``` (default: ```0```)

The right padding.

## Methods

### EdgeInsets.all

```int``` (required)

Define the same padding for all sides.

### EdgeInsets.horizontal

```int``` (required)

Define the same padding for the left and right sides.

### EdgeInsets.vertical

```int``` (required)

Define the same padding for the top and bottom sides.


## Constraints

If constraints are infinite, the [`Container`](Container.md) will fit the child size. Otherwise, the [`Container`](Container.md) will fit the constraints.
