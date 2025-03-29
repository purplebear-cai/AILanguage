GEN_CONVERSATION_PROMPT = """
Generate a 5-turn Japanese conversation for a [scenario] scenario. Include Japanese (Kanji/Hiragana/Katakana), Romaji, and English translations.
Generate a list of vocabularies (key new words). For each new word, include Kanji, Romaji, English, and a list of sentence examples for each new word.
Generate a list of key grammars. Explain the grammar, and list out a few sentence examples.
The output is a nested JSON format.
Example output:
{
"conversation": [{"kanji": str, "romaji": str, "english": str}],
"vocabulary": [{"kanji": str, "romaji": str, "english": str, "examples": list[str]}],
"grammar": [{"grammar": str, "examples": list[str]}]
}
"""