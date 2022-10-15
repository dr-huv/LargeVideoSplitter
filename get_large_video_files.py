import os



def get_large_video_files(spath):
	large_file_list = []
	for (dirname,dirfolders,dirfiles) in os.walk(spath): #tuple of 3 contains root directory name, list of folders in the directory, list of files in the directory
		for dirfile in dirfiles: #for each file in the file list
			dirfile_size = os.path.getsize(dirname+'\\'+dirfile) #get size of the file
			if(dirfile.endswith(".mp4") and dirfile_size>258435456): #filter out mp4 files larger than ~246 MB
				dirfile_path = (dirname+'\\'+dirfile) #get addresses of those files
				large_file_list.append(dirfile_path) #append the addresses to the list
	return large_file_list

