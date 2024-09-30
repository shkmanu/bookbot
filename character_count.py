def character_count():
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowered_texts = file_contents.lower()

        filtered = filter(str.isalpha, lowered_texts)
        lowered_text = "".join(filtered)

        character_dictionary = {}
    
    
        for character in lowered_text:
            if character in character_dictionary:
                character_dictionary[character] += 1
            else:
                character_dictionary[character] = 1
    
        
        print(character_dictionary)
    
            

character_count()