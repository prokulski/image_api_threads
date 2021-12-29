# Opis

## Instalacja

## Uruchomienie API

Przechodzimy do folderu `api` i z poziomu konsoli startujemy API:

```
uvicorn app:app
```

Sprawdzenie jak działa API można dokonać otwierając w przeglądarce jeden z dwóch adresów:

> <http://127.0.0.1:8000/image/>*num*

gdzie **num** to dowolna liczba całkowita - wynikiem będzie niebieski obrazek z białym tekstem z wartością num.

> <http://127.0.0.1:8000/chart/>*num*

gdzie *num* to dowolna liczba całkowita - wynikiem będzie wykres funkcji kwadratowej $f(x) = x^2$ dla całkowitych $x$ z zakresu $<0; num>$

## Uruchomienie grabbera

Przechodzimy do folderu `grabber` i z poziomu konsoli uruchamiamy odpowiednią wersję grabbera - jedno- lub wielowątkową.

### Wersja jednowątkowa

```
$ python grabber_one_thread.py
```

### Wersja wielowątkowa

```
$ python grabber_multi_threads.py
```
