import pygame
import sys

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((712, 712)) #, flags=pygame.NOFRAME)
pygame.display.set_caption("Music of fog")
icon = pygame.image.load('pixai-1743071598528304308.png')
pygame.display.set_icon(icon)

myfont = pygame.font.SysFont('Arial', 25)
text_start = myfont.render('Может мне стоит подойти к этой скале?..', True, 'black')
text_start_y = 100
start = pygame.image.load('photoassets\start.png')
banner = pygame.transform.scale(start, (500, 200))
banner_y = 0

background = pygame.image.load('photoassets\dackground.png').convert()

opened = False

ui_holder = pygame.image.load('photoassets\k1.png')

ui_book = pygame.image.load('photoassets\k23.png')


esc_menu = pygame.image.load('photoassets\escape_menu.png')

inventory = pygame.image.load('photoassets\inventory.png')

checker = 0
if checker == 0:
    a = pygame.mixer.Sound('msc\wa.mp3')
    b = pygame.mixer.Sound('msc\wb.mp3')
    c = pygame.mixer.Sound('msc\wc.mp3')
    d = pygame.mixer.Sound('msc\wd.mp3')
    e = pygame.mixer.Sound('msc\we.mp3')
    f = pygame.mixer.Sound('msc\wf.mp3')
    g = pygame.mixer.Sound('msc\wg.mp3')
else:
    a = pygame.mixer.Sound('msc\wwa.mp3')
    b = pygame.mixer.Sound('msc\wwb.mp3')
    c = pygame.mixer.Sound('msc\wwc.mp3')
    d = pygame.mixer.Sound('msc\wwd.mp3')
    e = pygame.mixer.Sound('msc\wwe.mp3')
    f = pygame.mixer.Sound('msc\wwf.mp3')
    g = pygame.mixer.Sound('msc\wwg.mp3')


bgsound = pygame.mixer.Sound('untitled.wav')

bgsound.play()

map_open = pygame.mixer.Sound('map_slot_sound.wav')

player_down = [
    pygame.image.load('girlstand\GirlStand1.png'),
    pygame.image.load('girlstand\GirlStand2.png'),
    pygame.image.load('girlstand\GirlStand3.png'),
    pygame.image.load('girlstand\GirlStand4.png'),       
]

player_right = [
    pygame.image.load('girlstand\GirlRight1.png'),
    pygame.image.load('girlstand\GirlRight2.png'),
    pygame.image.load('girlstand\GirlRight3.png'),
    pygame.image.load('girlstand\GirlRight4.png'), 
    
]

player_left = [
    pygame.image.load('girlstand\GirlLeft1.png'),
    pygame.image.load('girlstand\GirlLeft2.png'),
    pygame.image.load('girlstand\GirlLeft3.png'),
    pygame.image.load('girlstand\GirlLeft4.png'),     
]

player_up = [
    pygame.image.load('girlstand\GirlUp1.png'),
    pygame.image.load('girlstand\GirlUp2.png'),
    pygame.image.load('girlstand\GirlUp3.png'),
    pygame.image.load('girlstand\GirlUp4.png'),     
]

player_afk = [
    pygame.image.load('girlstand\GirlStand1.png'),
    pygame.image.load('girlstand\GirlStand1.png'),
    pygame.image.load('girlstand\GirlStand2.png'),
    pygame.image.load('girlstand\GirlStand2.png')
]

anim_count = 0
anim_speed = 0

map_height = 552
map_width = 652
player_x = 300
player_y = 300
player_speed = 3
press_start = False



sequence = ['f', 'g', 'm', 'g', 'h','m','l']
current_index = 0



font = pygame.font.Font(None, 36)
text = font.render('Подсказка: Последовательность: ' + ' '.join(sequence), True, (0, 0, 0))
text_rect = text.get_rect(center=(320, 30))

result_font = pygame.font.Font(None, 36)
result_text = ""

font = pygame.font.Font(None, 60)
text_menu = font.render('Начать', True, ('dark green'))
text_menu_rect = text_menu.get_rect(center=(320, 300))

fontinst = pygame.font.Font(None, 24)
text_instrument_chose = fontinst.render('Выбрать флейту', True, ('dark green'))
text_instrument_chose_rect = text_instrument_chose.get_rect(center=(80, 335))
text_instrument_chose2 = fontinst.render('Выбрать гитару', True, ('dark green'))
text_instrument_chose_rect2 = text_instrument_chose2.get_rect(center=(80, 365))

