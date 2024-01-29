import subprocess
import os
import re
import requests
import traceback as tb
from project_config import project_path, vscode_path, git_ignore_url

while True:
    project_name = input("Enter project name: ")
    correct = input("Is this correct? (y/n): ")
    if correct != "y":
        continue
    python_paths = []
    path_variable = os.getenv("PATH")
    if path_variable is None:
        print("PATH variable not found")
        break
    paths = path_variable.split(';')
    python_path_regex = re.compile(r"\\python\\python(\d+)\\$", re.IGNORECASE)
    for i, path in enumerate(paths):
        match = python_path_regex.search(path)
        if match is not None:
            try:
                version_number = match.group(1)
                version_number_int = version_number[0] + '.' + version_number[1:]
            except Exception as e:
                print(tb.format_exc())
                version_number = ""
            else:
                full_path = {"path": path, "version": version_number_int, "version_string": version_number}
                if full_path not in python_paths:
                    python_paths.append(full_path)
    if len(python_paths) == 0:
        print("No python paths found. Please add python to your PATH variable.")
        exit()
    else:
        while True:
            try:
                print("Found the following python paths:")
                python_paths = sorted(python_paths, key=lambda x: tuple(map(int, x['version'].split('.'))), reverse=True) # Sort by version number
                for i, path in enumerate(python_paths):
                    print(f"{str(i)}: {path['version']} ({path['path']})")
                python_path_index = int(input("Enter the index of the python Version you want to use: "))
                if python_path_index < 0 or python_path_index >= len(python_paths):
                    print("Invalid index")
                    break
                else:
                    if os.path.exists(f"{project_path}{project_name}"):
                        print("Directory already exists")
                        break
                    else:
                        print("Creating directory structure...")
                        try:
                            subprocess.run(["mkdir", f"{project_path}{project_name}"])
                            subprocess.run(["touch", f"{project_path}{project_name}\\main.py"])
                            gitignore_decision = input("Do you want to create a .gitignore file? (y/n): ")
                            if gitignore_decision == "y":
                                with open(f"{project_path}{project_name}\\.gitignore", "w") as f:
                                    request = requests.get(git_ignore_url)
                                    if request.status_code == 200:
                                        f.write(request.text)
                        except Exception as e:
                            print(tb.format_exc())
                            print("Error creating directory structure")
                            exit()
                        else:
                            try:
                                print(f"Using python version {python_paths[python_path_index]['version']} to create a virtual environment for '{project_name}' in '{project_path}'.")
                                subprocess_args = [f"{python_paths[python_path_index]['path']}\\Python{python_paths[python_path_index]['version_string']}.exe", "-m", "venv", f"{project_path}\\{project_name}\\env"]
                                subprocess.run(subprocess_args)
                            except Exception as e:
                                print(tb.format_exc())
                                print("Error creating virtual environment")
                                exit()
                            else:
                                print("Done")
                                code = input("Do you want to open the created project in VS Code? (y/n): ")
                                if code == "y":
                                    try:
                                        subprocess.run([vscode_path, f"{project_path}{project_name}"])
                                    except Exception as e:
                                        print(tb.format_exc())
                                        print("Error opening project in VS Code...")
                                        exit()
                                    else:
                                        exit()
                                else:
                                    exit()
            except ValueError:
                print("Invalid index")
                continue
            except KeyboardInterrupt:
                exit()
    if correct == "y":
        break
    else:
        continue