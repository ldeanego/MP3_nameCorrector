# -*- coding: UTF-8 -*-
#coding: utf8
__author__="Li Ding"

import os
import eyed3

#Get the absolute folder containing the mp3 files
mp3_dir=os.getcwd()+u'/workspace/'


for f in os.listdir(mp3_dir):
	
	#Current file name	
	f = f.encode("utf-8") 
	print f

	#Only process MP3 files
	(root, ext) = os.path.splitext(f)
	if ext==".mp3":
		audioFile = eyed3.load(mp3_dir+f.decode("utf-8"))

		#The artist of the song		
		print audioFile.tag.artist.encode("utf-8") 
		#The title of the song
		print audioFile.tag.title.encode("utf-8")

		#Rename		
		os.rename(mp3_dir+f.decode("utf-8"),mp3_dir+audioFile.tag.artist+" - "+audioFile.tag.title+".mp3")
		print "\n"
	




