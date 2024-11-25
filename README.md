Don't want to pay **1000 Robux** per video? Want to upload more than **3 Videos in 30 days**? 

This repository enables anyone to create **unlimited** amount of videos for **FREE**!

## Setup

1. Make the following hierarchy in **Roblox Studio**:
    1. Make a folder in `Replicated Storage` called `Modules`
    2. In `Modules`, add a **module script** called `Videos`
```
- Replicated Storage
  - Modules    (folder)
    - Videos   (module script)
```

2. Copy [`Videos.luau`](https://github.com/Py-mon/Free-Roblox-Studio-Video/blob/main/Videos.luau) and paste it into the `Videos` module script.
3. Install Python: [Video Tutorial](https://m.youtube.com/watch?v=8cAEH1i_5s0&pp=ygUII2plbm5qaWU%3D) (Get python 3.11)
3. Install **LUASprites** in the command line.
```
pip install LUASprites
```

## Add a Video
1. Get your desired video into a folder with all the frames (make all the size of the frames less than 1024x1024)
2. Run [`spritesheets.py`](https://github.com/Py-mon/Free-Roblox-Studio-Video/blob/main/spritesheet.py) and follow the steps. Run again if you messed up.
3. Import the generated images from `[Your folder of video frames]/output0/[the name you entered]` to your Roblox Studio experience.
4. Take the newly created file and copy it into a **module script** inside `Videos` in Roblox Studio.

## Playing a Video

```lua
local Modules = game:GetService("ReplicatedStorage").Modules
local Video = require(Modules.Video)
local EncounterExclamationPointVideo = require(Modules.Video.EncounterExclamationPoint).new()  -- dont forget .new()

-- Video.play(VideoName, FPS, Surface)
Video.play(EncounterExclamationPointVideo, 36, gui.Main.VideoDisplay)  -- Change gui.Main.VideoDisplay to any surface you want
```
