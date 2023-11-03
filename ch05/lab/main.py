import pygame


def threenp1(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count = count + 1
    return count

def threenp1range(upper_limit):
    objs_in_sequence = {}
    for n in range(2, upper_limit + 1):
        iters = threenp1(n)
        objs_in_sequence[n] = iters
    return objs_in_sequence

def display_graph(data):
    max_value = max(data.values())
    max_iterations_number = [k for k, v in data.items() if v == max_value]

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(None, 36)
    label = font.render("Max iterations: {}".format(max_value), 1, (255, 255, 255))
    screen.blit(label, (50, 50))

    max_width = max(data.keys())
    for num, iterations in data.items():
        pygame.draw.line(screen, (255, 255, 255), (50 + num * 10, 500 - iterations * 10), (50 + num * 10, 500))

    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    upper_limit = 1000
    data = threenp1range(upper_limit)
    display_graph(data)