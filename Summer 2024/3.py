def output(path, depth):  # функция составления пути из словаря dirs
    if not isinstance(path, dict):  # когда дошли до последнего каталога - сохраняем текущий путь в ответ
        answer.append("  " * depth + path)
    else:  # в противном случае проходим по вложенным каталогам
        for key in sorted(path):
            answer.append("  " * depth + key)  # добавляем текущий путь в ответ
            output(path[key], depth + 1)  # рекурсивно спускаемся по каталогу


# считываем данные
n = int(input().strip())  # число директорий
dirs = {}  # словарь для хранения директорий
for _ in range(n):
    cur_path = dirs  # текущий путь, ссылка на dirs
    path = input().split('/')  # текущая директория
    for cat in path:  # проходим по каталогам из path
        cur_path = cur_path.setdefault(cat, {})  # добавляем каталог в cur_path, обновляем cur_path с текущим каталогом

answer = []  # массив ответа
output(dirs, 0)  # составляем ответ
# ответ
print(*answer, sep='\n')
