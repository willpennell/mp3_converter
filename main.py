#! python3
# Main.py for mp3 conversion
from mp3converter import Mp3Converter
location = input('Enter the folder containg WAVs to convert: ')
new_convert = Mp3Converter(location)
new_convert.convert()





