from get_large_video_files import get_large_video_files
from split_video_to_clips import split_video_to_clips

spath = r'YOUR_PATH_HERE'

large_video_files_dict = (get_large_video_files(spath))

# print(type(large_video_files_dict))
for (large_video_file,size) in large_video_files_dict.items():
	split_video_to_clips({large_video_file:size})