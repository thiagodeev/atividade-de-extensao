def analyze_text(text):
    words = text.split()
    num_words = len(words)
    num_chars = len(text)
    num_sentences = text.count('.') + text.count('!') + text.count('?')
    
    print(f"Words: {num_words}")
    print(f"Characters: {num_chars}")
    print(f"Sentences: {num_sentences}")

text = input("Enter a text: ")
analyze_text(text)
