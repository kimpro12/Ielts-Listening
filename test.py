import random, string, pygame, sys, os, time, requests, json

def Clear():
    os.system("clear")

def Stop():
    sys.exit()

def PreparingFile(apikey, url, content, Speed, language):
    headers = {"Accept": "audio/wav"}
    params = {
        "text": content,
        "voice": language,
        "rate_percentage": Speed
    }
    auth = ("apikey", apikey)

    response = requests.get(url, headers=headers, params=params, auth=auth)

    if response.status_code == 200:
        with open("test.wav", "wb") as output_file:
            output_file.write(response.content)
        print("Finish!")
    else:
        print("Error with the apikey or url (maybe the host ibm cloud) ?")
        Stop()

def play(length, language, nameorphone, randomaccentornot):
    Clear()
    if randomaccentornot == 1:
        language = RandomAccent()
    if nameorphone == 1:
        s = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    elif nameorphone == 2:
        s = ''.join(random.choice(string.digits) for _ in range(length))
    content = ""
    for char in s:
        content += char + " "
    content = content.rstrip()
    apikey = ""
    url = ""
    with open('apikey.txt', 'r') as file:
        apikey += file.read().rstrip()
    with open('url.txt', 'r') as file:
        url += file.read().rstrip()
    Speed = input("Type the speed you want, Press Enter to set normal mode, or type the percantage you want to increase or decrease (ex: 20 is increasing 20%, -20 is decreasing 20%): ")
    if Speed == "":
        Speed = "0"
    else:
        while True:
            try:
                integer_value = int(Speed)
                break
            except ValueError:
                Speed = input("Please type a number or Press Enter to set normal mode: ")
                if (Speed == ""):
                    Speed = "0"
                    break
    url += "/v1/synthesize"
    PreparingFile(apikey, url, content, Speed, language)
    Check = input("Press Enter to start now, and fill your solution below while listening: ")
    if Check != "":
    	    Stop()
    pygame.mixer.init()
    file = "test.wav"
    sound_a = pygame.mixer.Sound(file)
    sound_a.play()
    while pygame.mixer.get_busy():
        pygame.time.delay(1)
    user_input = input("")
    if user_input != s:
        print("Wrong answer")
        print("The correct answer is: " + s)
    else:
        print("Correct answer")
    while (True):
        Repeat = input("Press Enter to repeat the audio, smt to exit: ")
        if Repeat == "":
                sound_a.play()
                while pygame.mixer.get_busy():
                   pygame.time.delay(1)
        else:
            break    
    pygame.mixer.quit()
    playornot = input("Press Enter to listen again, Type menu to back to menu or type anything to exit: ")
    if playornot == "":
    	play(length, language, nameorphone, randomaccentornot)
    elif playornot == "menu":
        Start()
    else:
        Stop()

def Australia():
    print("1. Jack (Expressive")
    print("2. Heidi (Expressive)")
    num = input("Type 1 or 2 to choose people: ")
    if num == "1":
        return "en-AU_JackExpressive"
    elif num == "2":
        return "en-AU_HeidiExpressive" 
    else:
        Stop()

def British():
    print("1. Kate")
    print("2. Charlotte")
    print("3. James")
    num = input("Type 1 or 2 or 3 to choose people: ")
    if num == "1":
        return "en-GB_KateV3Voice"
    elif num == "2":
        return "en-GB_CharlotteV3Voice"
    elif num == "3":
        return "en-GB_JamesV3Voice"
    else:
        Stop()        

def USA():
    print("1. Allison (Expressive)")
    print("2. Emma (Expressive)")
    print("3. Lisa (Expressive)")
    print("4. Michael (Expressive)")
    print("5. Allison")
    print("6. Emily")
    print("7. Henry")
    print("8. Kevin")
    print("9. Lisa")
    print("10. Michael")
    print("11. Olivia")
    num = input("Type 1 or 2 or... to choose people: ")
    if num == "1":
        return "en-US_AllisonExpressive"
    elif num == "2":
        return "en-US_EmmaExpressive"
    elif num == "3":
        return "en-US_LisaExpressive"
    elif num == "4":
        return "en-US_MichaelExpressive"    
    elif num == "5":
        return "en-US_AllisonV3Voice"
    elif num == "6":
        return "en-US_EmilyV3Voice"
    elif num == "7":
        return "en-US_HenryV3Voice"
    elif num == "8":
        return "en-US_KevinV3Voice"
    elif num == "9":
        return "en-US_LisaV3Voice"
    elif num == "10":
        return "en-US_MichaelV3Voice"
    elif num == "11":
        return "en-US_OliviaV3Voice"
    else:
        Stop()      

def RandomAccent():
    listaccent = ["en-AU_JackExpressive", "en-AU_HeidiExpressive", "en-GB_KateV3Voice", "en-GB_CharlotteV3Voice", "en-GB_JamesV3Voice", "en-US_AllisonExpressive", "en-US_EmmaExpressive", "en-US_LisaExpressive", "en-US_MichaelExpressive", "en-US_AllisonV3Voice", "en-US_EmilyV3Voice", "en-US_HenryV3Voice", "en-US_KevinV3Voice", "en-US_LisaV3Voice", "en-US_MichaelV3Voice", "en-US_OliviaV3Voice"]
    return random.choice(listaccent)

def Choose(s, nameorphone, randomaccentornot):
    Clear()
    n = input("Please type the length of the word/number you want to listen: ")
    if n == "":
        Stop()
    play((int(n)), s, nameorphone, randomaccentornot)

def ChooseNumberOrName(s, randomaccentornot):
    Clear()
    print("1. Number")
    print("2. Name")
    choice = input("Type 1 or 2 to choose listening practice type: ")
    if choice == "1":
        Choose(s, 2, randomaccentornot)
    elif choice == "2":
        Choose(s, 1, randomaccentornot)
    else:
        Stop()

def Start():
    Clear()
    print("1. Australia")
    print("2. British")
    print("3. United States")
    print("4. Random Accent each turn")
    num = input("Type 1 or 2 or 3 or 4 to choose accent: ")
    randomaccentornot = 0
    s = ""
    if num == "1":
        s = Australia()
    elif num == "2":
        s = British()
    elif num == "3":
        s = USA()
    elif num == "4":
        randomaccentornot = 1
    else:
        Stop()
    ChooseNumberOrName(s, randomaccentornot)

if __name__ == "__main__":
    Start()
