import requests
word = input("Enter a word: ").lower()
url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    meanings = data[0]['meanings']
    print(f"\nDefinitions for '{word}':")
    for meaning in meanings:
        part_of_speech = meaning['partOfSpeech']
        definitions = meaning['definitions']
        print(f"\nPart of Speech: {part_of_speech}")
        for definition in definitions:
            print(f"- {definition['definition']}")
else:
    print("Sorry, word not found or an error occurred.")
