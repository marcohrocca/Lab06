from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        cnx = get_connection() #Mi connetto al database
        if cnx is None:  # se la connessione è fallita
            return None  # restituisco None invece di andare in errore
        cursor = cnx.cursor(dictionary=True)
        query= "SELECT * FROM STRUMENTO" #CHIEDO TUTTI GLI STRUMENTI
        cursor.execute(query)
        lista_strumenti=[] #inizializzo contenitore
        #listview come lista vuota(quello che mostrerò dopo)
        for riga in cursor: #faccio ciclo su ogni riga trovata
            strumento = Strumento(
                riga["codice"],
                riga["tipo"],
                riga["marca"],
                riga["anno_acquisto"],
                riga["valore"],
                riga["disponibile"]

            )
            lista_strumenti.append(strumento) #aggiungo alla lista
            #contenitore ogni strumento letto dal database
        cursor.close() #chiude cursore
        cnx.close()    #chiudo la connessione col database
        return lista_strumenti #restituisco la lista

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        #prime due righe faccio copia in colla da prima
        cnx = get_connection()  # Mi connetto al database
        if cnx is None:  # se la connessione è fallita
            return None  # restituisco None invece di andare in errore
        cursor = cnx.cursor(dictionary=True)
        query= f"SELECT * FROM STRUMENTO WHERE tipo='{tipo}'" #query simile a prima ma con condizione in più
        #ovvero tipo uguale a quello richiesto
        #Faccio copia in colla della parte precedente visto che è uguale
        cursor.execute(query)
        lista_strumenti_ricerca = []  # inizializzo contenitore
        # listview come lista vuota(quello che mostrerò dopo)
        for riga in cursor:  # faccio ciclo su ogni riga trovata
            strumento = Strumento(
                riga["codice"],
                riga["tipo"],
                riga["marca"],
                riga["anno_acquisto"],
                riga["valore"],
                riga["disponibile"]

            )
            lista_strumenti_ricerca.append(strumento)  # aggiungo alla lista
            # contenitore ogni strumento letto dal database
        cursor.close()  # chiude cursore
        cnx.close()  # chiudo la connessione col database
        return lista_strumenti_ricerca  # restituisco la lista


