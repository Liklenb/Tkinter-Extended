class Color:
    def __init__(self, rgb: tuple[int, int, int, int]):
        self.rgb = rgb
        self.hexadecimal = self.rgb_to_hex(rgb)

    @staticmethod
    def hex_to_rgb(hexa: str) -> tuple:
        hexa = hexa.lstrip("#")
        return tuple(int(hexa[i:i + 2], 16) for i in (0, 2, 4)) + (255,)

    @staticmethod
    def rgb_to_hex(rgb: tuple):
        return '#%02x%02x%02x' % rgb[0:3]

    @staticmethod
    def from_hexadecimal(hexa: str):
        return Color(rgb=Color.hex_to_rgb(hexa))

    @staticmethod
    def from_rgb(r: int, g: int, b: int, a: int = 255):
        return Color(rgb=(r, g, b, a))

    @staticmethod
    def alpha_blend(background: 'Color', foreground: 'Color') -> 'Color':
        alpha = foreground.rgb[3] / 255
        r = int((1 - alpha) * background.rgb[0] + alpha * foreground.rgb[0])
        g = int((1 - alpha) * background.rgb[1] + alpha * foreground.rgb[1])
        b = int((1 - alpha) * background.rgb[2] + alpha * foreground.rgb[2])
        return Color.from_rgb(r, g, b)

    def with_opacity(self, opacity: float):
        if opacity > 1:
            opacity = 1
        elif opacity < 0:
            opacity = 0
        self.rgb = (self.rgb[0], self.rgb[1], self.rgb[2], int(opacity * 255))
        return self

    def __eq__(self, other):
        return self.rgb == other.rgb


class Colors:
    white: Color = Color(rgb=(255, 255, 255, 255))
    black: Color = Color(rgb=(0, 0, 0, 255))
    transparent: Color = Color(rgb=(0, 0, 0, 0))
    pink: Color = Color(rgb=(233, 30, 99, 255))
    pink_accent: Color = Color(rgb=(245, 0, 87, 255))
    red: Color = Color(rgb=(244, 67, 54, 255))
    red_accent: Color = Color(rgb=(255, 82, 82, 255))
    deep_orange: Color = Color(rgb=(255, 87, 34, 255))
    deep_orange_accent: Color = Color(rgb=(255, 110, 64, 255))
    orange: Color = Color(rgb=(255, 152, 0, 255))
    orange_accent: Color = Color(rgb=(255, 171, 64, 255))
    amber: Color = Color(rgb=(255, 193, 7, 255))
    amber_accent: Color = Color(rgb=(255, 215, 64, 255))
    yellow: Color = Color(rgb=(255, 235, 59, 255))
    yellow_accent: Color = Color(rgb=(255, 255, 0, 255))
    lime: Color = Color(rgb=(205, 220, 57, 255))
    lime_accent: Color = Color(rgb=(238, 255, 65, 255))
    light_green: Color = Color(rgb=(139, 195, 74, 255))
    light_green_accent: Color = Color(rgb=(178, 255, 89, 255))
    green: Color = Color(rgb=(76, 175, 80, 255))
    green_accent: Color = Color(rgb=(105, 240, 174, 255))
    teal: Color = Color(rgb=(0, 150, 136, 255))
    teal_accent: Color = Color(rgb=(100, 255, 218, 255))
    cyan: Color = Color(rgb=(0, 188, 212, 255))
    cyan_accent: Color = Color(rgb=(24, 255, 255, 255))
    light_blue: Color = Color(rgb=(3, 169, 244, 255))
    light_blue_accent: Color = Color(rgb=(64, 196, 225, 255))
    blue: Color = Color(rgb=(33, 150, 243, 255))
    blue_accent: Color = Color(rgb=(68, 138, 225, 255))
    indigo: Color = Color(rgb=(63, 81, 181, 255))
    indigo_accent: Color = Color(rgb=(83, 109, 254, 255))
    purple: Color = Color(rgb=(156, 39, 176, 255))
    purple_accent: Color = Color(rgb=(224, 64, 251, 255))
    deep_purple: Color = Color(rgb=(103, 58, 183, 255))
    deep_purple_accent: Color = Color(rgb=(124, 77, 255, 255))
    blue_grey: Color = Color(rgb=(96, 125, 139, 255))
    brown: Color = Color(rgb=(121, 85, 72, 255))
    grey: Color = Color(rgb=(158, 158, 158, 255))
