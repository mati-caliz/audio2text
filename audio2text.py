import assemblyai as aai

aai.settings.api_key = "ffbcd19f906b4c688060d677d7ff18e9"

FILE_URL = "C:\\Users\\matia\\OneDrive\\Desktop\\AudioToText\\audio4.mp3"

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)

if transcript.status == aai.TranscriptStatus.error:
    print(transcript.error)
else:
    print(transcript.text)
