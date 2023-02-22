import pygame
import random as rd
# 위치가 랜덤으로 나와야함
# 먹으면 다시 랜덤으로 재배치

class Food(pygame.Rect):
  def __init__(self, pos, w, h, color = (0,255,255)):
    super().__init__(pos[0], pos[1], w, h)
    self.color = color
    
  # 재배치
  # 좌표를 받아오도록
  def respawn(self, pos):
    self.update(pos[0], pos[1], self.w, self.h)