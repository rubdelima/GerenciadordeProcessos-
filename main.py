import pygame
from botoes import Retangulo, Circulo, Processo
import time
from threading import Thread

tempo_corrido = 0
def update_time():
    global tempo_corrido
    global encerrar
    while not encerrar:
        time.sleep(0.1)
        tempo_corrido = tempo_corrido + 1

def atualizar_lista():
    global lista_processos
    global tipo_processo
    if len(lista_processos) > 0:
        match(tipo_processo):
            case 'Round Robin':
                round_robin()
            case '  Priority':
                priority()
            case '      SJF':
                sjf()
            case '     FiFo':
                fifo()
            case _:
                pass
    
def round_robin():
    global lista_processos
    for i in lista_processos:
        i.size_x -= 1


def fifo():
    global lista_processos
    if lista_processos[0].size_x >0:
        lista_processos[0].size_x -= 1
    if lista_processos[0].size_x <= 0:
        del lista_processos[0]

        
def sjf():
    global lista_processos
    lista_processos = sorted(lista_processos, key=lambda x: x.size_x)
    fifo()

def priority():
    global lista_processos
    lista_processos = sorted(lista_processos, key=lambda x: x.prioridade, reverse=True)



pygame.init()
# Defindo as globais da tela
window_size = (600, 600)
background_color = (217, 217, 217)
screen = pygame.display.set_mode(window_size)
screen.fill(background_color)
box_titulo = Retangulo(
    janela = screen,
    pos_x=50, pos_y= 20, size_x = 500, size_y = 50,
    color=(166, 166, 166), label='    Escalonador de Processos'
)
lista_box_aux = ['Tempo de execução:', 'Prioridade:', 'Selecione a Cor:']
lista_box = []
for i, box in enumerate(lista_box_aux):
    lista_box.append(Retangulo(
        janela=screen,
        pos_x= 80, pos_y = 100 + i*50, size_x=440, size_y=40,
        color=(111,111,111), label=box, label_size=15, center=False
    ))

lista_b_tempo = []
for i in range(10):
    lista_b_tempo.append(Circulo(
        janela=screen, 
        pos_x=300+ 22*i,pos_y = 120, size_x=10, size_y=10,
        label=f'{i+1}', label_size=15, center=False
    ))

lista_b_prioridade = []
for i in range(10):
    lista_b_prioridade.append(Circulo(
        janela=screen, 
        pos_x=300+ 22*i,pos_y = 170, size_x=10, size_y=10,
        label=f'{i+1}', label_size=15, center=False
    ))

lista_b_cores_aux = [(255, 49, 49), (255, 222, 89), (193, 255, 114), (92, 225, 230), (203, 108, 190)]
lista_b_cores = []
for i , cor in enumerate(lista_b_cores_aux):
    lista_b_cores.append(Circulo(
        janela=screen, 
        pos_x=300 + 48*i, pos_y = 220, size_x=20, size_y=20,
       double=True, double_collor=cor  
    ))

botao_inserir = Retangulo(
    janela= screen, 
    pos_x=200, pos_y= 270, size_x=200, size_y=50,
    color=(111,111,111), label='       Inserir', label_size=15, center=True
)


lista_escalonadores_aux = ['     FiFo', '      SJF', '  Priority', 'Round Robin']
lista_escalonadores =[]

for i, escalonador in enumerate(lista_escalonadores_aux):
    lista_escalonadores.append(Retangulo(
        janela= screen, 
        pos_x=50+i*125, pos_y= 330, size_x=100, size_y=50,
        color=(111,111,111), label=escalonador, label_size=15, center=True
    ))

lista_escalonadores[0].is_selected = True

barra_processos = Retangulo(
        janela= screen, 
        pos_x=50, pos_y= 450, size_x=500, size_y=100,color=(111,111,111), label=None)

lista_processos = [
    Processo(
        janela=screen,
        pos_x=50, pos_y= 450, size_x=200, size_y=100,color=(193, 255, 114), label=None,prioridade=12),
    Processo(janela=screen,
        pos_x=150, pos_y= 450, size_x=100, size_y=100,color=(255, 222, 89), label=None,prioridade=20),
]

lista_global = [lista_b_cores, lista_b_prioridade, lista_b_tempo, lista_processos, lista_escalonadores]

tipo_processo = '     FiFo'

encerrar= False
thr = Thread(target=update_time)
thr.start()


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            encerrar = True
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            for i in lista_global:
                lista_aux = []
                print('sdfasdf')
                for j in i:
                    a = j.pos_x < mouse_pos[0] < j.pos_x + j.size_x
                    b = j.pos_y < mouse_pos[1] < j.pos_y + j.size_y
                    if a and b:
                        j.is_selected = not j.is_selected
                        break
            a = botao_inserir.pos_x < mouse_pos[0] < botao_inserir.pos_x + botao_inserir.size_x
            b = botao_inserir.pos_y < mouse_pos[1] < botao_inserir.pos_y + botao_inserir.size_y
            if a and b:
                new_cor = None
                new_prioridade = None
                new_tempo = None
                for i in lista_b_cores:
                    if i.is_selected:
                        new_cor = i.color
                        #i.is_selected = False
                        #break
                for i in range(10):
                    if lista_b_prioridade[i].is_selected:
                        new_prioridade = (i+1)*10
                        #lista_b_prioridade[i].is_selected = False
                        #break
                    if lista_b_tempo[i].is_selected:
                        new_tempo = (i+1)*10
                        #lista_b_tempo[i].is_selected = False
                        #break
                if new_prioridade != None and new_cor != None and new_tempo != None:
                    if len(lista_processos) == 0:
                        new_position = 50
                    else:
                        aux = len(lista_processos)-1
                        new_position = lista_processos[aux].pos_x + lista_processos[aux].size_x
                    lista_processos.append(Processo(
                                    janela=screen,pos_x=new_position, pos_y= 450, size_x=new_tempo, size_y=100,
                                    color=new_cor, label=None,prioridade=new_prioridade))
            

                        
            
        #print(event)
        
    if not(tempo_corrido %10):
        for i in lista_escalonadores:
                if i.is_selected:
                    tipo_processo = i.label
                    break

        if len(lista_processos) > 0:
            match(tipo_processo):
                case 'Round Robin':
                    for i in lista_processos:
                        i.size_x -= 1
                case '  Priority':
                    lista_processos = sorted(lista_processos, key=lambda x: x.prioridade, reverse=True)
                case '      SJF':
                    lista_processos = sorted(lista_processos, key=lambda x: x.size_x)
                case _:
                    pass
                
            if tipo_processo != "Round Robin":
                if lista_processos[0].size_x >0:
                    lista_processos[0].size_x -= 1
                if lista_processos[0].size_x <= 0:
                    del lista_processos[0]
    
    barra_processos.atualizar_botao()
    
    for i in range(len(lista_processos)):
        if i !=0:
            lista_processos[i].pos_x = lista_processos[i-1].pos_x+lista_processos[i-1].size_x
    
    for i in lista_global:
        for j in i:
            j.atualizar_botao()
    
           
    pygame.display.update()


