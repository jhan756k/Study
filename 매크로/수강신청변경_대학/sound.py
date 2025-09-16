from gtts import gTTS

audio = 'speech.mp3'
language = 'kr'

sp = gTTS(
    lang=language,
    text="",
    slow=False
)
sp.save(audio)