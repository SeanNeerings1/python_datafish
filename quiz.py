import gspread
from google.oauth2 import service_account
import random

def good():
    print("Goed gedaan!")

def bad():
    print("Kan beter.")

vraag = ['Wat is 2+4', 'Wat is 10x3+5', 'Wat is 8x2+3', 'Wat is 2+8x(10x√2)x0', 'Wat is 1+1', 'Wat is 8x9', 'Wat is 90x1200x0+1', 'Wat is 10²', 'Wat is 5²x1', 'Wat is 3x3']
antwoorden = ['6', '35', '19', '0', '2', '72', '1', '100', '25', '9']

print('\n\n\nWelkom bij de gigantische Webdevelopers Quiz 2022')

antwoord = input('Ben je klaar om de Quiz te spelen? (ja/nee): ')
punten = 0
aantal_vragen = 3

if antwoord.lower() == 'ja':
    print('\n\nMooi. Dan gaat de gigantische Webdevelopers Quiz 2022 beginnen!!\nGeef bij iedere vraag als antwoord de voornaam van een student uit de klas op.\n\n')

    player_name = input("Voer je naam in: ")  # Collect the player's name
    
    for _ in range(aantal_vragen):
        i = random.randint(0, len(vraag) - 1)
        a = vraag.pop(i)
        b = antwoorden.pop(i)

        antwoord = input(f"{a}\n")

        if antwoord.lower() == b:
            punten += 1
            print('goed!')
        else:
            print('fout!')

    print('\n\nBedankt voor het spelen van de Quiz, Name: ' + player_name + ', Score: ' + str(punten) + ' van de ' + str(aantal_vragen) + ' vragen juist beantwoord!')
    cijfer = round(float(10 / aantal_vragen * punten), 1)
    print('Je cijfer voor het project komt daarmee op een voorlopige Score: ' + str(cijfer) + '.')

    # Authenticate with Google Sheets
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = service_account.Credentials.from_service_account_file(
        "pythonsheets-365306-4cedad897386.json", scopes=scope
    )
    client = gspread.authorize(creds)

    # Open the Google Sheets document by its title
    spreadsheet = client.open("python_opdracht")

    # Select a worksheet by index (0-based) or title
    worksheet = spreadsheet.get_worksheet(0)

    # Append the data to the worksheet
    data = ["Name: " + player_name, "Score: " + str(cijfer)]  # Include "Name: " and "Score: " labels
    worksheet.append_rows([data]) 
    
    if punten >= 2:
        good()
    else:
        bad()

elif antwoord.lower() == 'nee':
    print('De Quiz gaat niet beginnen, want ik begrijp dat je er nog niet klaar voor bent.\nJammer joh!')
else:
    print('Dit antwoord ken ik niet!')