# Color

The `Color` class allows you to create a color from a hexadecimal value or from an RGBA value.

## Usage

```python
    # Different ways to create the red color
    Color((255, 0, 0, 255))
    Color.from_rgba(r=255, g=0, b=0, a=255)
    Color.from_hexadecimal("#FF0000")
```

## Properties

### rgba

```tuple[int, int, int, int]``` (required)

The RGBA value of the color.

## Methods

### Color.from_rgba

#### r

```int``` (default: ```0```)

The red value of the color.

#### g

```int``` (default: ```0```)

The green value of the color.

#### b

```int``` (default: ```0```)

The blue value of the color.

#### a

```int``` (default: ```255```)

The alpha value of the color.

### Color.from_hexadecimal

#### hexadecimal

```str``` (required)

The hexadecimal value of the color.

### Color.hex_to_rgba

Returns: ```tuple[int, int, int, int]```

The RGBA value of the color.

#### hexadecimal {id="hexadecimal_1"}

```str``` (required)

The hexadecimal value of the color.

### Color.rgba_to_hex

Returns: ```str```

The hexadecimal value of the color.

#### rgba {id="rgba_1"}

```tuple[int, int, int, int]``` (required)

The RGBA value of the color.

### Color.alpha_blend

Returns: ```Color```

Superimposes the color on the background color.

<tip>
    The <code>foreground</code> color has to have an alpha value lower than 255. If not, the <code>foreground</code> color will be returned
</tip>

#### background

```Color``` (required)

The background color.

#### foreground

```Color``` (required)

The foreground color.

### with_opacity

Returns: ```Color```

Returns the color with the specified opacity.

#### opacity

```int``` (required)

The opacity of the color.

If the opacity is greater than 255, it will be set to 255. If it is lower than 0, it will be set to 0.

### rgba {id="rgba_2"}

```tuple[int, int, int, int]```

The RGBA value of the color.

### hexadecimal {id="hexadecimal_2"}

```str```

The hexadecimal value of the color.
