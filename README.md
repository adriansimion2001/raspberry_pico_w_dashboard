# Proiect raspberry_pico_w_dashboard

Dashboard-ul a fost realizat utilizand framework-ul microdot, cat si librari uzuale micropython (ex. machine pentru controlul GPIO).

<img alt="image" src="https://github.com/adriansimion2001/raspberry_pico_w_dashboard/assets/108823792/ca4c2183-8c06-483d-b0b1-e364c53da548">
<img alt="image" src="https://github.com/adriansimion2001/raspberry_pico_w_dashboard/assets/108823792/58dbf094-73df-4c82-b61d-43747916eacb">
<img alt="image" src="https://github.com/adriansimion2001/raspberry_pico_w_dashboard/assets/108823792/850d3d59-9451-4adc-a699-e7c038aff709">
<img alt="image" src="https://github.com/adriansimion2001/raspberry_pico_w_dashboard/assets/108823792/531004b9-a1b6-438c-b8e7-7233731f4084">



What you need:
  1) Raspberry pico w board (este necesara versiunea w deoarece ne folosim de functionalitatea wireless a microcontroller-ului).
  2) O retea wi-fi (o retea wi-fi locala sau un hotspot wireless).

How to setup:
  1) Placa raspberry pico w se conecteaza la computer printr-un calbu usb -> micro usb.
  2) Folosind Thonny se completeaza campurile SSID si SSI_PASSWORD din fisierul boot.py cu datele corespunzatoare retelei wi-fi utilizate.
  3) Se recomplieazaa codul si se ruleaza, dupa modificarile facute placa poate fi alimentata si de la un acumulator extern, fara a necesita un computer.
  4) Se copiaza adresa IP aparuta in consola compilatorului intr-un browser pentru a putea accesa pagina principala.

How to use:
  1) Pagina principala prezinta un indicator pentru Data si ora, Un api pentru vreme (se poate configura in fisierele html).
  2) Folosind butonul ADD putem configura pinii GPIO ca intrari sau iesiri digitale.
  3) Folosind butonul REMOVE putem elimina butoanele/indicatoarele introduse.

Bibliografie:
  - Proiectul se bazeaza pe repository-ul lui donskytech : rpi-pico-w-bme280-weather-station (https://github.com/donskytech/rpi-pico-w-bme280-weather-station)
