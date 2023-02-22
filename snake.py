import pygame

class Snake_Segment(pygame.Rect):
  def __init__ (self, x,y,w,h):
    super().__init__(x,y,w,h)
    self.size = (w,h)
    self.pos = (x,y)
    

class Snake:
  
  def __init__(self, color=(255,255,255), cnt=3):
    self.snake = [Snake_Segment(320,320,10,10)]
    self.head = self.snake[0]
    self.color = color
    self.now_dir = (1,0)
    self.next_dir = (1,0)
    for _ in range(cnt):
      self.make_segment((self.snake[-1].x-10, self.snake[-1].y))
  
  # 몸체 만들기
  def make_segment(self,pos):
    self.snake.append(Snake_Segment(pos[0], pos[1], self.head.w, self.head.h))
  
  # 뱀 움직이기
  def move(self):
    # 몸통 움직이기
    for i in range(len(self.snake)-1, 0, -1):
      self.snake[i].clamp_ip(self.snake[i-1])
    # 머리 움직이기
    self.now_dir = self.next_dir
    self.head.move_ip(10 * self.now_dir[0] , 10 * self.now_dir[1])
  
  # 모든 몸의 파츠를 반환
  def get_all_segment(self):
    return self.snake
  
  # 먹었을 때 몸이 늘어나게하는 함수
  def extend(self):
    self.make_segment((self.snake[-1].x, self.snake[-1].y))
  
  # 위로 방향전환
  def turn_up(self):
    if self.now_dir != (0,1):
      self.next_dir = (0,-1)
  # 밑으로 방향전환
  def turn_down(self):
    if self.now_dir != (0,-1):
      self.next_dir = (0,1)
  # 왼쪽으로 방향전환    
  def turn_left(self):
    if self.now_dir != (1,0):
      self.next_dir = (-1,0)
  # 오른쪽으로 방향전환    
  def turn_right(self):
    if self.now_dir != (-1,0):
      self.next_dir = (1,0)
  
  # TODO
  # 몸이랑 머리랑 부딪히면 게임오버 처리