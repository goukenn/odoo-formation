def OverlappingRanges(arr):
    a, b, c, d, x = arr
    
    # Calculer le début et la fin du chevauchement
    overlap_start = max(a, c)
    overlap_end = min(b, d)
    
    # Nombre d'éléments qui se chevauchent
    overlap_count = max(0, overlap_end - overlap_start + 1)
    
    return "true" if overlap_count >= x else "false"