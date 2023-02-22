import pygame
import sys
import random as rd
from food import Food
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
food = Food(rd.randint(10, 600), rd.randint(10, 600), 5, 5)

game_on = True


while game_on:
  screen.fill(BLACK)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    # 키 입력 처리
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
  
  # 먹을거 렌더링
  pygame.draw.rect(screen, food.color, food)
  
  # TODO
  # 뱀이 벽에 닿으면 게임오버 처리, 판정이 좀 더 여유롭게 적용
  # 자기 자신을 물었는지도 체크해야함
  if (snake.head.x < 0 or snake.head.x > 640) or (snake.head.y < 0 or snake.head.y > 640) or snake.bite_is_self():
    for sg in snake.get_all_segment():
      pygame.draw.rect(screen, RED, sg)
    game_on = False
  
  # 음식 충돌 체크
  if snake.head.colliderect(food):
    food.respawn()
    snake.extend()
  
  # 점수 처리
  
  pygame.display.update()
  clock.tick(FPS)
  
# 게임오버 용 while문
while True:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      # 마우스 왼쪽 클릭시 종료
      if pygame.mouse.get_pressed()[0]:
        pygame.quit()
        sys.exit()