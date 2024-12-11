import genanki

# Unique identifiers for the deck and model
my_deck_id = 2059400110
my_model_id = 1607392319

# Define the card model
my_model = genanki.Model(
    my_model_id,
    'Simple Model',
    fields=[
        {'name': 'Word'},
        {'name': 'Translation'},
        {'name': 'Pronunciation'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Word}}<br><audio controls src="{{Pronunciation}}"></audio>',
            'afmt': '{{FrontSide}}<hr id="answer">{{Translation}}',
        },
    ])

# Create the deck
my_deck = genanki.Deck(
    my_deck_id,
    'English Vocabulary')

# List of words, translations, and audio files
words = [
    {'word': 'apple', 'translation': 'яблоко', 'pronunciation': 'audio/apple.mp3'},
    {'word': 'book', 'translation': 'книга', 'pronunciation': 'audio/book.mp3'},
    {'word': 'computer', 'translation': 'компьютер', 'pronunciation': 'audio/computer.mp3'},
]

# Add cards to the deck
for item in words:
    my_deck.add_note(genanki.Note(
        model=my_model,
        fields=[item['word'], item['translation'], item['pronunciation']]
    ))

# Save the deck to a file
genanki.Package(my_deck).write_to_file('english_vocabulary.apkg')

