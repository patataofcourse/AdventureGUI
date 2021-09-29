def color(hex):
    if type(hex) == str:
        if len(hex) == 3:
            hex = hex[0] + "0" + hex[1] + "0" + hex[2] + "0"
        hex = int(hex, base=16)
    red = (hex & 0xff0000) // 0x10000
    green = (hex & 0xff00) // 0x100
    blue = hex & 0xff
    return red, green, blue