def insertion_sort(a, crescente=True):
    for j in range(1, len(a)):
        chave = a[j]
        i = j - 1

        if crescente:
            while i >= 0 and a[i] > chave:
                a[i + 1] = a[i]
                i -= 1
        else:
            while i >= 0 and a[i] < chave:
                a[i + 1] = a[i]
                i -= 1

        a[i + 1] = chave
        print(f"Interação {j}: {a}")
