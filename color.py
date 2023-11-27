class Color:
    def __init__(self, rgba: tuple[int, int, int, int]):
        self.rgba = rgba
        self.hexadecimal = self.rgba_to_hex(rgba)

    @staticmethod
    def hex_to_rgba(hexa: str) -> tuple:
        hexa = hexa.lstrip("#")
        return tuple(int(hexa[i:i + 2], 16) for i in (0, 2, 4)) + (255,)

    @staticmethod
    def rgba_to_hex(rgba: tuple):
        return '#%02x%02x%02x' % rgba[0:3]

    @staticmethod
    def from_hexadecimal(hexa: str):
        return Color(rgba=Color.hex_to_rgba(hexa))

    @staticmethod
    def from_rgba(r: int, g: int, b: int, a: int = 255):
        return Color(rgba=(r, g, b, a))

    @staticmethod
    def alpha_blend(background: 'Color', foreground: 'Color') -> 'Color':
        alpha = foreground.rgba[3] / 255
        r = int((1 - alpha) * background.rgba[0] + alpha * foreground.rgba[0])
        g = int((1 - alpha) * background.rgba[1] + alpha * foreground.rgba[1])
        b = int((1 - alpha) * background.rgba[2] + alpha * foreground.rgba[2])
        return Color.from_rgba(r, g, b)

    def with_opacity(self, opacity: float):
        if opacity > 1:
            opacity = 1
        elif opacity < 0:
            opacity = 0
        self.rgba = (self.rgba[0], self.rgba[1], self.rgba[2], int(opacity * 255))
        return self

    def __eq__(self, other):
        return self.rgba == other.rgba


class Colors:
    white: Color = Color(rgba=(255, 255, 255, 255))
    black: Color = Color(rgba=(0, 0, 0, 255))
    transparent: Color = Color(rgba=(0, 0, 0, 0))
    pink: Color = Color(rgba=(233, 30, 99, 255))
    pink_accent: Color = Color(rgba=(245, 0, 87, 255))
    red: Color = Color(rgba=(244, 67, 54, 255))
    red_accent: Color = Color(rgba=(255, 82, 82, 255))
    deep_orange: Color = Color(rgba=(255, 87, 34, 255))
    deep_orange_accent: Color = Color(rgba=(255, 110, 64, 255))
    orange: Color = Color(rgba=(255, 152, 0, 255))
    orange_accent: Color = Color(rgba=(255, 171, 64, 255))
    amber: Color = Color(rgba=(255, 193, 7, 255))
    amber_accent: Color = Color(rgba=(255, 215, 64, 255))
    yellow: Color = Color(rgba=(255, 235, 59, 255))
    yellow_accent: Color = Color(rgba=(255, 255, 0, 255))
    lime: Color = Color(rgba=(205, 220, 57, 255))
    lime_accent: Color = Color(rgba=(238, 255, 65, 255))
    light_green: Color = Color(rgba=(139, 195, 74, 255))
    light_green_accent: Color = Color(rgba=(178, 255, 89, 255))
    green: Color = Color(rgba=(76, 175, 80, 255))
    green_accent: Color = Color(rgba=(105, 240, 174, 255))
    teal: Color = Color(rgba=(0, 150, 136, 255))
    teal_accent: Color = Color(rgba=(100, 255, 218, 255))
    cyan: Color = Color(rgba=(0, 188, 212, 255))
    cyan_accent: Color = Color(rgba=(24, 255, 255, 255))
    light_blue: Color = Color(rgba=(3, 169, 244, 255))
    light_blue_accent: Color = Color(rgba=(64, 196, 225, 255))
    blue: Color = Color(rgba=(33, 150, 243, 255))
    blue_accent: Color = Color(rgba=(68, 138, 225, 255))
    indigo: Color = Color(rgba=(63, 81, 181, 255))
    indigo_accent: Color = Color(rgba=(83, 109, 254, 255))
    purple: Color = Color(rgba=(156, 39, 176, 255))
    purple_accent: Color = Color(rgba=(224, 64, 251, 255))
    deep_purple: Color = Color(rgba=(103, 58, 183, 255))
    deep_purple_accent: Color = Color(rgba=(124, 77, 255, 255))
    blue_grey: Color = Color(rgba=(96, 125, 139, 255))
    brown: Color = Color(rgba=(121, 85, 72, 255))
    grey: Color = Color(rgba=(158, 158, 158, 255))
