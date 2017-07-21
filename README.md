# Jupyter Notebook + Reveal.js = Slides

## Introduzione

Microsoft Powerpoint non lo so usare. Sono un programmatore. Sono abituato a scrivere codice html e fare backend in Python. Se proprio devo scrivo anche un po' di javascript. 

La mia scelta preferita è usare reveal.js unito ai notebook Jupyter. Basta creare un notebook  e usare `nbconvert` per creare le slides. 

In questo modo, posso caricare le slides sul mio sito e accedere ad esse da qualunque computer connesso ad internet, senza stare li a farmi problemi su adattatori e prese varie.


## Getting Started

1. Il notebook si trova nella cartella `static`. Per informazioni su come creare le slide in un notebook qui trovate un bel [link](http://www.slideviper.oquanta.info/tutorial/slideshow_tutorial_slides.html#/3) 

2. Quando avete finito, tornate nella cartella principale e lanciate `python build.py`. 

3. Avete appena creato un file html. Quello che vi manca è avviare un server. Per farlo, lanciate `python run.py`, e poi aprite il browser all'indirizzo indicato.

4. Opzionalmente, potete eseguire `python build.py -r` per creare la pagina html e lanciare in automatico il server (utile per quando state scrivendo il notebook).

#### Servono:
- Python 3.5.2
- nbconvert 4.2.0
- jupyter 1.0.0
- reveal.js 3.1.0

#### Demo:
- [Machine Learning as a Service](http://www.alessandrocucci.it/slides/mlaas/index.html)


## Copyright
Guarda il file [LICENSE](LICENSE) per i dettagli. 
P.s. E' tutto free e open: prendi, modifica e condividi!
