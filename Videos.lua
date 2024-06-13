local Video = {}


function Video.new(size)
	local video = {}

	video.frames = {}	
	video.size = size
	
	return video
end

function Video.addFrame(video, index, position, sheet)
	local numberIndex = #index - string.reverse(index):find('_')
	local frameNumber = tonumber(string.sub(index, numberIndex + 2, #index))
	
	local frame = {position=position, sheet=sheet}
	video.frames[frameNumber] = frame
end

function Video.play(video, fps, surface)
	local frames = #video.frames
	local waitPerFrame = 1 / fps
	
	surface.BackgroundTransparency = 1
	surface.ImageRectSize = video.size
	
	task.spawn(function()
		for i=1,frames do
			local frame = video.frames[i]
			if frame.sheet ~= surface.Image then
				surface.Image = frame.sheet
			end
			surface.ImageRectOffset = frame.position

			task.wait(waitPerFrame)
		end
	end)
end


return Video
