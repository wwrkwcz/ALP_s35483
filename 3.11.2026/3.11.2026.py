import random
import time
import sys

sys.setrecursionlimit(20000)

def quicksort(tablica):
    if len(tablica) <= 1:
        return tablica
    pivot = tablica[len(tablica) // 2]
    lewa = [x for x in tablica if x < pivot]
    srodek = [x for x in tablica if x == pivot]
    prawa = [x for x in tablica if x > pivot]
    return quicksort(lewa) + srodek + quicksort(prawa)

def heapsort(tablica):
    rozmiar = len(tablica)
    for i in range(rozmiar // 2 - 1, -1, -1):
        heapify(tablica, rozmiar, i)
    for i in range(rozmiar - 1, 0, -1):
        tablica[0], tablica[i] = tablica[i], tablica[0]
        heapify(tablica, i, 0)
    return tablica

def heapify(tablica, rozmiar, i):
    najwiekszy = i
    lewy_syn = 2 * i + 1
    prawy_syn = 2 * i + 2
    if lewy_syn < rozmiar and tablica[i] < tablica[lewy_syn]:
        najwiekszy = lewy_syn
    if prawy_syn < rozmiar and tablica[najwiekszy] < tablica[prawy_syn]:
        najwiekszy = prawy_syn
    if najwiekszy != i:
        tablica[i], tablica[najwiekszy] = tablica[najwiekszy], tablica[i]
        heapify(tablica, rozmiar, najwiekszy)

def bubblesort(tablica):
    rozmiar = len(tablica)
    for i in range(rozmiar):
        for j in range(0, rozmiar - i - 1):
            if tablica[j] > tablica[j + 1]:
                tablica[j], tablica[j + 1] = tablica[j + 1], tablica[j]
    return tablica

def insertionsort(tablica):
    for i in range(1, len(tablica)):
        klucz = tablica[i]
        j = i - 1
        while j >= 0 and klucz < tablica[j]:
            tablica[j + 1] = tablica[j]
            j -= 1
        tablica[j + 1] = klucz
    return tablica

def timsort(tablica):
    return sorted(tablica)

def quick_insertion_hybrid(tablica):
    if len(tablica) < 16:
        return insertionsort(tablica)
    pivot = tablica[len(tablica) // 2]
    lewa = [x for x in tablica if x < pivot]
    srodek = [x for x in tablica if x == pivot]
    prawa = [x for x in tablica if x > pivot]
    return quick_insertion_hybrid(lewa) + srodek + quick_insertion_hybrid(prawa)

N = 10000

losowe = [random.randint(1, 100000) for _ in range(N)]

posortowane_9000 = sorted([random.randint(1, 100000) for _ in range(9000)])
losowe_1000 = [random.randint(1, 100000) for _ in range(1000)]
prawie_losowe = posortowane_9000 + losowe_1000

powtorzenia = [random.randint(1, 5) for _ in range(N)]
odwrotne = sorted([random.randint(1, 100000) for _ in range(N)], reverse=True)

print("ALGORYTM QUICKSORT")
kopia = losowe.copy()
start = time.perf_counter()
quicksort(kopia)
stop = time.perf_counter()
print("Dane losowe:", (stop - start) * 1000, "ms")

kopia = prawie_losowe.copy()
start = time.perf_counter()
quicksort(kopia)
stop = time.perf_counter()
print("Dane prawie losowe:", (stop - start) * 1000, "ms")

kopia = powtorzenia.copy()
start = time.perf_counter()
quicksort(kopia)
stop = time.perf_counter()
print("Dane z wieloma powtorzeniami:", (stop - start) * 1000, "ms")

kopia = odwrotne.copy()
start = time.perf_counter()
quicksort(kopia)
stop = time.perf_counter()
print("Dane odwrotnie posortowane:", (stop - start) * 1000, "ms")

print("\nALGORYTM HEAPSORT")
kopia = losowe.copy()
start = time.perf_counter()
heapsort(kopia)
stop = time.perf_counter()
print("Dane losowe:", (stop - start) * 1000, "ms")

kopia = prawie_losowe.copy()
start = time.perf_counter()
heapsort(kopia)
stop = time.perf_counter()
print("Dane prawie losowe:", (stop - start) * 1000, "ms")

kopia = powtorzenia.copy()
start = time.perf_counter()
heapsort(kopia)
stop = time.perf_counter()
print("Dane z wieloma powtorzeniami:", (stop - start) * 1000, "ms")

kopia = odwrotne.copy()
start = time.perf_counter()
heapsort(kopia)
stop = time.perf_counter()
print("Dane odwrotnie posortowane:", (stop - start) * 1000, "ms")

print("\nALGORYTM BUBBLESORT")
kopia = losowe.copy()
start = time.perf_counter()
bubblesort(kopia)
stop = time.perf_counter()
print("Dane losowe:", (stop - start) * 1000, "ms")

kopia = prawie_losowe.copy()
start = time.perf_counter()
bubblesort(kopia)
stop = time.perf_counter()
print("Dane prawie losowe:", (stop - start) * 1000, "ms")

kopia = powtorzenia.copy()
start = time.perf_counter()
bubblesort(kopia)
stop = time.perf_counter()
print("Dane z wieloma powtorzeniami:", (stop - start) * 1000, "ms")

kopia = odwrotne.copy()
start = time.perf_counter()
bubblesort(kopia)
stop = time.perf_counter()
print("Dane odwrotnie posortowane:", (stop - start) * 1000, "ms")

print("\nALGORYTM TIMSORT")
kopia = losowe.copy()
start = time.perf_counter()
timsort(kopia)
stop = time.perf_counter()
print("Dane losowe:", (stop - start) * 1000, "ms")

kopia = prawie_losowe.copy()
start = time.perf_counter()
timsort(kopia)
stop = time.perf_counter()
print("Dane prawie losowe:", (stop - start) * 1000, "ms")

kopia = powtorzenia.copy()
start = time.perf_counter()
timsort(kopia)
stop = time.perf_counter()
print("Dane z wieloma powtorzeniami:", (stop - start) * 1000, "ms")

kopia = odwrotne.copy()
start = time.perf_counter()
timsort(kopia)
stop = time.perf_counter()
print("Dane odwrotnie posortowane:", (stop - start) * 1000, "ms")

print("\nALGORYTM HYBRYDOWY")
kopia = losowe.copy()
start = time.perf_counter()
quick_insertion_hybrid(kopia)
stop = time.perf_counter()
print("Dane losowe:", (stop - start) * 1000, "ms")

kopia = prawie_losowe.copy()
start = time.perf_counter()
quick_insertion_hybrid(kopia)
stop = time.perf_counter()
print("Dane prawie losowe:", (stop - start) * 1000, "ms")

kopia = powtorzenia.copy()
start = time.perf_counter()
quick_insertion_hybrid(kopia)
stop = time.perf_counter()
print("Dane z wieloma powtorzeniami:", (stop - start) * 1000, "ms")

kopia = odwrotne.copy()
start = time.perf_counter()
quick_insertion_hybrid(kopia)
stop = time.perf_counter()
print("Dane odwrotnie posortowane:", (stop - start) * 1000, "ms")
