with open('en-ru.txt', 'r', encoding='utf-8') as infile:
    ru_en_dict = {}
    for line in infile:
        # Убираем пробелы
        line = line.strip()
        if ' - ' in line:
            eng_word, ru_words = line.split(' - ', 1)
            ru_words = ru_words.split(', ')
            for ru_word in ru_words:
                if ru_word not in ru_en_dict:
                    ru_en_dict[ru_word] = []
                ru_en_dict[ru_word].append(eng_word)
    sorted_ru_en_dict = sorted(ru_en_dict.items())
with open('ru-en.txt', 'w', encoding='utf-8') as outfile:
    for ru_word, eng_words in sorted_ru_en_dict:
        eng_words_sorted = sorted(eng_words)
        outfile.write(f"{ru_word} – {', '.join(eng_words_sorted)}\n")
print("Русско-английский словарь записан в ru-en.txt.")
