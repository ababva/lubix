import argparse
import json
import os
import subprocess
import requests


def fetch_dependencies(package_name, version="latest", depth=0, max_depth=1, registry_url="https://registry.npmjs.org"):
    """
    Рекурсивно извлекает зависимости для указанного пакета.
    """
    if depth > max_depth:
        return {}

    url = f"{registry_url}/{package_name}"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch package: {package_name}")

    package_data = response.json()
    dependencies = {}
    for versions in package_data["versions"].values():
        if "dependencies" in versions:
            dependencies.update(versions["dependencies"])
    result = {}
    for dep_name, dep_version in dependencies.items():
        result[dep_name] = fetch_dependencies(dep_name, version="latest", depth=depth + 1, max_depth=max_depth, registry_url=registry_url)

    return result


def build_dot_graph(package_name, dependencies, parent=None):
    """
    Построение графа в формате DOT.
    """
    graph = ""
    if parent:
        graph += f'"{parent}" -> "{package_name}";\n'

    for dep, sub_deps in dependencies.items():
        graph += build_dot_graph(dep, sub_deps, package_name)

    return graph


def generate_graph(dot_file_path, output_path, graphviz_path):
    """
    Генерация PNG-файла из DOT-файла с помощью Graphviz.
    """
    command = [graphviz_path, "-Tpng", dot_file_path, "-o", output_path]
    subprocess.run(command, check=True, shell=True)


def main():
    parser = argparse.ArgumentParser(description="Визуализация графа зависимостей npm-пакетов.")
    parser.add_argument("--graphviz", default="C:\\Program Files\\Graphviz\\bin\\dot.exe", help="Путь к утилите Graphviz (например, C:\\Program Files\\Graphviz\\bin\\dot.exe).")
    parser.add_argument("--package", default="@tanstack/react-query", help="Имя анализируемого npm-пакета.")
    parser.add_argument("--output", default="C:\\Users\\anike\\PycharmProjects\\parasha3\\a.png", help="Путь к файлу для сохранения графа (формат PNG).")
    parser.add_argument("--depth", default="1", type=int, help="Максимальная глубина анализа зависимостей.")
    parser.add_argument("--registry", default="https://registry.npmjs.org", help="URL-адрес репозитория (по умолчанию: https://registry.npmjs.org).")
    args = parser.parse_args()

    dot_file_path = "dependencies.dot"

    try:
        print(f"Fetching dependencies for {args.package}...")
        dependencies = fetch_dependencies(args.package, version="latest", max_depth=args.depth, registry_url=args.registry)
        print("Building DOT graph...")
        dot_graph = f"digraph dependencies {{\n{build_dot_graph(args.package, dependencies)}}}\n"

        with open(dot_file_path, "w") as f:
            f.write(dot_graph)

        print("Generating PNG...")
        generate_graph(dot_file_path, args.output, args.graphviz)
        print(f"Dependency graph saved to {args.output}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if os.path.exists(dot_file_path):
            os.remove(dot_file_path)


if __name__ == "__main__":
    main()
