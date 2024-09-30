def report():

    opening = "--Begin report of books/frankenstein.txt--"
    print(opening)

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        count = len(words)
        word_count = f"{count} words found in the document"
        print(word_count)

        print("")

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowered_texts = file_contents.lower()

        filtered = filter(str.isalpha, lowered_texts)
        lowered_text = "".join(filtered)

        character_dictionary = {}
        character_diclis = []
    
        for character in lowered_text:
            if character in character_dictionary:
                character_dictionary[character] += 1
            else:
                character_dictionary[character] = 1
    
        for letter in character_dictionary:
            count = character_dictionary[letter]
            row = {"letter": letter, "count": count}
            character_diclis.append(row)
        
        def sort_on(character_diclis):
            return character_diclis["count"]
        character_diclis.sort(reverse=True, key=sort_on)
        
        for item in character_diclis:
            char = item["letter"]
            coun = item["count"]
            phrase = f"The '{char}' character was found {coun} times"
            print(phrase)

    closing = "--End report--"
    print(closing)

report()