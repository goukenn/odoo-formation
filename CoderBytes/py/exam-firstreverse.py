def firstreverse(s: str) -> str:
    """
    Inverse une chaîne de caractères.
    """
    h = list(s)
    h = h[::-1]
    return ''.join(h)


# Test
print(firstreverse("hello coderbyte"))