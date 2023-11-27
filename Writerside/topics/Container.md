# Container

The `Container` widget allows you to draw a surface and let a padding between the parent and its child.

## Usage

```python
Container(
    padding=EdgeInsets.all(20),
    border_radius=20,
    background_color=Colors.red,
    child=Text("""Ipsum ut recusandae doloremque eius qui ea aut. Illum voluptas aut similique impedit iste. Occaecati incidunt similique accusamus vero laudantium.

Et sit asperiores dignissimos rerum a. Illo porro voluptas nesciunt. Dolores fuga tempore itaque dolorem qui distinctio. Recusandae deleniti et ipsam dolorem quis quod in. Alias reiciendis alias provident expedita. Ut blanditiis eos corporis suscipit autem in at.

Ut porro et molestias numquam quis incidunt facilis. Dolor ipsum illum minus facere. Eius incidunt dolor atque tenetur. Ea voluptas id rerum.

Quia veniam doloribus cum architecto sint beatae qui sunt. Ea itaque repudiandae illo. Omnis et tempora repellat modi debitis ut vitae qui. Quia enim repellat quia consequuntur vitae. Aliquid consequatur tempore laudantium et eos.

Mollitia quis molestiae ea non voluptate. Fugit similique rem sequi possimus veritatis accusamus repudiandae ipsa. Qui sed quis velit sapiente. Et omnis sit laboriosam excepturi quia voluptates fugiat eum. Alias amet quo reiciendis non nisi esse autem molestiae."""),
)
```

## Properties

### child

```Widget``` (required)

The child contained by the `Container` widget.

### background_color

[```Color```](Color.md) (default: ```Colors.transparent```)

The background color of the container.

### padding

[```EdgeInsets```](EdgeInsets.md) (default: ```EdgeInsets.all(0)```)

The padding between the parent and the child.

### border_radius

```int``` (default: ```0```)

The border radius of the container.

### border_width

```int``` (default: ```0```)

The border width of the container.

### border_color

[```Color```](Color.md) (default: ```Colors.transparent```)
