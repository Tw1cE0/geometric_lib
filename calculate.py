import circle
import square

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
    """
    Вычисляет периметр или площадь фигуры.

    Args:
        fig (str): Название фигуры ("circle" или "square").
        func (str): Имя функции ("perimeter" или "area").
        size (list): Список размеров фигуры (1 для круга, 1 для квадрата).

    Returns:
        None
    
    Raises:
        AssertionError: если fig или func некорректны.

    Example:
        >>> calc('circle', 'perimeter', [5])
        perimeter of circle is 31.41592653589793
        >>> calc('square', 'area', [4])
        area of square is 16
    """
    assert fig in figs, f"Invalid figure name: {fig}. Available: {figs}"
    assert func in funcs, f"Invalid function name: {func}. Available: {funcs}"

    result = eval(f'{fig}.{func}(*{size})')
    print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))

    calc(fig, func, size)


