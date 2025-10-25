import json

with open('gameDataTr.json', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the malformed entry before parsing
content = content.replace('"hint": "Türkiye\'de Boğaziçi\'ni aşarak Avrupa ve Asya\'yı birleştiren büyük bir şehir."\n          },', '{"word": "İstanbul", "hint": "Türkiye\'de Boğaziçi\'ni aşarak Avrupa ve Asya\'yı birleştiren büyük bir şehir."},', 1)

try:
    data = json.loads(content)
    # The rest of the logic to handle duplicate keys will be implemented once the file is parsable.
except json.JSONDecodeError as e:
    print(f"Still an error parsing JSON: {e}")
    # If there are still errors, I might need to do more manual fixing.
    # For now, let's see if the first fix is enough.

# Manual correction of duplicate keys and missing comma
# This is a simplified example of what I'll do programmatically if needed.
# For now, I'll just focus on fixing the immediate error.

# The error is "Expecting ',' delimiter: line 1476 column 20 (char 66615)"
# This points to the transition between the first "easy" and the second "normal" in "Şehirler ve Başkentler"
# Let's find that spot and add a comma.
lines = content.split('\\n')
# This is not a robust way to edit JSON, but for a one-off fix of a known error, it can work.
# A better way would be to load the file, manipulate the data structure, and dump it back.
# But since loading fails, I have to do some string manipulation first.

# The error is likely due to the structure. I will manually reconstruct the problematic parts.
# I'll find the start of the "Şehirler ve Başkentler" category and manually parse it as a string,
# identify the duplicate keys, merge them, and then replace the block in the original content.

# Let's try a simpler fix first. The error is a missing comma.
# I'll locate the end of the first 'easy' block and add a comma.
# This is brittle, but it's the quickest way to try and fix the parse error.
fixed_content = content.replace('''          }
        "normal"''', '''          },
        "normal"''', 1)

# Now let's try to parse it again.
try:
    data = json.loads(fixed_content)
    # If it works, now I can handle the duplicate keys.
    for category in data['gameData']:
        if category['categoryName'] in ["Hayvanlar", "Şehirler ve Başkentler"]:
            levels = category['levels']

            # This is a bit tricky because I can't have duplicate keys in a dict.
            # The file is fundamentally broken from a JSON perspective if it has duplicate keys.
            # The python json library will automatically handle this by taking the last key.
            # I will load and then dump the json to fix this.
            pass

    # The json.loads will handle the duplicate keys by keeping the last one.
    # This is not ideal, as it loses data.
    # The better approach is to fix the source file.

    # I'll manually fix the duplicate keys issue by merging them.
    # I've inspected the file, and the duplicate keys have the same content.
    # So, just removing the duplicates should be fine.

    # Correcting the "Hayvanlar" category
    fixed_content = fixed_content.replace('''        ],
        "easy": [
          {
            "word": "Penguen",
            "hint": "Güney Yarımküre'de, özellikle Antarktika'da yaşayan uçamayan bir kuş."
          },
          {
            "word": "Japon Balığı",
            "hint": "Genellikle bir kasede veya akvaryumda evcil hayvan olarak beslenen küçük, turuncu renkli bir tatlı su balığı."
          },
          {
            "word": "Yunus",
            "hint": "Oyunbaz davranışlarıyla tanınan son derece zeki bir deniz memelisi."
          },
          {
            "word": "Panda",
            "hint": "Güney orta Çin'e özgü, siyah beyaz postu ve bambu diyetiyle bilinen bir ayı."
          },
          {
            "word": "Zebra",
            "hint": "Ayırt edici siyah-beyaz çizgili postları olan bir Afrika atı."
          }''', '')

    # Correcting the "Şehirler ve Başkentler" category
    fixed_content = fixed_content.replace('''        ],
        "easy": [
          {
            "word": "İstanbul",
            "hint": "Türkiye'de Boğaziçi'ni aşarak Avrupa ve Asya'yı birleştiren büyük bir şehir."
          },
          {
            "word": "New York",
            "hint": "Özgürlük Heykeli ve Times Meydanı gibi ikonik simge yapılarıyla bilinen Amerika Birleşik Devletleri'nin en kalabalık şehri."
          },
          {
            "word": "Özgürlük Heykeli",
            "hint": "Amerika Birleşik Devletleri'nde New York şehrinde New York Limanı'ndaki Liberty Adası'nda devasa bir neoklasik heykel."
          },
          {
            "word": "Eyfel Kulesi",
            "hint": "Paris, Fransa'da Champ de Mars'ta bir ferforje kafes kulesi."
          },
          {
            "word": "Kolezyum",
            "hint": "İtalya'nın Roma şehrinin merkezinde, Roma Forumu'nun hemen doğusunda oval bir amfitiyatro."
          }''', '')

    # Also correcting the malformed "normal" entry
    fixed_content = fixed_content.replace('''        "normal": [
            "hint": "Türkiye'de Boğaziçi'ni aşarak Avrupa ve Asya'yı birleştiren büyük bir şehir."
          },''', '''        "normal": [''')


    with open('gameDataTr.json', 'w', encoding='utf-8') as f:
        # I will just write the fixed content and then try to run the update script again.
        # But first, let's load it to make sure it's valid.
        json.loads(fixed_content)
        f.write(fixed_content)

    print("gameDataTr.json has been cleaned.")

except json.JSONDecodeError as e:
    print(f"Failed to clean gameDataTr.json: {e}")
    # If it still fails, I'll need a more robust approach.
