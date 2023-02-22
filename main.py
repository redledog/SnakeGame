import pygame
import sys

from snake import Snake

FPS = 15

## 컬러 세팅 ##
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

pygame.init()
pygame.display.set_caption("Snake Game")
screen = pygame.display.set_mode(size=(640, 640))

clock = pygame.time.Clock()

snake = Snake(WHITE)

game_on = True

while game_on:
  screen.fill(BLACK)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_on = False
    if event.type == pygame.KEYDOWN:
      keys = pygame.key.get_pressed()
      if keys[pygame.K_w]:
        snake.turn_up()
      elif keys[pygame.K_s]:
        snake.turn_down()
      elif keys[pygame.K_a]:
        snake.turn_left()
      elif keys[pygame.K_d]:
        snake.turn_right()
  snake.move()
  
  # 뱀 렌더링
  for sg in snake.get_all_segment():
    pygame.draw.rect(screen, snake.color, sg)
  
  # TODO
  # 뱀이 벽에 닿으면 게임오버 처리
  # 음식 추가
  # 점수 처리
  
  pygame.display.update()
  clock.tick(FPS)
  
pygame.quit()
sys.exit()