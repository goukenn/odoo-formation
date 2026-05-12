def meanmode(arr):
    mode = 0
    sum_val = 0
    T = len(arr)
    t = {}
    
    # Parcourir le tableau et compter les occurrences
    for q in arr:
        sum_val += q
        if q not in t:
            t[q] = 0
        t[q] += 1
    
    # Trier par occurrence décroissante
    t = dict(sorted(t.items(), key=lambda x: x[1], reverse=True))
    
    # Calculer la moyenne
    mean = sum_val / T
    
    # Le mode est la clé avec le plus haut compte
    mode = next(iter(t))  # Premier élément du dictionnaire trié
    
    return 'true' if mean == mode else 'false'


# Tests
print(meanmode([1, 2, 3]))          # false
print(meanmode([5, 3, 3, 3, 1]))    # true