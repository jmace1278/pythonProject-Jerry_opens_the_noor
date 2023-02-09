import pygame

pygame.init()

# Create the screen
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jerry opens the noor")
pygame.display.flip()

# Defining game variables
Current_level = 0
Level_passed = False
tile_size = 50
clock = pygame.time.Clock()

# Loading images and colours

wall_img = pygame.image.load("Wall.png")
air_img = pygame.image.load("NOTHING.png")
Home_Screen_img = pygame.image.load("Title_Screen.png")
End_Screen_img = pygame.image.load("end_screen.png")
start_button_img = pygame.image.load("start_button.png")
exit_button_img = pygame.image.load("exit_button.png")
restart_button_img = pygame.image.load("restart_button.png")
character_img = pygame.image.load("Face1.png")
enemy_img = pygame.image.load("Enemy.png")
Sight_radius_img = pygame.image.load("Sight radius.png")
Sight_radius_large_img = pygame.image.load("sight radius large.png")
door_img = pygame.image.load("DOOR.png")
key_img = pygame.image.load("Key.png")
white = [255, 255, 255]
black = [0, 0, 0]

# Creating map layouts

world_map1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
world_map2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
world_map3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
world_map4 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
world_map5 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def determine_state():
    global Current_level
    if Current_level == 1:
        current_world = world1.tile_list
        current_player = player1
        current_key = key1
        current_door = door1
        return current_world, current_player, current_key, current_door
    if Current_level == 2:
        current_world = world2.tile_list
        current_player = player2
        current_key = key2
        current_door = door2
        return current_world, current_player, current_key, current_door
    if Current_level == 3:
        current_world = world3.tile_list
        current_player = player3
        current_key = key3
        current_door = door3
        return current_world, current_player, current_key, current_door
    if Current_level == 4:
        current_world = world4.tile_list
        current_player = player4
        current_key = key4
        current_door = door4
        return current_world, current_player, current_key, current_door
    if Current_level == 5:
        current_world = world5.tile_list
        current_player = player5
        current_key = key5
        current_door = door5
        return current_world, current_player, current_key, current_door


# Creating the button_class


class Button:
    def __init__(self, x, y, img, button_type):
        self.button_img = img
        self.rect = self.button_img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.button_type = button_type

    # Creating the button click
    def update(self):
        global Current_level
        global run
        click = pygame.mouse.get_pressed()
        if click[0]:
            mouse_position = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_position[0], mouse_position[1]):
                if self.button_type == "Start":
                    Current_level += 1
                elif self.button_type == "Exit":
                    run = False
                elif self.button_type == "Restart":
                    Current_level = 1
                    player1.rect.x = player1.starting_x
                    player1.rect.y = player1.starting_y
                    player2.rect.x = player2.starting_x
                    player2.rect.y = player2.starting_y
                    player3.rect.x = player3.starting_x
                    player3.rect.y = player3.starting_y
                    player4.rect.x = player4.starting_x
                    player4.rect.y = player4.starting_y
                    player5.rect.x = player5.starting_x
                    player5.rect.y = player5.starting_y
                    key1.rect.x = key1.starting_x
                    key1.rect.y = key1.starting_y
                    key2.rect.x = key2.starting_x
                    key2.rect.y = key2.starting_y
                    key3.rect.x = key3.starting_x
                    key3.rect.y = key3.starting_y
                    key4.rect.x = key4.starting_x
                    key4.rect.y = key4.starting_y
                    key5.rect.x = key5.starting_x
                    key5.rect.y = key5.starting_y
                    key1.picked_up = False
                    key2.picked_up = False
                    key3.picked_up = False
                    key4.picked_up = False
                    key5.picked_up = False
        screen.blit(self.button_img, (self.rect.x, self.rect.y))

# Creating the world_class


