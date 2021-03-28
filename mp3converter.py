import os, shutil
from pydub import AudioSegment
class Mp3Converter:
    """ Class to house mp3 Conversion """

    def __init__(self, location):
        """ initialises location and creates folders within the location """
        self.location = location.replace('\\', '/')
        self.mp3_location = self.location + '\\MP3'
        self.wav_location = self.location + '\\WAV'
        os.makedirs(self.mp3_location)
        os.makedirs(self.wav_location)
    
    def move(self, filename):
        shutil.move(filename, self.wav_location)

    def convert(self):
        """ Converts to WAVS to MP3 """
        os.chdir(self.location)
        for folder, subfolder, filenames in os.walk(self.location):
            for filename in filenames:
                try:
                    if filename.endswith('.wav'):
                        mp3_filename = filename.replace('.wav', '.mp3')
                        save_location = self.mp3_location + '\\' + mp3_filename
                        AudioSegment.from_wav(filename).export(save_location, format='mp3')
                        self.move(filename)
                except FileNotFoundError:
                    pass
                else: pass
        print('All done!')
