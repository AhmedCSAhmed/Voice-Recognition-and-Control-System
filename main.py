# Text to be spoken
import speech_recognition as sr
import playsound # to play saved mp3 file
from gtts import gTTS # google text to speech
import os # to save/open files
import webbrowser # to open browser

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

# sr.Microphone(device_index=3) # Currently setting and reading in from my macbook speakers

recognizer = sr.Recognizer() # Always need to make an instance of the

with sr.Microphone(device_index=0) as audioSource:
    recognizer.adjust_for_ambient_noise(audioSource) # adjusting the audio source to specfically adjust for loud noises
    print("Adjusting for ambient noise. Please wait...")

    promptText = "Adjusting for ambient noise. Please wait..."
    ttsPrompt = gTTS(promptText)
    ttsPrompt.save("promptText.mp3")
    playsound.playsound("promptText.mp3")
    
    
    
    print("speak....\n")
    promptText = "speak..."
    ttsPrompt = gTTS(promptText)
    ttsPrompt.save("promptText.mp3")
    
    
    playsound.playsound("promptText.mp3")
    audio = recognizer.listen(audioSource) # the audio we are listening in for

    
    try:
        audiotext = recognizer.recognize_google(audio)
        promptText = "Google understood you said this.. "
        ttsPrompt = gTTS(promptText)
        ttsPrompt.save("promptText.mp3")
        playsound.playsound("promptText.mp3")
        print("Google understood.. " + audiotext)
        promptText = "You said this "
        ttsPrompt = gTTS(promptText)
        ttsPrompt.save("promptText.mp3")
        playsound.playsound("promptText.mp3")
        
        tts = gTTS(audiotext)
        tts.save("output.mp3")
        playsound.playsound("output.mp3")
        print(audiotext)
        if "take me to" in audiotext:
            word = audiotext.split("take me to", 1)[1].strip()
            url = f"https://www.{word}.com/"
            webbrowser.open_new_tab(url)
            webbrowser.open_new(url)
            
    
                


            
        
        
    except sr.UnknownValueError:
        print("we fully couldn't understand what was being said by you")

        
        