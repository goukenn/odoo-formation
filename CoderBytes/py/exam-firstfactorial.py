def firstfactorial(num: int) -> int:
    """
    Calcule la factorielle d'un nombre.
    Lève une exception si num > 18.
    """
    if num > 18:
        raise ValueError("bad test case")
    
    result = 1
    while num > 1:
        result *= num
        num -= 1
    
    return result


# Tests
print(firstfactorial(4))   # 24
print(firstfactorial(8))   # 40320