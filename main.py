import pygame
import neat
import time
import os

import img
from bird import Bird
from base import Base
from pipe import Pipe

pygame.font.init()
GENERATION = 0
STAT_FONT = pygame.font.SysFont("comicsans", 50)

def draw_window(win,birds, pipes, base, score, generation):
    win.blit(img.BG_IMG, (0,0))
    
    for pipe in pipes:
        pipe.draw(win)
    
    base.draw(win)

    for bird in birds:
        bird.draw(win)

    text = STAT_FONT.render("Score: " + str(score), 1, (255,255,255))
    win.blit(text, (img.WIN_WIDTH - 10 - text.get_width(), 10))

    text = STAT_FONT.render("Gen: " + str(generation), 1, (255,255,255))
    win.blit(text, (10, 10))

    pygame.display.update()

def main(genomes, config):
    global GENERATION
    GENERATION += 1
    nets = [] #nets control each bird
    ge = [] #genomes
    birds = [] #each bird

    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config) #generate a net
        nets.append(net)
        birds.append(Bird(230,350))
        genome.fitness = 0 #starting fitness = 0
        ge.append(genome)
    

    #bird = Bird(230,350)
    base = Base(img.WIN_HEIGHT - 70)
    pipes = [Pipe(700)]
    win = pygame.display.set_mode((img.WIN_WIDTH,img.WIN_HEIGHT))
    clock = pygame.time.Clock()

    score = 0
    running = True

    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
        
        pipe_index = 0 # the pipe we should check for inputs for the birds, there can be more than 1 pipe on screen
        #if the birds pass the first pipe, they should consider the inputs of the second one instead
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP_IMG.get_width():
                pipe_index = 1
        else:
            running = False
            break

        for bird_index, bird in enumerate(birds):
            bird.move()
            ge[bird_index].fitness += 0.1 # 30 for each second (30 fps)
            output = nets[bird_index].activate((bird.y, abs(bird.y - pipes[pipe_index].height), abs(bird.y - pipes[pipe_index].height_bottom)))

            if output[0] > 0.5: # if the value of the output neuron is > 0.5 we jump
                bird.jump()


        pipes_to_remove = []
        add_pipe = False # should we add a new pipe to the game?
        for pipe in pipes:
            for bird_index, bird in enumerate(birds):
                if pipe.collide(bird):
                   ge[bird_index].fitness -= 1  # if a bird hits a pipe, reduce fitness by 1
                   birds.pop(bird_index)
                   nets.pop(bird_index)
                   ge.pop(bird_index) # ????

                if not pipe.completed and pipe.x < bird.x:
                    pipe.completed = True
                    add_pipe = True

            if pipe.x + pipe.PIPE_TOP_IMG.get_width() < 0:
                    pipes_to_remove.append(pipe)
            
            pipe.move()
        
        if add_pipe:
            score += 1
            for genome in ge:
                genome.fitness += 5
            pipes.append(Pipe(700))
        
        for pipe in pipes_to_remove:
            pipes.remove(pipe)
        
        for bird_index, bird in enumerate(birds):
            #print(bird.y + bird.img.get_height(), img.WIN_HEIGHT - 75)
            if bird.y + bird.img.get_height() >= (img.WIN_HEIGHT - 75):
                #print("bird hit the bottom")
                birds.pop(bird_index)
                nets.pop(bird_index)
                ge.pop(bird_index)
            
            elif (bird.y <= 0 ):
                #print("bird hit the top")
                birds.pop(bird_index)
                nets.pop(bird_index)
                ge.pop(bird_index)

        
        base.move()
        draw_window(win,birds,pipes,base,score, GENERATION)


#main()

def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    #generate population
    population = neat.Population(config)

    #reporter in terminal
    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)

    #50 generations
    winner = population.run(main,50)

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'neat-config.txt')
    run(config_path)