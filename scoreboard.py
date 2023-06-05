import pygame

# 점수와 관련된 전반적인 기능
class ScoreBoard:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont("Ariel", 30)
        self.scoreText = lambda: f"Score : {self.score}"
        self.gameOverText = "GameOver"

    def score_render_text(self, color):
        surface = self.font.render(self.scoreText(), False, color)
        return surface

    def gameover_render_text(self, color):
        surface = self.font.render(self.gameOverText, False, color)
        return surface
    
    # 재시작 텍스트가 그려져있는 surface 객체를 반환해주는 함수
    def render_restart_text(self, color):
        surface = self.font.render("Press left mouse button...", False, color)
        return surface
