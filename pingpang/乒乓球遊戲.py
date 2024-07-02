import pygame
from ball import Ball
from paddle import Paddle

def paddle_move(keys,left_paddle,right_paddle):
    if keys[pygame.K_UP]:
        right_paddle.update(True,height)
    if keys[pygame.K_DOWN]:
        right_paddle.update(False,height)
    if keys[pygame.K_w]:
        left_paddle.update(True,height)
    if keys[pygame.K_s]:
        left_paddle.update(False,height)

def draw_score(window,left_score,right_score):
    left_score_text = score_font.render(f"{left_score}",True,white)
    right_score_text = score_font.render(f"{right_score}",True,white)
    window.blit(left_score_text,(100,20))
    window.blit(right_score_text,(width-100-right_score_text.get_width(),20))

black = (0,0,0)
white = (255,255,255)
width = 700
height = 500
FPS = 60

pygame.init()
window = pygame.display.set_mode((width,height))  
pygame.display.set_caption("乒乓球") 

score_font = pygame.font.Font("微軟正黑體.ttf", 50)

ball = Ball(width/2,height/2,7,white)
#ball1 = Ball(100,100,10, (255,0,0))
#ball2 = Ball(300,300,10, (0,255,0))
paddle_width = 15
paddle_height = 100
left_paddle = Paddle(10,height/2-paddle_height/2,paddle_width,paddle_height,white)
right_paddle = Paddle(width-10-paddle_width,height/2-paddle_height/2,paddle_width,paddle_height,white)



clock = pygame.time.Clock()   
run = True
while run:
    # 取得輸入
    clock.tick(FPS)  
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:  
            run = False
    #    elif event.type == pygame.KEYDOWN:
    #       if event.key == pygame.K_UP:
    #          y -= 4
    #     elif event.key == pygame.K_DOWN:
    #        y += 4           

    keys = pygame.key.get_pressed()
    paddle_move(keys,left_paddle,right_paddle)
    
    # 遊戲更新
    ball.update(width,height,left_paddle,right_paddle)
    ball.check_collide(left_paddle,right_paddle)
    #ball1.update(width,height)
    #ball2.update(width,height)
    
    
    # 畫面顯示
    window.fill(black)  
    ball.draw(window)
    #ball1.draw(window)
    #ball2.draw(window)
    left_paddle.draw(window)
    right_paddle.draw(window)
    draw_score(window,left_paddle.score,right_paddle.score)
    pygame.display.update() #告知遊戲設定可以顯示了

pygame.quit()