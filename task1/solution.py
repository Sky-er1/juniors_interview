def strict(func):
    def wrapper(*args, **kwargs):
        # Получаем аннотации аргументов функции
        annotations = func.__annotations__

        # Проверяем каждый аргумент на соответствие аннотации
        for arg_name, arg_value in zip(annotations, args):
            expected_type = annotations[arg_name]
            if not isinstance(arg_value, expected_type):
                raise TypeError(
                    f"Аргумент '{arg_name}' должен быть типа {expected_type.__name__}, "
                    f"но получил {type(arg_value).__name__}"
                )

        # Вызываем оригинальную функцию, если все проверки пройдены
        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError
