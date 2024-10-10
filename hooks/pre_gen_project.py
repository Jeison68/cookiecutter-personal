import os
import sys

project_slug = "{{cookiecutter.project_slug}}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[31m"

if project_slug.startswith("x"):
    print(f"{ERROR_COLOR}ERROR:{project_slug=} is not Valid names for this template ")
    sys.exit(1)

print(f"{MESSAGE_COLOR}Let's do it! You're going to create something awesome")
print(f"Creating project at {os.getcwd()}{RESET_ALL}")