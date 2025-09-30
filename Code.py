from googletrans import Translator, LANGUAGES
from datetime import datetime

# Initialize the Translator
translator = Translator()

# Display available languages
print("\nAvailable languages:")
for code, lang in LANGUAGES.items():
    print(f"{code}: {lang}")

# Input: Text and Target Language
print("\n--- Welcome to Advanced Language Translator ---")
source_text = input("Enter text to translate: ").strip()
dest_lang = input("Enter target language code (e.g., 'en' for English, 'fr' for French): ").strip()

# Translation Processing
try:
    # Translate the text
    translated = translator.translate(source_text, dest=dest_lang)
    
    # Extract details
    detected_language = LANGUAGES.get(translated.src, "Unknown").capitalize()
    target_language = LANGUAGES.get(dest_lang, "Unknown").capitalize()
    translated_text = translated.text
    character_count = len(source_text)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Display the results
    print("\n--- Translation ---")
    print(f"Original Text: {source_text}")
    print(f"Detected Source Language: {detected_language}")
    print(f"Translated Text ({target_language}): {translated_text}")
    print(f"Character Count: {character_count}")
    print(f"Timestamp: {timestamp}")

    # Save to a log file
    with open("translation_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write("\n--- Translation Log ---\n")
        log_file.write(f"Original Text: {source_text}\n")
        log_file.write(f"Detected Source Language: {detected_language}\n")
        log_file.write(f"Translated Text ({target_language}): {translated_text}\n")
        log_file.write(f"Character Count: {character_count}\n")
        log_file.write(f"Timestamp: {timestamp}\n")
        log_file.write("---\n")

    print("\nTranslation has been logged in 'translation_log.txt'.")

except Exception as e:
    print("Error in translation:", e)
