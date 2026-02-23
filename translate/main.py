from translate import Translator

translator = Translator(to_lang="fr")

# Read the text in source language
with open("translate/english.txt", "r") as source_file:
    english_lines = source_file.readlines()
    source_file.close()

# Translate
french_lines = []
for line in english_lines:
    translation = translator.translate(line)
    french_lines.append(translation)
    french_lines.append("\n")

# Save the translated text
with open("translate/french.txt", "w") as dest_file:
    dest_file.writelines(french_lines)
    dest_file.close()

