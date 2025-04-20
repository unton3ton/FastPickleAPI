# https://sky.pro/media/chto-takoe-pickle-i-kak-ego-ispolzovat-v-python/
# https://proglib.io/p/kak-hranit-obekty-python-so-slozhnoy-strukturoy-moduli-pickle-i-dill-2020-04-30


# ✈️Что такое Pickle?
# Pickle — это стандартная библиотека Python, которая позволяет сохранять (сериализовать) 
# и восстанавливать (десериализовать) объекты Python в файлы. 
# Это особенно полезно для долгосрочного хранения данных или передачи их между программами. 
# С помощью pickle можно сохранить сложные структуры данных, такие как списки, словари, классы и даже функции.

# ➡️Пример использования Pickle. Сохранение данных в файл:

import pickle

# Исходные данные
data = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "Data Science", "Machine Learning"]
}

# Сохраняем данные в файл
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

print("Данные успешно сохранены!")


# ➡️Восстановление данных из файла:

# Восстанавливаем данные из файла
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print("Восстановленные данные:")
print(loaded_data)

# ➡️Результат:
# Восстановленные данные:
# {'name': 'Alice', 'age': 30, 'skills': ['Python', 'Data Science', 'Machine Learning']}

# 🔎Почему Pickle полезен?
# - Простота использования: Легко сохранять и восстанавливать сложные структуры данных.

# - Гибкость: Поддерживает практически все типы данных Python.

# - Быстродействие: Pickle работает быстрее, чем другие форматы, такие как JSON.

# ➡️Pickle — это мощный инструмент для сохранения и восстановления данных в Python. Он позволяет легко работать со сложными структурами данных и экономит время на повторной обработке информации.

# 🐍 Pythoner (https://t.me/+pcr2A0ImufcyNDEy)