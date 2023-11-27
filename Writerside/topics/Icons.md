# Icons

List of all the icons available in the [Material Design Icons](https://fonts.google.com/icons) library.

The names are mostly the same as the ones in the library.
Names are snake cased (all lower case with space replaced by underscores).

## Structure

```
(icon_)name_style
```

If the name of the icon starts with a number, "icon_" is placed before the name of the icon.

"class" icon name is replaced by "icon_class".

### Some examples

```
add -> Icons.add
123 -> Icons.icon_123
search with rounded style -> Icons.search_rounded
class -> Icons.icon_class
```


## Styles

The name is followed by the style of the icon.

If no style is specified, the icon is filled.

### outlined

Only the outline of the icon is colored.

### rounded

All the corners of the icon are rounded.

### two_tone

The icon is composed of two colors.

<warning>
    You need to specify a color with an opacity inferior to 1 for this style to work.
</warning>

### sharp

The icon is composed of sharp edges.

## Specifications

<tip>
    You don't need to read and understand this section to use the icons. It's only here for the curious ones or the ones who want to contribute/modify the icons.
</tip>

<warning>
    You should not use/modify things referenced in this section unless you know what you are doing.
</warning>

### Size

The maximal size of the icons is 1000x1000 pixels. You can go further but the quality of the icon will be reduced.

### Location

The icons are located in the ```assets/icons/material-design-icons-4.0.0``` folder.

### Format

The original format of the icons is SVG, but it's not supported by the ```PIL``` library. Therefore, the icons are converted to PNG format.

### List

List of available icons is available [here](https://fonts.google.com/icons).

Currently, downloaded library version is 4.0.0

You can consult icon.py to see the list of all the icons available in the library.
