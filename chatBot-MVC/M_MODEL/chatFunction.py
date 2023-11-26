# Definizione funzioni per operazioni mirate


# GeneraPreventivo
def getPreventive(customer, noItem, item, price, aliquotes):
    str = ("Generami un preventivo per %s, "
           "contenente %s pezzi di %s al prezzo di %s cadauno, "
           "considerando un aliquota di %s", customer, noItem, item, price, aliquotes)

    return str

#GeneraContratto -> toDo!