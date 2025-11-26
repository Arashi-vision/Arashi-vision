bad_words = ["fuck", "shit", "bitch"]

def is_clean(text: str):
    for b in bad_words:
        if b in text.lower():
            return False
    return True
