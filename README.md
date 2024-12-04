# Программа main.py
## fetch_dependencies: рекурсивно извлекает зависимости указанного npm-пакета, ограничивая глубину анализа.
![image](https://github.com/user-attachments/assets/46e3fa57-7e5d-4a0c-9fbd-09bce5e47faa)

## build_dot_graph: создает текстовое описание графа зависимостей в формате DOT для визуализации.
![image](https://github.com/user-attachments/assets/0df7106a-bfe2-426d-82e5-e98b373a629b)

## generate_graph: генерирует PNG-файл с графом зависимостей из DOT-файла с использованием Graphviz.
![image](https://github.com/user-attachments/assets/e886edb5-cfec-4e67-97df-82a9bc5f86fc)

## main: управляет процессом извлечения зависимостей, построения графа и его визуализации на основе входных параметров.
![image](https://github.com/user-attachments/assets/45b14128-8e79-4b97-b51b-7660eb8b312e)

# Тесты tests.py
tests.py
![image](https://github.com/user-attachments/assets/57181008-561e-498e-bcdb-43219c982ddc)

Тесты проверяют корректность работы функций, используемых в визуализаторе зависимостей. test_fetch_dependencies проверяет, что функция fetch_dependencies возвращает словарь с зависимостями и включает ожидаемые пакеты, а test_build_dot_graph проверяет, что функция build_dot_graph корректно создает описание графа в формате DOT, включая связи между узлами
![image](https://github.com/user-attachments/assets/2eb79c82-16a3-4264-9b57-508cb3a6b5a9)
Все тесты выполнены успешно
# Gitclone
```git clone https://github.com/ababva/lubix```

# Файл a.png
![image](https://github.com/user-attachments/assets/88d62e2d-acd2-44c3-b9ba-f4e15f984b67)
*При приближении изображение становится нормальным

# Запуск
## python .\main.py --package <пакет> --output <Путь к .png файлу> --depth <глубина>
### <пакет> - Указание репозитория, откуда парсится
### <Путь к .png файлу> - Путь к файлу, где будет генерироваться граф

