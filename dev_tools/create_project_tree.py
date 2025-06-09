from pathlib import Path


# Рекурсивно формує дерево на основі словника
def create_project_tree(structure: dict, prefix: str = "") -> str:
    lines = []
    keys = list(structure.keys())
    for index, key in enumerate(keys):
        connector = "└── " if index == len(keys) - 1 else "├── "
        lines.append(f"{prefix}{connector}{key}")
        value = structure[key]
        if isinstance(value, dict) and value:
            extension = "    " if index == len(keys) - 1 else "│   "
            subtree = create_project_tree(value, prefix + extension)
            lines.append(subtree)
    return "\n".join(lines)


project_tree = {
    "root_package/": {
        "pyproject.toml": None,
        "poetry.lock": None,
        "Dockerfile/": None,
        "README.md": None,
        "src/": {
            "bot_assistant/": {
                "main.py": None,
                "models/": None,
                "views/": None,
                "handlers/": None,
                "utils/": None,
                "data/": None,
            },
        },
        "tests/": {None},
        "dev_tools/": {None},
        "logs/": None,
        ".vscode/": None,
        ".dockerignore": None,
        ".gitignore": None,
        "bot_diagram.svg/": None,
    }
}


output_path = Path("project_tree.txt")
tree_text = create_project_tree(project_tree)
output_path.write_text(tree_text, encoding="utf-8")

print("Структура проекту збережена в './project_tree.txt'")


# result:

""" 
└── root_package/
    ├── pyproject.toml
    ├── poetry.lock
    ├── Dockerfile/
    ├── README.md
    ├── src/
    │   └── bot_assistant/
    │       ├── main.py
    │       ├── models/
    │       ├── views/
    │       ├── handlers/
    │       ├── utils/
    │       └── data/
    ├── tests/
    ├── dev_tools/
    ├── logs/
    ├── .vscode/
    ├── .dockerignore
    ├── .gitignore
    └── bot_diagram.svg/
"""
