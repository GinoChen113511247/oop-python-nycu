import pygame

# 定義 Ball 類別
class Ball:
    def __init__(self, screen, color, radius, pos, velocity):
        self.screen = screen
        self.color = color
        self.radius = radius
        self.pos = pos  # [x, y]
        self.velocity = velocity  # [vx, vy]

    def update_ball(self, screen_width, screen_height):
        # 更新小球位置
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

        # 碰撞判斷：左右邊界
        if self.pos[0] - self.radius <= 0 or self.pos[0] + self.radius >= screen_width:
            self.velocity[0] = -self.velocity[0]

        # 碰撞判斷：上下邊界
        if self.pos[1] - self.radius <= 0 or self.pos[1] + self.radius >= screen_height:
            self.velocity[1] = -self.velocity[1]

    def draw_ball(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)

def main():
    # 初始化 pygame
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("BouncyBall")
    
    # 建立第一顆球：初始位置在畫面中央
    ball1 = Ball(
        screen=screen,
        color=(255, 255, 255),  # 白色
        radius=20,
        pos=[screen_width // 2, screen_height // 2],
        velocity=[3, 3]
    )
    
    # 建立第二顆球：不同顏色、半徑、速度，且初始位置與第一顆球不同
    ball2 = Ball(
        screen=screen,
        color=(255, 0, 0),  # 紅色
        radius=30,
        pos=[screen_width // 4, screen_height // 4],  # 與 ball1 不同的初始位置
        velocity=[4, 2]
    )

    clock = pygame.time.Clock()
    running = True

    # 主迴圈：持續更新與繪製
    while running:
        # 處理事件（例如使用者關閉視窗）
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 清除螢幕（填滿黑色背景）
        screen.fill((0, 0, 0))
        
        # 更新小球的狀態
        ball1.update_ball(screen_width, screen_height)
        ball2.update_ball(screen_width, screen_height)
        
        # 繪製小球
        ball1.draw_ball()
        ball2.draw_ball()

        # 更新畫面
        pygame.display.flip()

        # 控制遊戲迴圈速率
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
