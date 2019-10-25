import glob
import moviepy.editor as mp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
import moviepy.editor as mp



# for filepath in glob.iglob('*/*.mp4'):
#     print(filepath)

logo_path = ''
movies_names = []

class Main():
    def __init__(self):
        global logo_path
        print('starting')
        logo_path = (os.getcwd() + '/logo.png')

        self.load_movies_names()


    def load_movies_names(self):
        for filepath in glob.iglob('movies/*'):
            movie_folder = filepath + '/'
            movies_names.append(movie_folder)

        self.read_movie_data()

    def read_movie_data(self):
        for name in movies_names :
            if name.split('/')[1].startswith('#'):
                print('Ignored')
            else:
                os.chdir(name)
                for filepath in glob.iglob('*.mp4'):
                    movie = filepath
                    time = 'time.txt'

                    if not time :
                        print('please add a text file with minutes time to cut')
                    else:
                        with open(time) as f:
                            name = 1
                            lines = f.readlines()
                            for line in lines :
                                file_name = str(name) + '.mp4'
                                data = line.split('-')
                                time_start = data[0]
                                all_start_titme = time_start.split(':')
                                if len(all_start_titme) > 2 :
                                    start = (int(all_start_titme[0]) * 60 * 60) + (int(all_start_titme[1])*60) + int(all_start_titme[2])

                                else:
                                    start = (int(all_start_titme[0])*60) + (int(all_start_titme[1]))

                                time_end =  data[1]
                                all_end_time = time_end.split(':')
                                if len(all_end_time) > 2 :
                                    end = (int(all_end_time[0]) * 60 * 60) + (int(all_end_time[1])*60) + int(all_end_time[2])

                                else:
                                    end = (int(all_end_time[0])*60) + (int(all_end_time[1]))

                                self.cut_every_movies(movie , start , end ,file_name)
                                print(movie + '------ >>>>' + file_name)
                                name += 1

                        os.chdir('../..')

    def cut_every_movies(self ,movie , start_time ,  end_time  , targetname):
        video = mp.VideoFileClip(movie)
        print(logo_path)
        logo = (mp.ImageClip(logo_path)
                .set_duration(video.duration)
                .resize(height=75)  # if you need to resize...
                .margin(right=10, top=10, opacity=0)  # (optional) logo-border padding
                .set_pos(("right", "bottom")))

        final = mp.CompositeVideoClip([video, logo])
        final.subclip(start_time, end_time).write_videofile(targetname, audio_codec='aac' )


def main():
    app = Main()

if __name__ == '__main__':
    main()