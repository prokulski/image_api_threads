# Opis

Repozytorium zawiera przykład prostego API i jego użycia. Celem jest pokazanie jak zmienia się prędkość działania *grabberów* jeśli zastosujemy wielowątkowe odpytywanie API.

## Instalacja

Tworzymy środowisko wirtualne, instalujemy pakiety i aktywujemy to środowisko:

```bash
$ virtualenv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt 
```

## Uruchomienie API

Przechodzimy do folderu `api` i z poziomu konsoli startujemy API:

```bash
$ uvicorn app:app
```

Sprawdzenie jak działa API można dokonać otwierając w przeglądarce jeden z dwóch adresów:

> <http://127.0.0.1:8000/image/>*num*

gdzie **num** to dowolna liczba całkowita - wynikiem będzie niebieski obrazek z białym tekstem z wartością num.

> <http://127.0.0.1:8000/chart/>*num*

gdzie *num* to dowolna liczba całkowita - wynikiem będzie wykres funkcji kwadratowej $ f(x) = x^2 $ dla całkowitych $ x $ z zakresu $ <0; num> $

## Uruchomienie grabbera

Przechodzimy do folderu `grabber` i z poziomu konsoli uruchamiamy odpowiednią wersję grabbera - jedno- lub wielowątkową albo wieloprocesową.

### Wersja jednowątkowa

```bash
$ python grabber_one_thread.py
```
Na testowej maszynie osiągi (na 1000 iteracjach) był następujące:

```
Pobranie obrazków: 4.403s, średnio 227.097/s
Pobranie wykresów: 189.566s, średnio 5.275/s
```

### Wersja wielowątkowa

```bash
$ python grabber_multi_threads.py
```

Na testowej maszynie osiągi (na 1000 iteracjach) był następujące:

```
Pobranie obrazków: 3.045s, średnio 328.452/s
Pobranie wykresów: 175.807s, średnio 5.688/s
```

### Wersja wieloprocesowa

```bash
$ python grabber_multi_processes.py
```

Na testowej maszynie osiągi (na 1000 iteracjach) był następujące:

```
Pobranie obrazków: 2.884s, średnio 346.742/s
Pobranie wykresów: 176.136s, średnio 5.677/s
```
