Don't want to pay **1000 Robux** per video? Want to upload more than **3 Videos in 30 days**? 

This repository enables anyone to create **unlimited** amount of videos for **FREE**!

## Usage

1. Make the following hierarchy in **Roblox Studio**:
    1. Make a folder in `Replicated Storage` called `Modules`
    2. In `Modules`, add a **module script** called `Videos`
```
- Replicated Storage
  - Modules    (folder)
    - Videos   (module script)
```

2. Copy [`Videos.luau`](https://github.com/Py-mon/Free-Roblox-Studio-Video/blob/main/Videos.luau) and paste it into the `Videos` module script.
3. Get your desired video into a folder with all the frames (make all the frames 128x128, 256x256, 512x512, or 1024x1024)
4. Install **LUASprites**
```
pip install LUASprites
```
6. Run [`spritesheets.py`](https://github.com/Py-mon/Free-Roblox-Studio-Video/blob/main/spritesheet.py) and follow the steps. Run again if you messed up.
8. Import the images in `[your entered folder]/output0/[the name you entered]` to your Roblox Studio experience.
9. Take the newly created file and copy it into a **module script** inside `Videos` in Roblox Studio.

## Playing A Video

```lua
local Modules = game:GetService("ReplicatedStorage").Modules
local Video = require(Modules.Video)
local EncounterExclamationPointVideo = require(Modules.Video.EncounterExclamationPoint).new()  -- dont forget .new()

-- Video.play(VideoName, FPS, Surface)
Video.play(EncounterExclamationPointVideo, 36, gui.Main.VideoDisplay)  -- Change gui.Main.VideoDisplay to any surface you want
```
