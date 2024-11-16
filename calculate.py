import circle
import square


def calc(figure_type, function_name, *args):
    """Вычисляет периметр или площадь фигуры."""
    if figure_type == "circle":
        if function_name == "perimeter":
            if len(args) == 1:
                return {"perimeter": circle.perimeter(*args)}
            else:
                return {"error": "Неверное количество аргументов"}
        elif function_name == "area":
            if len(args) == 1:
                return {"area": circle.area(*args)}
            else:
                return {"error": "Неверное количество аргументов"}
    elif figure_type == "square":
        if function_name == "perimeter":
            if len(args) == 1:
                return {"perimeter": square.perimeter(*args)}
            else:
                return {"error": "Неверное количество аргументов"}
        elif function_name == "area":
            if len(args) == 1:
                return {"area": square.area(*args)}
            else:
                return {"error": "Неверное количество аргументов"}
    return {"error": "Неверный тип фигуры или имя функции"}
