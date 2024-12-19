import genanki

# Unique identifiers for the deck and model
my_deck_id = 2059400110
my_model_id = 1607392319

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
            'qfmt': '{{Word}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Translation}}<br><audio autoplay><source src="{{Pronunciation}}"></audio>',
        },
    ])

my_deck = genanki.Deck(
    my_deck_id,
    'English Vocabulary')

file_path = 'list.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    for item in file:
        my_deck.add_note(genanki.Note(
            model=my_model,
            fields=[item['word'], item['translation'], item['pronunciation']]
        ))

# Save the deck to a file
genanki.Package(my_deck).write_to_file('english_vocabulary.apkg')

