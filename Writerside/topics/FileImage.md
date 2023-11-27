# FileImage

Display an image from a file. The format of the file must be in the [supported format list](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html) of the [Pillow library](https://python-pillow.org/).

## Usage

```python
FileImage(
    path = 'path/to/image.png'
)
```

<tip>
    For cleaner project structure, it is recommended to create an assets folder in your project and put all your ressources in it.
    For example, to add an image named "image.png" to your project, it is recommended to have the following structure:
    <code-block lang="bash">
    project/
        assets/
            images/
                image.png
        main.py
    </code-block>
    Then, you can use the image like this:
    <code-block lang="python">
    FileImage(
        path = 'assets/images/image.png'
    )
    </code-block>
</tip>

## Properties

### path

```str``` (required)

The path to the image file.

### size

[```Size```](Size.md) (default: ```Size(0, 0)```)

The size of the image. If the size is ```Size(0, 0)```, the image will be displayed with its original size.

## Constraints

`FileImage` isn't influenced by its parent constraints.
