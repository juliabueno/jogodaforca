from mostra_forca import corpo
from random import randint
from palavras import palavras

def run():
    print("""
    ###########################################################
    ############## BEM-VINDO AO JOGO DA FORCA #################
    ###########################################################
    """)

    try:
        
        arquivo_score = open('score_forca.txt','r')
        arquivo_derrotas = open('derrotas_forca.txt','r')
    except:
        
        arquivo_score = open('score_forca.txt','w')
        arquivo_score.write('0')
        arquivo_score = open('score_forca.txt','r')
        
        arquivo_derrotas = open('derrotas_forca.txt','w')
        arquivo_derrotas.write('0')
        arquivo_derrotas = open('derrotas_forca.txt','r')

    score = int(arquivo_score.read())
    derrotas = int(arquivo_derrotas.read())

    def sortear_palavra_e_categoria(palavras):
        categoria = list(palavras.keys())[randint(0,len(list(palavras.keys()))-1)]
        palavra = palavras[categoria][randint(0,len(palavras[categoria])-1)]
        return categoria,palavra
        
    continuar = True
    while continuar:
        
        categoria_e_palavra = sortear_palavra_e_categoria(palavras)
        categoria = categoria_e_palavra[0]
        palavra = categoria_e_palavra[1]

        
        letras_acertadas = ['_' for i in range(len(palavra))]

        
        acertou, enforcou = False, False
        erros = 0
        jogadas = 0

        print(f""" 
    VITÓRIA:     {score}
    DERROTAS:    {derrotas}
    CATEGORIA: {categoria}
        """)

        while(not acertou and not enforcou):

            print(corpo[erros])
            print(letras_acertadas)

            chute = input('Chute uma letra: ')
            
            
            if (chute.upper() in palavra.upper()):
                posicao = 0
                for letra in palavra:
                    if chute.upper() == letra.upper():
                        letras_acertadas[posicao] = letra
                    posicao += 1
            
            
            else:
                erros += 1

             
            if erros == 6:
                
                print("""
            |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
            |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
            |||||||||||||||||||||||||||||                            ||||||||||||||||||||||||||||||||
            |||||||||||||||||||||||||||||         ENFORCOU!!!        ||||||||||||||||||||||||||||||||
            |||||||||||||||||||||||||||||                            ||||||||||||||||||||||||||||||||
            |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
            |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                
                """)

                print(corpo[6])
                
                
                
                derrotas += 1
                arquivo_derrotas = open('derrotas_forca.txt','w')
                arquivo_derrotas.write(str(derrotas))
                
                continuar = True if (input('Quer continuar? ')[0].upper() == 'S') else False
                break

            
            if list(palavra) == letras_acertadas:

                print(f""" 
                           

                            PARABÉNS ACERTOU!!! você ganhou!!!

                              A PALAVRA É {palavra.upper()} 
                              
                    """)
                
                
                score += 1
                arquivo_score = open('score_forca.txt','w')
                arquivo_score.write(str(score))
                
                continuar = True if (input('Quer continuar? ')[0].upper() == 'S') else False
                break
            jogadas += 1

    arquivo_score.close()
    arquivo_derrotas.close()