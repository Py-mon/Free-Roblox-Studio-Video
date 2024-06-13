-- Example usage of playing a video

local Modules = game:GetService("ReplicatedStorage").Modules -- Change this to the parent of where ever you put the this Video Module
local Video = require(Modules.Video)
local EncounterExclamationPointVideo = require(Modules.Video.EncounterExclamationPoint).new()

Video.play(EncounterExclamationPointVideo, 36, gui.Main.VideoDisplay) -- Change gui.Main.VideoDisplay to any surface you want
