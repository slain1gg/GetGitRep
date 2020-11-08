def main():
    x, y = 100, 100
    width, height = 200, 200

    draw_house(x, y, width, height)


def draw_house(x, y, width, height):
    """
    Рисует домик на основе ширины width и высоты height
    от опорной точки (x, y), которая находится в середине
    нижней точки фундамента
    :param x: координата середины домика
    :param y: координата низа фундамента
    :param width: полная ширина домика
    :param height: полная высота домика
    :return: None
    """
    print('Рисую дом', x, y, width, height)
    foundation_height = 0.05 * height
    walls_width = 0.9 * width
    walls_height = 0.5 * height
    roof_height = height - walls_height - foundation_height

    draw_house_foundation(x, y, width, foundation_height)
    draw_house_walls(x, y - foundation_height, walls_width, walls_height)
    draw_house_roof(x, y - foundation_height - walls_height, width, roof_height)


def draw_house_foundation(x, y, width, height):
    '''
    Рисует основание домика на основе ширины width и высоты height
    от опорной точки (x, y), которая находится в середине
    нижней точки фундамента
    :param x: координата середины фундамента
    :param y: координата низа фундамента
    :param width: полная ширина фундамента
    :param height: полная высота фундамента
    :return: None
    '''
    print('рисую фундамент...', x, y, width, height)


def draw_house_walls(x, y, width, height):
    '''
    Рисует стены домика на основе ширины width и высоты height
    от опорной точки (x, y), которая находится в середине
    нижней точки стен
    :param x: координата середины стен
    :param y: координата низа стен
    :param width: полная ширина стен
    :param height: полная высота стен
    :return: None
    '''
    print('рисую стены...', x, y, width, height)


def draw_house_roof(x, y, width, height):
    '''
    Рисует крышу домика на основе ширины width и высоты height
    от опорной точки (x, y), которая находится в середине
    нижней точки крыши
    :param x: координата середины крыши
    :param y: координата низа крыши
    :param width: полная ширина крыши
    :param height: полная высота крыши
    :return: None
    '''
    print('рисую крышу...', x, y, width, height)


if __name__ == "__main__":
    main()
