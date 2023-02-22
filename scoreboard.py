import pygame
# 점수와 관련된 전반적인 기능
class ScoreBoard:
  def __init__(self):
    self.score = 0
    self.font = pygame.font.SysFont("Ariel", 30)
    self.scoreText = lambda : f"Score : {self.score}"
    self.gameOverText = "GameOver"
    
  def score_render_text(self, color):
    return self.font.render(self.scoreText(), False, color)
  
  def gameover_render_text(self, color):
    return self.font.render(self.gameOverText, False, color)