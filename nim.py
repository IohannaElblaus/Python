#definição das jogadadas
jogada_comp=0
jogada_usua=0

def computador_escolhe_jogada(nc,mc):
	jogada_comp=(nc%(mc+1))
	if jogada_comp==0:
		jogada_comp=mc
	return jogada_comp

def usuario_escolhe_jogada(nu,mu):
	jogada_usua=int(input("Quantas peças você vai tirar?"))
	while jogada_usua<=0 or jogada_usua>nu or jogada_usua>mu:
		print("Oops! Jogada inválida! Tente de novo.")
		jogada_usua=int(input("Quantas peças você vai tirar?"))
	return jogada_usua

#definição da partida
vezdocomp=True
def partida():
	n=0
	m=0
	retirada=0
	while n<=0:
		n=int(input("Quantas peças?"))
	while m==0 or n<m:
		m=int(input("Limite de peças por jogada?"))

	if n%(m+1)==0:
		print("\nVocê começa!")
		vezdocomp=False
	else: 
		print("\nComputador começa!")
		vezdocomp=True

	while n!=0:
		if vezdocomp:
			retirada=computador_escolhe_jogada(n,m)
			n=n-retirada
			print ("O computador tirou", retirada,"peça(s).")
			print ("Agora restam",n,"peças no tabuleiro.\n")
			vezdocomp=False

		else:
			retirada=usuario_escolhe_jogada(n,m)
			n=n-retirada
			print ("Você tirou",retirada,"peça(s).")
			print ("Agora restam",n,"peças no tabuleiro.\n")
			vezdocomp=True

	if n==0 and vezdocomp==False:
		print ("Fim do jogo! O computador ganhou!")

#apresentação
print ("Bem-vindo - para jogar uma partida isolada ao jogo do NIM! Escolha:\n")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")
jogo=0
while jogo!=1 and jogo!=2: 
	jogo = int(input("opção 1 ou 2?"))

#apenas 1 jogo
if jogo==1:
	print("\nVocê escolheu uma partida!\n")
	partida()
	print("**** Fim da partida! ****")

#campeonato de 3 jogos
if jogo==2:
	print("\nVocê escolheu um campeonato!\n")
	rodada=1
	while rodada<=3:
		print("**** Rodada",rodada,"****\n")
		partida()
		rodada=rodada+1
		print("**** Final do campeonato! ****\n")
		print("Placar: Você 0 X 3 Computador")
