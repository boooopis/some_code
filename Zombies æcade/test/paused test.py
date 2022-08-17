def pause():
    loop = 1
    write("PAUSED", 500, 150)
    write("Press Space to continue", 500, 250)
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = 0
                if event.key == pygame.K_SPACE:
                    screen.fill((0, 0, 0))
                    loop = 0
        pygame.display.update()
        # screen.fill((0, 0, 0))
        clock.tick(60)
        
