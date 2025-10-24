from pydub import AudioSegment

file_path = input("Enter your path to the audio file => ")
export_path = input("Enter the path you want to save the file at => ")

sound = AudioSegment.from_mp3(file_path)

start_min = int(input("Enter start minute => "))
start_second = int(input("Enter start second => "))

end_min = int(input("Enter end minute => ")) 
end_second = int(input("Enter end second => "))

start_time = start_min * 60 * 1000 + start_second * 1000
end_time = end_min * 60 * 1000 + end_second * 1000

extract = sound[start_time:end_time]

extract.export(export_path, format="mp3")