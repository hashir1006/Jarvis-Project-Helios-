from pathlib import Path

PROJECT_NAME = "JARVIS_OS"

folders = [
    "core",
    "voice",
    "automation",
    "vision",
    "ui",
    "database",
    "plugins",
    "assets",
    "tests",
    "logs",
    "config",
]

files = {
    "main.py": "",
    "config.py": "",
    "README.md": "# JARVIS OS\n",
    ".gitignore": """__pycache__/
*.pyc
.venv/
.env
logs/
database/*.db
.vscode/
""",
    "requirements.txt": "",
    "core/__init__.py": "",
    "voice/__init__.py": "",
    "automation/__init__.py": "",
    "vision/__init__.py": "",
    "ui/__init__.py": "",
    "plugins/__init__.py": "",
}

root = Path.cwd()

print(f"Creating project in: {root}")

for folder in folders:
    (root / folder).mkdir(parents=True, exist_ok=True)

for file_path, content in files.items():
    file = root / file_path
    file.parent.mkdir(parents=True, exist_ok=True)
    if not file.exists():
        file.write_text(content, encoding="utf-8")

print("\nProject created successfully!")

print("\nFolder structure:")

for path in sorted(root.rglob("*")):
    print(path.relative_to(root))