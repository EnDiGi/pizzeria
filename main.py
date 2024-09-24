import menu

nomePizzeria = 'Pac-Man Pizza'

def accogliCliente():

        nome = ''
        età = 0

        print('Benvenuto nella pizzeria ' + nomePizzeria + '!')

        return nome, età

def faiOrdine(nome, età):
        ordine = []
		
        if età >= 18:
                menu.bevande += menu.bevande18
		
        print(menu.menu)
		
        return ordine

def mostraOrdine(nome, ordine):
        pass

def main():
        nome, età = accogliCliente()
        ordine = faiOrdine(nome, età)
        mostraOrdine(nome, ordine)

if __name__ == '__main__':
        main()