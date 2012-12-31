Gas App Solution - L’altra faccia del GAS
(e ora, qualcosa di completamente diverso!)

Cosa è?
Gas App Solution (o GAS in acronimo) vuole essere uno strumento pronto per tutti i gestori di gruppi di acquisto solidale (o G.A.S. in acronimo); l’intenzione degli ideatori è di fornire uno strumento pronto per chiunque voglia gestire il proprio gruppo senza avere necessariamente le conoscenze informatiche richieste.

Cosa significa “RFC”?
“Request For Comment”, è il modo in cui nella comunità open source (e su internet per estensione) si elaborano le idee: chi ne ha una la propone alla comunità e chiede pareri e commenti a chiunque possa essere interessato.
Ovviamente è un po’ pretenzioso e borioso voler qualificare questo documento una RFC in senso strettamente tecnico, ma le regole che segue e gli scopi che assolve sono più o meno gli stessi.

Perché questo nome di progetto?
Inizialmente era stato proposto “The Terry Project”, ma la citazione dei Monty Python non era immediatamente comprensibile, o non lo era affatto, per chi non fosse fan dei Monty Python, quindi si è scelto un nome più descrittivo.
E comunque un nome vale l’altro, l’importante è che piaccia e dica qualcosa a chi lo legge.

In cosa si differenzia GAS da altre soluzioni simili?
Innanzitutto è scritto in python, per seconda cosa nasce dall’esperienza diretta di alcuni G.A.S. che hanno sempre gestito acquisti e consegne “a mano”: pur facendo uso di aiuti telematici (email, programmi per fogli di calcolo, etc.) tutte le attività ripetitive e di gestione vengono effettuate dalle persone. Lo scopo principale di GAS è di aiutare i gestori dei gruppi (e quindi i relativi fornitori e clienti) fornendo degli strumenti per automatizzare i calcoli e le operazioni ripetitive e di interrogazione della base di dati.

E non ci sono altri prodotti scritti in python?
Che io sappia ce n’è uno solo: ed è django-gas, ospitato su google code, ma si appoggia a MySQL come motore del database, mentre vorremmo utilizzare PostgreSQL per il nostro progetto. In più non sembra aggiornato e mantenuto sin dal giugno 2011.

Ma non doveva essere anche per “non addetti ai lavori”?
Purtroppo un tot di conoscenze tecniche sono richieste, ma c’è l’intenzione di istituire un gruppo di lavoro che supporti a tutti i livelli i gestori di GAS volenterosi che, ad esempio, non hanno le conoscenze tecniche adeguate, o che non abbiano il tempo e il modo di avere una conoscenza approfondita di dette tecniche.

Come opererebbe questo gruppo di lavoro?
Ci sono diversi livelli di azione: si parte dalla progettazione del software, al suo sviluppo, incluse le necessarie fasi di test, nonché la sua manutenzione (bug fix e/o introduzione di nuove funzioni).
C’è poi la questione dell’hosting su internet, si è pensato di partire da soluzioni “casalinghe” o di affittare in consorzio uno spazio su web su cui far girare il sito.
Abbiamo anche da istituire un gruppo di assistenza tecnica, che provveda sia all’installazione e configurazione per gli utenti meno addentro alla materia, che al supporto tecnico post-installazione per tutti gli utenti.
Infine, c’è sicuramente bisogno di un altro gruppo che gestisca le relazioni, con i GAS interessati, con eventuali soggetti interessati a finanziare l’opera (in qualsiasi modo: con conferimenti in danaro, con prestazione di opera occasionale gratuita, etc.), con soggetti interessati a prendere parte attiva e stabile con il progetto, promozione presso organi di stampa e diffusione, etc.

Un “progettone”, non c’è il rischio di perdersi per strada?
Certamente sì, per questo motivo, prima ancora di scrivere una riga di codice, e anche prima di disegnare un abbozzo di database, vogliamo proporre questa idea a quanti più possano essere interessati per poter partire tutti insieme.

Quindi non esiste nulla di concreto riguardo a GAS?
Il passo più difficile è stato fatto: sceglierne il nome (potrà anche variare in fase di rilascio), altrimenti sarebbe sempre rimasto una entità indefinita.
Ci sono già tre persone che stanno pensando e modellando l’idea, e una di queste sta provvedendo ad acquisire la maggior parte delle conoscenze tecniche necessarie a rendere concreta l’idea.
L’altra persona, coinvolta attivamente nella gestione di un gruppo di acquisto, legge, corregge, e dà pareri; può sembrare insignificante come aiuto, ma è una grossa parte del lavoro.
La terza persona non è un tecnico, e non partecipa attivamente al gruppo, ha solo compiti di correzione e supporto all’idea; anche il suo contributo è molto importante.

Possiamo avere una tempistica?
Non ce n’è nessuna per ora, già al punto in cui siamo ci sono una serie di questioni da risolvere per poter presentare una idea più solida.

Ma almeno si sa che funzioni dovrebbe avere GAS?
Sì, nella loro schematicità.
In sostanza l’obiettivo è di creare un prodotto agile e veloce nelle sue funzioni, nonché gradevole alla vista e con una interfaccia intuitiva.
Ad esempio, le anagrafiche saranno uniche, sia che il soggetto sia un fornitore, un cliente, un GAS a sua volta, o un GAS di GAS (o consorzio di essi); in questo modo si snellirà l’accesso al database e si eviteranno duplicazioni di dati che potrebbero portare ad errori non previsti.

Esistono altri progetti simili e funzionanti?
Come detto prima, non ho notizia di altri progetti scritti in python a parte “django-gas”.
Ci sono altre due soluzioni che conosco e sono “gestigas” e “gas-web”, il primo è scritto in php, che vogliamo evitare; mentre il secondo non solo non sembra essere open source, ma soprattutto sembra essere a pagamento.
Noi vogliamo creare un prodotto che vada oltre questi limiti: il fatto che sarà open source non vorrà automaticamente dire che sarà del tutto gratuito, perché dietro le schermate di gestione alla fin fine c’è sempre un omino che preme i tasti e il cui lavoro va retribuito.
D’altro canto non chiederemo nessun “contributo obbligatorio” per poter accedere ai sorgenti, alla documentazione, all’assistenza e a tutto quel che riguarda questo progetto.

Perché questa avversione per il PHP e MySQL?
PHP è un linguaggio di scripting, e va benissimo per piccole applicazioni o per siti dinamici senza troppi dati da elaborare; stesso discorso per MySQL: diventa debole con grossi volumi di dati.
E infine, Facebook è scritto in php, mentre Google (e tutti i siti correlati) sono scritti in python. Lanciate una ricerca su uno o sull’altro e verificate la velocità dei due siti.

A chi ci si può rivolgere se interessati?
Su facebook basta mandare un messaggio ad EvanMac BongoRage, lo pseudonimo dell’ideatore di GAS, altrimenti via e-mail potete scrivere alle Edizioni42 (edizioni42@gmail.com). Qualsiasi cosa vi venga in mente riguardo a questo progetto è ben accetta; soprattutto perché è una RFC, se non nella forma, almeno nelle intenzioni.
