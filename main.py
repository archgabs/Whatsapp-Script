import speech_recognition as sr
import pywhatkit as wp

# Notes before using it: INSTALL PYWHATKIT (pip install pywhatkit) and install speech_recognition aswell!


class Whatsapp:
    def __init__(self, number) -> None:
        self._number = number

    # This is a func to send instantly a message to a certain phone number.

    def send_message_instanlty(self):
        try:
            wp.sendwhatmsg_instantly(
                self._number, input("Whats the message? "))
        except ValueError as e:
            print("Something went wrong: ", str(e))

    # This is a func to send schedule messages to a certain phone number.

    def send_message_schedule(self, hour, minute):
        try:
            wp.sendwhatmsg(self._number, input(
                "Whats the message? "), hour, minute)
        except ValueError as e:
            print("Something went wrong: ", str(e))

    # This is a func to send images with (or no) captions to a certain phone number.

    def send_image(self, url):
        try:
            wp.sendwhats_image(self._number, url, input("Whats the message? "))
        except ValueError as e:
            print("Something went wrong: ", str(e))


def selecting_with_voice():
    exit_program = False
    recognizer = sr.Recognizer()

    while exit_program == False:
        menu()
    # Recognizing the voice

        with sr.Microphone() as mic_source:
            try:
                audio = recognizer.listen(mic_source)
                audio_txt = recognizer.recognize_google(
                    audio, language="pt-BR")
                audio_txt = audio_txt.title()

            except ValueError as e:
                print("Noticed Error: ", str(e))

        # Creating Important Variables

        number = input("Number => ")
        phone = Whatsapp(number)

        # Selecting the right choice with voice.

        if audio_txt == "Enviar Mensagem":
            phone.send_message_instanlty()

        elif audio_txt == "Agendar Mensagem":
            hour = int(input("Hour => "))
            minute = int(input("Minute => "))
            phone.send_message_schedule(hour, minute)

        elif audio_txt == "Enviar Imagem":
            url = input("Path => ")
            phone.send_image(url)
        else:
            print("Sorry, didn't heard you.")

        user_choice = input("==> Want to Continue? Y/N ")
        user_choice = user_choice.upper()

        if user_choice == "Y":
            exit_program == False
        else:
            exit_program == True


def menu():
    print("""

888       888 888               888                                                          888     888          d8b                  
888   o   888 888               888                                                          888     888          Y8P                  
888  d8b  888 888               888                                                          888     888                               
888 d888b 888 88888b.   8888b.  888888 .d8888b   8888b.  88888b.  88888b.         888        Y88b   d88P  .d88b.  888  .d8888b .d88b.  
888d88888b888 888 "88b     "88b 888    88K          "88b 888 "88b 888 "88b      8888888       Y88b d88P  d88""88b 888 d88P"   d8P  Y8b 
88888P Y88888 888  888 .d888888 888    "Y8888b. .d888888 888  888 888  888        888          Y88o88P   888  888 888 888     88888888 
8888P   Y8888 888  888 888  888 Y88b.       X88 888  888 888 d88P 888 d88P                      Y888P    Y88..88P 888 Y88b.   Y8b.     
888P     Y888 888  888 "Y888888  "Y888  88888P' "Y888888 88888P"  88888P"                        Y8P      "Y88P"  888  "Y8888P "Y8888  
                                                         888      888                                                                  
                                                         888      888                                                                  
                                                         888      888                                                                  

Enviar Mensagem - Agendar Mensagem - Enviar Imagem
Fale agora!
 """)


if __name__ == "__main__":
    selecting_with_voice()
