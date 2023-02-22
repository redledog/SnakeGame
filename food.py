import pygame
import random as rd
# 위치가 랜덤으로 나와야함
# 먹으면 다시 랜덤으로 재배치

class Food(pygame.Rect):
  def __init__(self, x, y, w, h, color = (0,255,255)):
    super().__init__(x,y,w,h)
    self.color = color
    
  # 재배치
  def respawn(self):
    self.update(self.w, self.h, rd.randint(10, 600), rd.randint(10, 600))