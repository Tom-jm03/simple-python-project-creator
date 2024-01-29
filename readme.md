# Python Project Creator

This script helps you to create a new Python project with a specific Python version and a virtual environment on windows.

## Usage
1. Copy the `project_config.py.sample` file to `project_config.py` and edit the values in the file to your liking. The values in the file will be used as default values when creating a new project. You can also edit the values later when creating a new project.
2. Run the script with `python main.py`.
3. You will be asked to enter the name of your new project. Type the name and press Enter.
4. Confirm the name of your project by typing `y` and pressing Enter.
5. The script will then display a list of Python versions found in your PATH. Each version will be displayed with an index, the version number, and the path.
6. Enter the index of the Python version you want to use for your project and press Enter.
7. If the directory for the project already exists, the script will notify you and stop. If not, it will proceed to create the directory structure for your project.
8. The script will ask you if you want to create a `.gitignore` file. If you want to create one, type `y` and press Enter. The script will download a standard Python `.gitignore` file from GitHub.
9. The script will then use the selected Python version to create a virtual environment in your project directory.
10. Finally, the script will ask you if you want to open the created project in VS Code. If you want to open it, type `y` and press Enter.

## Requirements

- Windows
- Python 3.6 or higher
- Access to the internet (for downloading the `.gitignore` file)
- VS Code (if you want to open the project in VS Code)

## Troubleshooting

If you encounter any errors while running the script, the error message will be printed to the console. If you can't resolve the issue, please open an issue on GitHub.