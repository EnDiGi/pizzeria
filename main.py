nomePizzeria = 'nomegenericochecambieròappenativedròetroveraiunnomemigliore'

def accogliCliente():

	nome = ''
	età = 0

	print('Benvenuto nella pizzeria', nomePizzeria + '!')

	return nome, età

def faiordine(nome, età):
	ordine = []

	return ordine

def mostraOrdine(nome, ordine):
	pass

def main():
	nome, età = accogliCliente()
	ordine = faiordine(nome, età)
	mostraOrdine(nome, ordine)

if __name__ == '__main__':
	main()