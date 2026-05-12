def letterchange(s: str) -> str:
    """
    Convertit chaque lettre à la suivante dans l'alphabet.
    Si la lettre suivante est une voyelle, elle devient majuscule.
    """
    result = ''
    
    for c in s:
        ch = c
        
        # Vérifier si c'est une lettre
        if c.isalpha():
            if ch == 'z':
                ch = 'a'
            elif ch == 'Z':
                ch = 'A'
            else:
                ch = chr(ord(c) + 1)
            
            # Si la lettre suivante est une voyelle, la rendre majuscule
            if ch in 'aeiou':
                ch = ch.upper()
        
        result += ch
    
    return result


# Tests
print(letterchange("bonjour")) # cpOkpvs
print(letterchange("hello*3")) # Ifmmp*3