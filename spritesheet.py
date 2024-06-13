import os
import pathlib


def get_folder():
    return pathlib.Path(input("Enter folder path of videos: "))


def exists(path: pathlib.Path):
    return path.exists() and str(path).replace(" ", "") not in ["", ".", "\\"]


folder = get_folder()
while not exists(folder):
    print("That path doesn't exist. ")
    folder = get_folder()

name = str(input("Enter name of video: "))


def get_size_and_x():
    size = input(
        "\nPixels\nExamples: 256x256 or 100x200\nRecommended Max: 512x512\nAbsolute Max: 1024x1024 (video might lag)\nEnter pixels: "
    )
    remove_spaces = size.replace(" ", "")
    x_index = remove_spaces.find("x")
    return remove_spaces, x_index


size, x_index = get_size_and_x()
while x_index == -1:
    size, x_index = get_size_and_x()

height, width = size[:x_index], size[x_index + 1 :]

os.system(f"cd {folder.parent}")

input(
    f"The program is next going to ask you what to name your video. Name it: '{name}'. Then it will ask you to enter a number. Type in number 1. Press enter to continue... "
)
os.system(f"luasprite {folder}")

source_code = folder / f"output0/{name}.lua"

with open(source_code, "r") as f:
    code = f.read()

code = code.replace(f"), Vector2.new({size}, {size}), ", "), ")
code = code.replace(f"setmetatable(new{name}, {name})", "")
code = code.replace(f"{name}.__index = {name}\nsetmetatable({name}, Spritesheet)", "")
code = code.replace(f"new{name}:AddSprite(", f"Video.addFrame({name}, ")
code = code.replace(
    f"local new{name} = Spritesheet.new()\n",
    f"local {name} = Video.new(Vector2.new({size}, {size}))",
)
code = code.replace(f"return new{name}", f"return {name}")
code = code.replace(
    'local Spritesheet = require(script:FindFirstAncestorWhichIsA("ModuleScript").Spritesheet)',
    "local Video = require(script.Parent.Parent.Video)",
)

print(code)

with open(f"{name}.luau", "w") as f:
    f.write(code)
