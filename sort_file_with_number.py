from pytube import  Playlist
from pathlib import Path
import os 

download_path = str(Path.home()/"Downloads/YoutubeVideos/core_javascript/")
# print('***', Path.home() )

download_path = input("Enter Yout full directory Name Like(/home/username/Downlaods/YoutubeVideos/) : ")
# print('Downlaod Path : ',download_path)
# print() 
playlist_url = 'https://youtube.com/playlist?list=PLbGui_ZYuhiiaQjuOfvgx_-gzVBlCxrk0'

playlist_url = input('Enter youtube  playlist link : ')
p = Playlist(playlist_url)

download_files_name_without_extenstion = [ file_name.split('.')[0] for file_name in os.listdir(download_path)]

# print('files_name_without_extenstion : ', download_files_name_without_extenstion)
# print()

files_name_with_youtube_list = [ video.title for video in p.videos]
# print('file_name with url: ', files_name_with_youtube_list)
# print()

count =  1 

for file_name in files_name_with_youtube_list: 
    print('count for ', count )
    print(file_name ) 
    if file_name in download_files_name_without_extenstion:
    
        try : 
            print('try', count )
            old_file_name = download_path + '/'+ file_name + '.mp4' 
            new_file_name = download_path + '/'+ str(count) + ' '+ file_name  + '.mp4'
    
            os.rename(old_file_name, new_file_name)
        except : 
            print('File is not Downloaded please download file \n File Name : ', file_name ) 
#            print('exception', count )
            
    count += 1            

print('Rename file name with number and file name')



