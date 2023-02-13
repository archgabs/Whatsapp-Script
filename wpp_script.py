import pywhatkit as wp

class Whatsapp:
    def __init__(self, number, hour=None, minute=None) -> None:
        self._number = number
        self.hour = hour
        self.minute = minute

    @property
    def number(self, n):
        self._number = n

    def sending_msg(self):
        message = input("What message you want to send? => ")
        wp.sendwhatmsg_instantly(f"{self._number}",f"{message}")

    def schedule_msg(self):
        message = input("What message you want to send? => ")
        wp.sendwhatmsg(f"{self._number}",f"{message}", self.hour, self.minute)

    def sending_imgs(self):
        message = input("What message you want to send? => ")
        extention = input("Pay attention! Whats the extention of the image?\nExemple: .png / .gif => ")
        # Change The Location Right Here, REMEMBER TO USE "/" NOT "\"":
        wp.sendwhats_image(self._number, f"C:/Users/jgabr/OneDrive/Documentos/python_scripts/Whatsapp Script/wpp_img/generic.{extention}", f"{message}", 10,True, 3)

if __name__ == "__main__":
    print("""
 __          ___           _                           _____           _       _   
 \ \        / / |         | |                          / ____|         (_)     | |  
  \ \  /\  / /| |__   __ _| |_ ___  __ _ _ __  _ __   | (___   ___ _ __ _ _ __ | |_ 
   \ \/  \/ / | '_ \ / _` | __/ __|/ _` | '_ \| '_ \   \___ \ / __| '__| | '_ \| __|
    \  /\  /  | | | | (_| | |_\__ \ (_| | |_) | |_) |  ____) | (__| |  | | |_) | |_ 
     \/  \/   |_| |_|\__,_|\__|___/\__,_| .__/| .__/  |_____/ \___|_|  |_| .__/ \__|
                                        | |   | |                        | |        
                                        |_|   |_|                        |_|   
                                             
Made by @archgabs, shoutout to Pywhatkit Devs!
    """)
    n = input("Please, insert a number (Example: +5522999999999) => ")
    choice = input("(1) - Send a Message | (2) - Send a Scheduled Message! | (3) - Send a image! \n=> ")

    if choice == "1":
        phone = Whatsapp(f"{n}")
        phone.sending_msg()
    elif choice == "2":
        h = int(input("Please, tell me a hour (0 - 24 Format) => "))
        m = int(input("Please, tell me a minute (0 - 59 Format) => "))
        phone = Whatsapp(f"{n}", h, m)
        phone.schedule_msg()
    else:
        phone = Whatsapp(f"{n}")
        phone.sending_imgs()        