start_game = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if text_menu_rect.collidepoint(event.pos):
                start_game = True

    if not start_game:
        screen.blit(start, (0,0))
        screen.blit(text_menu, text_menu_rect)
    else:        
        run = True
        while run:
        
            clock.tick(25)

            keys = pygame.key.get_pressed()

            screen.blit(background, (0, 0))  

            screen.blit(ui_holder, (80, 580))

            screen.blit(text_start, (120, 635))

            screen.blit(ui_book, (20, 620))
            
            checker = 0
            if checker == 0:
                a = pygame.mixer.Sound('msc\wa.mp3')
                b = pygame.mixer.Sound('msc\wb.mp3')
                c = pygame.mixer.Sound('msc\wc.mp3')
                d = pygame.mixer.Sound('msc\wd.mp3')
                e = pygame.mixer.Sound('msc\we.mp3')
                f = pygame.mixer.Sound('msc\wf.mp3')
                g = pygame.mixer.Sound('msc\wg.mp3')
            else:
                a = pygame.mixer.Sound('msc\wwa.mp3')
                b = pygame.mixer.Sound('msc\wwb.mp3')
                c = pygame.mixer.Sound('msc\wwc.mp3')
                d = pygame.mixer.Sound('msc\wwd.mp3')
                e = pygame.mixer.Sound('msc\wwe.mp3')
                f = pygame.mixer.Sound('msc\wwf.mp3')
                g = pygame.mixer.Sound('msc\wwg.mp3')

            if player_x < 0:
                player_x = 0
            if player_x > map_width:
                player_x = map_width
            if player_y < 0:
                player_y = 0
            if player_y > map_height:
                player_y = map_height

            if keys[pygame.K_LEFT]:
                player_x -= player_speed
                screen.blit(player_left[anim_count], (player_x, player_y))
            elif keys[pygame.K_RIGHT] :
                player_x += player_speed
                screen.blit(player_right[anim_count], (player_x, player_y))
            elif keys[pygame.K_UP] :
                player_y -= player_speed
                screen.blit(player_up[anim_count], (player_x, player_y))
            elif keys[pygame.K_DOWN] :
                player_y += player_speed
                screen.blit(player_down[anim_count], (player_x, player_y))
            elif keys[pygame.K_ESCAPE]:  
                screen.blit(esc_menu, (-10, 50))
                uiE = myfont.render('А тут', True, 'black')
                uiE2 = myfont.render('меню', True, 'black')
                uiE3 = myfont.render('выхода', True, 'black')
                screen.blit(uiE, (280, 235))
                screen.blit(uiE2, (280, 275))
                screen.blit(uiE3, (280, 305))
            elif keys[pygame.K_i]: 
                screen.blit(inventory, (-10, 50))
                ui = myfont.render('Пока тут не хватает иконок', True, 'black')
                ui2 = myfont.render('но по задумке тут', True, 'black')
                ui3 = myfont.render('выбирается инструмент', True, 'black')
                screen.blit(ui, (80, 235))
                screen.blit(ui2, (80, 275))
                screen.blit(ui3, (80, 305))
                screen.blit(text_instrument_chose, text_instrument_chose_rect) 
                screen.blit(text_instrument_chose2, text_instrument_chose_rect2) 
               
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if text_instrument_chose_rect.collidepoint(event.pos):  
                        checker = 1 
                    elif text_instrument_chose_rect2.collidepoint(event.pos): 
                        checker = 0       
            else :
                screen.blit(player_afk[anim_count], (player_x, player_y))

                if 220 < player_x < 260 and 290 < player_y < 300:
                    screen.blit(esc_menu, (-10, 50))
                    screen.blit(text, text_rect)
                    for event in pygame.event.get():        
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_f :
                                pygame.mixer.Sound.play(a)
                            elif event.key == pygame.K_g :
                                pygame.mixer.Sound.play(b)
                            elif event.key == pygame.K_h :
                                pygame.mixer.Sound.play(c)
                            elif event.key == pygame.K_j :
                                pygame.mixer.Sound.play(d)
                            elif event.key == pygame.K_k :
                                pygame.mixer.Sound.play(e)
                            elif event.key == pygame.K_l :
                                pygame.mixer.Sound.play(f)
                            elif event.key == pygame.K_m :
                                pygame.mixer.Sound.play(g)
                            
                            if event.unicode == sequence[current_index]:
                                current_index += 1
                            else:
                                current_index = 0
                    if current_index == len(sequence):
                        result_text = "Поздравляем! Вы решили головоломку!"
                        current_index = 0    
                    result_surface = result_font.render(result_text, True, (255, 0, 0))
                    result_rect = result_surface.get_rect(center=(400, 300))
                    screen.blit(result_surface, result_rect)
                        
            for function_keys in pygame.event.get():
            
                if function_keys.type == pygame.KEYDOWN:
                    if function_keys.key == pygame.K_ESCAPE :
                        pygame.mixer.Sound.play(map_open)
                    elif function_keys.key == pygame.K_i:
                        pygame.mixer.Sound.play(map_open) 
                           
                    elif function_keys.key == pygame.K_f :
                        pygame.mixer.Sound.play(a)
                    elif function_keys.key == pygame.K_g :
                        pygame.mixer.Sound.play(b)
                    elif function_keys.key == pygame.K_h :
                        pygame.mixer.Sound.play(c)
                    elif function_keys.key == pygame.K_j :
                        pygame.mixer.Sound.play(d)
                    elif function_keys.key == pygame.K_k :
                        pygame.mixer.Sound.play(e)
                    elif function_keys.key == pygame.K_l :
                        pygame.mixer.Sound.play(f)
                    elif function_keys.key == pygame.K_m :
                        pygame.mixer.Sound.play(g)  
                          
                    elif function_keys.key == pygame.K_END:
                        run = False 
                        pygame.quit()

            if anim_count >= 3 :
                anim_count = 0
            else :
                anim_speed += 1
                if anim_speed == 5 :
                    anim_count += 1
                    anim_speed = 0
                pygame.display.flip()
            pygame.display.flip()          
    pygame.display.flip()

            
    