class World:
    def __init__(self, world_map):
        self.map = world_map
        self.tile_list = []
        row_count = 0
        for row in self.map:
            col_count = 0
            for col in row:
                if col == 1:
                    img = pygame.transform.scale(wall_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count*tile_size
                    img_rect.y = row_count*tile_size
                    tile = (img, img_rect, 1)
                    self.tile_list.append(tile)
                if col == 0:
                    img = pygame.transform.scale(air_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect, 0)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

# creating the character class


class Character:
    def __init__(self, x, y):
        self.sight_radius = Sight_radius_img
        self.sight_radius.set_colorkey(white)
        self.sight_radius_large = Sight_radius_large_img
        self.sight_radius_large.set_colorkey(white)
        self.character_img = pygame.transform.scale(character_img, (40, 40))
        self.character_img.set_colorkey((34, 177, 76))
        self.rect = self.character_img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.starting_x = x
        self.starting_y = y
        self.dx = 0
        self.dy = 0

    def update(self):
        # Creating movement
        self.dx = 0
        self.dy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            self.dx -= 2
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.dx += 2
        if key[pygame.K_UP] or key[pygame.K_w]:
            self.dy -= 2
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            self.dy += 2

        # Creating collision
        current_state = determine_state()
        for tile in current_state[0]:
            if tile[2] == 3:
                if tile[1].colliderect(self.rect.x, self.rect.y + self.dy, 40, 40):
                    if self.dy < 0:
                        self.dy = tile[1].bottom - self.rect.top
                    if self.dy > 0:
                        self.dy = tile[1].top - self.rect.bottom
                if tile[1].colliderect(self.rect.x + self.dx, self.rect.y, 40, 40):
                    if self.dx < 0:
                        self.dx = tile[1].right - self.rect.left
                    if self.dx > 0:
                        self.dx = tile[1].left - self.rect.right
        self.rect.x += self.dx
        self.rect.y += self.dy

        # outputting to the screen
        screen.blit(self.character_img, (self.rect.x, self.rect.y))
        # outputting sight radius
        if not Current_level == 5:
            screen.blit(self.sight_radius, (self.rect.x-680, self.rect.y-680))
        else:
            screen.blit(self.sight_radius_large, (self.rect.x-680, self.rect.y-680))


# Creating the Door_class
class Door:
    def __init__(self, x, y):
        self.door_img = door_img
        self.rect = self.door_img.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        global Level_passed
        global Current_level
        screen.blit(self.door_img, self.rect)
        current_state = determine_state()
        if current_state[1].rect.colliderect(self.rect.x, self.rect.y, 25, 50) and current_state[2].picked_up:
            if not Level_passed:
                Current_level += 1
                Level_passed = True
        if not current_state[1].rect.colliderect(self.rect.x, self.rect.y, 25, 50):
            Level_passed = False


# creating the Key_class
class Key:
    def __init__(self, x, y):
        self.key_img = key_img
        self.key_img.set_colorkey(white)
        self.rect = self.key_img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.starting_x = x
        self.starting_y = y
        self.picked_up = False

    def update(self):
        current_state = determine_state()
        # Picking up the key
        if current_state[1].rect.colliderect(self.rect.x, self.rect.y, 25, 50):
            self.picked_up = True
        # Making key sprite follow the character
        if self.picked_up:
            if current_state[1].dx < 0:
                self.rect.x = current_state[1].rect.x + 30
            elif current_state[1].dx > 0:
                self.rect.x = current_state[1].rect.x - 20
            self.rect.y = current_state[1].rect.y - 20
        screen.blit(self.key_img, (self.rect.x, self.rect.y))


class Enemy:
    def __init__(self, x, y, direction, speed):
        self.enemy_img = enemy_img
        self.enemy_img = pygame.transform.scale(enemy_img, (40, 40))
        self.enemy_img.set_colorkey((34, 177, 76))
        self.rect = self.enemy_img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx = 0
        self.dy = 0
        self.direction = direction
        self.speed = speed

    def update(self):
        self.dy = 0
        self.dx = 0
        current_state = determine_state()
        if self.direction == "Horizontal":
            self.dx += self.speed
            for tile in current_state[0]:
                if tile[2] == 1:
                    if tile[1].colliderect(self.rect.x + self.dx, self.rect.y, 40, 40):
                        self.speed = -self.speed
        if self.direction == "Vertical":
            self.dy += self.speed
            current_state = determine_state()
            for tile in current_state[0]:
                if tile[2] == 1:
                    if tile[1].colliderect(self.rect.x, self.rect.y + self.dy, 40, 40):
                        self.speed = -self.speed
        self.rect.x += self.dx
        self.rect.y += self.dy
        screen.blit(self.enemy_img, (self.rect.x, self.rect.y))
        if current_state[1].rect.colliderect(self.rect.x, self.rect.y, 40, 40):
            current_state[1].rect.x = current_state[1].starting_x
            current_state[1].rect.y = current_state[1].starting_y
            current_state[2].picked_up = False
            current_state[2].rect.x = current_state[2].starting_x
            current_state[2].rect.y = current_state[2].starting_y


# Defining each level
# Home screen
start_button = Button(100, 350, start_button_img, "Start")
exit_button = Button(100, 500, exit_button_img, "Exit")
# World1
world1 = World(world_map1)
player1 = Character(50, 600)
door1 = Door(600, 50)
key1 = Key(400, 500)
# World2
world2 = World(world_map2)
player2 = Character(50, 600)
door2 = Door(450, 500)
key2 = Key(200, 200)
# World3
world3 = World(world_map3)
player3 = Character(50, 600)
door3 = Door(50, 100)
key3 = Key(500, 100)
enemy3 = Enemy(600, 350, "Horizontal", 3)
# World4
world4 = World(world_map4)
player4 = Character(50, 600)
door4 = Door(600, 200)
key4 = Key(150, 600)
enemy_4 = Enemy(300, 250, "Vertical", 2)
# World5 - Special Room??
world5 = World(world_map5)
player5 = Character(50, 600)
door5 = Door(600, 150)
key5 = Key(150, 150)
enemy5_1 = Enemy(200, 50, "Vertical", 5)
enemy5_2 = Enemy(300, 400, "Vertical", 5)
enemy5_3 = Enemy(400, 200, "Vertical", 5)
# End Screen
exit_button_2 = Button(200, 650, exit_button_img, "Exit")
restart_button = Button(400, 650, restart_button_img, "Restart")

# Running the game
run = True
while run:

    if Current_level == 0:
        screen.blit(Home_Screen_img, (0, 0))
        exit_button.update()
        start_button.update()
    if Current_level == 1:
        world1.draw()
        door1.update()
        key1.update()
        player1.update()
    if Current_level == 2:
        world2.draw()
        door2.update()
        key2.update()
        player2.update()
    if Current_level == 3:
        world3.draw()
        door3.update()
        key3.update()
        enemy3.update()
        player3.update()
    if Current_level == 4:
        world4.draw()
        door4.update()
        key4.update()
        enemy_4.update()
        player4.update()
    if Current_level == 5:
        world5.draw()
        key5.update()
        enemy5_1.update()
        enemy5_2.update()
        enemy5_3.update()
        player5.update()
        door5.update()
        screen.blit(player5.character_img, (player5.rect.x, player5.rect.y))
        screen.blit(player5.sight_radius_large, (player5.rect.x - 680, player5.rect.y - 680))
    if Current_level == 6:
        screen.blit(End_Screen_img, (0, 0))
        exit_button_2.update()
        restart_button.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    clock.tick(60)
pygame.quit()
