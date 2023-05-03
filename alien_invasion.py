import sys
import pygame

def run_game():
    #게임을 초기화하고 화면 객체를 만듭니다.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")


    While True:
        # for event in pygame.event.get():
        #     event.type == pygame.QUIT:
        #         sys.exit()
        pygame.display.filp()
    
run_game()