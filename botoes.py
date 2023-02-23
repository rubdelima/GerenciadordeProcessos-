import pygame
class Botao():
    def __init__(self,janela,  pos_x, pos_y, size_x, size_y,
                 color,double=False, double_collor=False, center=True , label=None, label_size=25):
        self.janela = janela
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
        self.color = color
        self.label = label
        self.label_size = label_size
        self.center = center
        self.primary_collor = self.color
        self.double = double
        self.double_collor = double_collor
        self.is_selected = False
        self.atualizar_botao()
        
        
    def atualizar_botao(self):
        if self.is_selected:
            self.color = (0, 191, 99)
        else:
            self.color = self.primary_collor
            
        self.rect = pygame.Rect(self.pos_x, self.pos_y, self.size_x, self.size_y)
        pygame.draw.rect(self.janela, self.color, self.rect, border_radius=25)
        if self.double:
            self.rect_doubly = pygame.Rect(self.pos_x+self.size_x*0.1, self.pos_y+self.size_y*0.1, self.size_x*0.8, self.size_y*0.8)
            pygame.draw.rect(self.janela, self.double_collor, self.rect_doubly, border_radius=20)
        
        if self.label != None:
            font = pygame.font.Font('font.ttf', self.label_size)
            text = font.render(str(self.label), True, (255, 255, 255))
            if self.center:
                font_distance = len(list(self.label))*self.label_size/10
                self.font_x = self.pos_x + font_distance/2
            else:
                self.font_x = self.pos_x + 10
            self.janela.blit(text, (self.font_x, self.pos_y+(self.size_y//10)))

        
class Processo(Botao):
    def __init__(self, janela,  pos_x, pos_y, size_x, size_y,
                 color, prioridade,  label=None, label_size=25, center = True):
        label = str(prioridade)
        super().__init__(janela=janela, pos_x=pos_x, pos_y=pos_y, size_x=size_x, size_y=size_y,
                 color=color, label=label, label_size=label_size, center=center)
        self.prioridade = prioridade
    
        

        

        