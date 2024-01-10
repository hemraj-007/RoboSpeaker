import pyttsx3  #text to speech

#Code placed under this block will run when you execute the script.
if __name__ == '__main__':
    print("Welcome to Robo speaker")
    while True:
        x = input("Enter what you want to speak")
        if x=='q':
            print("byeeeee")
            break;
    # Initialize the text-to-speech engine
        engine = pyttsx3.init()
    
    # Speak the input text
        engine.say(x)
    
    # Wait for the speech to finish
        engine.runAndWait()