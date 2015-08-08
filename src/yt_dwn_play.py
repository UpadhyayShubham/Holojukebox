import os

with open("video_rename.txt", 'r+') as a:
	with open("youtube_links.txt", 'r') as b:
		i = int(a.readline())
		j = b.readline()
		j = j.rstrip()
		i=i+1
		s1 = "youtube-dl -i "
		s5 = j		
		s9 = " -o"		
		s6 = s1 + s5 + s9
		s2 = str(i)
		s3 = s6 + s2 + ".mp4" 
		os.system(s3) 
		a.seek(0,0)
		a.write(str(i))
		a.close()
		b.close()

	s4 = "mplayer -fs " + s2 + ".mp4"

	os.system(s4)
	
