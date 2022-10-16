import math
from moviepy.editor import VideoFileClip

def split_video_to_clips(large_video_file_dict):
	spath = list(large_video_file_dict.keys())[0] #extract path from dict

	video_name = spath.split("//")[-1] #extract video name form dict
	video_size = large_video_file_dict[spath] #extract video size in bytes
	video_duration = VideoFileClip(spath).duration #extract video duration in seconds
	
	clip_count = math.ceil(video_size/258435456) #number of subclips the videofiles has to be split into
	no_of_digits = len(str(clip_count)) #number of digits in the clip count(for zfill)
	clip_duration = video_duration/clip_count #The length of each clip to pass into the for loop

	for clip_number in range(clip_count): #creates clips from the video
		current_clip = VideoFileClip(spath).subclip(clip_number*clip_duration,(clip_number+1)*clip_duration) #multiple subclips are created with this
		current_clip_name = video_name[:-4]+"_"+str(clip_number+1).zfill(no_of_digits)+".mp4" #gives each subclip an appropriate title
		current_clip.write_videofile(current_clip_name) #creates the video file