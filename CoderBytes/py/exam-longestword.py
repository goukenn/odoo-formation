def longestword(s: str) -> str:
    """
    Trouve le mot le plus long contenant uniquement
    des lettres et des chiffres.
    """
    max_length = 0
    longest = ''
    
    for word in s.split(" "):
        # Vérifier si le mot contient seulement des lettres et chiffres
        if word.isalnum():
            word_length = len(word)
            if word_length > max_length:
                max_length = word_length
                longest = word
    
    return longest


# Tests
print(longestword("fun!!& time"))      # time
print(longestword("I love dogs"))      # love