import os
import pathlib

folder = pathlib.Path(input("Enter folder path of videos: "))
name = input("Enter name of video: ")
size = int(input("Enter pixels: "))
os.system(f"cd {folder.parent}")

os.system(f"luasprite {folder}")

source_code = folder / f"output0/{name}.lua"

with open(source_code, "r") as f:
    code = f.read()
    
code = code.replace(f"), Vector2.new({size}, {size}), ", "), ")
code = code.replace(f"setmetatable(new{name}, {name})", "")
code = code.replace(
    f"{name}.__index = {name}\nsetmetatable({name}, Spritesheet)", ""
)
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
with open(f"Videos/{name}.luau", 'w') as f:
    f.write(code)
    
print(code)



