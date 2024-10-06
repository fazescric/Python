def aggiungi_libro(libreria, titolo, autore):
    if titolo not in libreria:
        libreria[titolo] = {"autore": autore, "valutazioni": []}
        print(f"Libro '{titolo}' di {autore} aggiunto alla libreria.")
    else:
        print(f"Il libro '{titolo}' è già presente nella libreria.")

def aggiungi_valutazione(libreria, titolo, valutazione):
    if titolo in libreria:
        libreria[titolo]["valutazioni"].append(valutazione)
        print(f"Valutazione {valutazione} aggiunta a '{titolo}'.")
    else:
        print(f"Il libro '{titolo}' non esiste nella libreria.")

def calcola_media(libreria, titolo):
    if titolo in libreria and libreria[titolo]["valutazioni"]:
        media = sum(libreria[titolo]["valutazioni"]) / len(libreria[titolo]["valutazioni"])
        return round(media, 2)
    else:
        print(f"Il libro '{titolo}' non ha valutazioni o non esiste.")
        return None

def mostra_libreria(libreria):
    if libreria:
        for titolo, dettagli in libreria.items():
            media = calcola_media(libreria, titolo)
            media_str = str(media) if media is not None else "N/A"
            print(f"Titolo: {titolo}, Autore: {dettagli['autore']}, Media Valutazioni: {media_str}")
    else:
        print("La libreria è vuota.")

libreria = {}

aggiungi_libro(libreria, "Il Signore degli Anelli", "J.R.R. Tolkien")
aggiungi_libro(libreria, "1984", "George Orwell")

aggiungi_valutazione(libreria, "Il Signore degli Anelli", 3)
aggiungi_valutazione(libreria, "Il Signore degli Anelli", 5)

aggiungi_valutazione(libreria, "1984", 4)
aggiungi_valutazione(libreria, "1984", 6)

print("\nElenco dei libri nella libreria:")
mostra_libreria(libreria)
print(f"\nmedia libro: ")
print(calcola_media(libreria, "1984”)
