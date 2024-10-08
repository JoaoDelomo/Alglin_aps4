import pygame
import numpy as np
import math

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pygame.mixer.music.load('Pink Floyd - Another Brick in the Wall (lyrics).mp3')

cube_vertices = np.array([[-1, -1, -1],
                          [-1, -1,  1],
                          [-1,  1, -1],
                          [-1,  1,  1],
                          [ 1, -1, -1],
                          [ 1, -1,  1],
                          [ 1,  1, -1],
                          [ 1,  1,  1]])

cube_edges = [(0, 1), (0, 2), (0, 4), (1, 3), (1, 5),
              (2, 3), (2, 6), (3, 7), (4, 5), (4, 6),
              (5, 7), (6, 7)]

prism_vertices = np.array([[0, 1, 0],
                           [-1, -1, -1],
                           [1, -1, -1],
                           [1, -1, 1],
                           [-1, -1, 1]])

prism_edges = [(0, 1), (0, 2), (0, 3), (0, 4),
               (1, 2), (2, 3), (3, 4), (4, 1)]

def rotate_x(vertices, theta):
    rotation_matrix = np.array([[1, 0, 0],
                                [0, math.cos(theta), -math.sin(theta)],
                                [0, math.sin(theta), math.cos(theta)]])
    return np.dot(vertices, rotation_matrix)

def rotate_y(vertices, theta):
    rotation_matrix = np.array([[math.cos(theta), 0, math.sin(theta)],
                                [0, 1, 0],
                                [-math.sin(theta), 0, math.cos(theta)]])
    return np.dot(vertices, rotation_matrix)

def rotate_z(vertices, theta):
    rotation_matrix = np.array([[math.cos(theta), -math.sin(theta), 0],
                                [math.sin(theta), math.cos(theta), 0],
                                [0, 0, 1]])
    return np.dot(vertices, rotation_matrix)

def project(vertices, screen_width, screen_height, fov, distance):
    projected_vertices = []
    for vertex in vertices:
        x, y, z = vertex
        factor = fov / (distance + z)
        x = x * factor + screen_width / 2
        y = -y * factor + screen_height / 2
        projected_vertices.append([x, y])
    return projected_vertices

def draw_rainbow(screen, start_pos):
    rainbow_colors = [
        (255, 0, 0),
        (255, 127, 0),
        (255, 255, 0),
        (0, 255, 0),
        (0, 0, 255),
        (75, 0, 130),
        (148, 0, 211)
    ]
    
    for i, color in enumerate(rainbow_colors):
        pygame.draw.line(screen, color, start_pos, (800, 300 + i * 5), 3)

def main():
    angle_x = 0
    angle_y = 0
    angle_z = 0
    fov = 400
    distance = 5
    shape = 'cube'
    music_playing = False
    light_beam_active = False

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_c]:
            shape = 'cube'
            pygame.mixer.music.stop()
            music_playing = False
            light_beam_active = False
        if keys[pygame.K_p]:
            shape = 'prism'

        if keys[pygame.K_l]:
            light_beam_active = not light_beam_active
            if light_beam_active and not music_playing:
                pygame.mixer.music.play(-1)
                music_playing = True
            elif not light_beam_active:
                pygame.mixer.music.stop()
                music_playing = False

        if keys[pygame.K_LEFT]:
            angle_y -= 0.05
        if keys[pygame.K_RIGHT]:
            angle_y += 0.05
        if keys[pygame.K_UP]:
            angle_x -= 0.05
        if keys[pygame.K_DOWN]:
            angle_x += 0.05
        if keys[pygame.K_w]:
            distance -= 0.1
        if keys[pygame.K_s]:
            distance += 0.1

        if shape == 'cube':
            vertices = cube_vertices
            edges = cube_edges
        elif shape == 'prism':
            vertices = prism_vertices
            edges = prism_edges

        rotated_vertices = rotate_x(vertices, angle_x)
        rotated_vertices = rotate_y(rotated_vertices, angle_y)
        rotated_vertices = rotate_z(rotated_vertices, angle_z)

        projected_vertices = project(rotated_vertices, 800, 600, fov, distance)

        for edge in edges:
            points = []
            for vertex in edge:
                points.append(projected_vertices[vertex])
            pygame.draw.line(screen, (255, 255, 255), points[0], points[1], 2)

        if light_beam_active and shape == 'prism':
            light_entry = [(projected_vertices[1][0] + projected_vertices[2][0]) / 2,
                           (projected_vertices[1][1] + projected_vertices[2][1]) / 2]
            light_exit = [(projected_vertices[3][0] + projected_vertices[4][0]) / 2,
                          (projected_vertices[3][1] + projected_vertices[4][1]) / 2]
            
            pygame.draw.line(screen, (255, 255, 255), (0, 300), light_entry, 3)
            draw_rainbow(screen, light_exit)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
