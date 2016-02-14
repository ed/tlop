import pygame
import sys

def num_gen(n):
    num = 1
    while num < n:
        s = num*115 + 65
        yield s
        num = num+1


def num_gen2(n):
    num = 0
    while num < n:
        s = 968 + num*48 - num
        yield s
        num = num+1


def string_gen(background, font, s, last_word, n):
    itr = num_gen(n)
    for i in range (2, n):
        j = next(itr)
        text = font.render(s, 1, (10, 10, 10))
        background.blit(text, (222, j))
        text = font.render(last_word, 1, (10, 10, 10))
        background.blit(text, (922, j))


def string_gen2(background, font, s, n):
    itr = num_gen2(n)
    for i in range (1, n):
        j = next(itr)
        text = font.render(s, 1, (10, 10, 10))
        background.blit(text, (186, j))
        background.blit(text, (1005, j))


   
def initialize_font(default_font_size, s, tw, th):
    font = pygame.font.Font(None, default_font_size)
    text_w, text_h = font.size(s)
    if text_w >= tw or text_h >= th:
        font = pygame.font.Font(None, font_reducer(s, default_font_size, text_w, text_h, tw, th))
    elif text_w < tw or text_h < th:
        font = pygame.font.Font(None, font_adder(s, default_font_size, text_w, text_h, tw, th))
    else:
        font = pygame.font.Font(None, default_font_size)
    return font


def font_reducer(s, font_size, text_w, text_h,tw,th):
    while True:
        if (text_w <= tw or text_h <= th):
            break
        else:
            font_size = font_size - 1
            font = pygame.font.Font(None, font_size)
            text_w, text_h = font.size(s)
    return(font_size)


def font_adder(s, font_size, text_w, text_h,tw,th):
    while True:
        if (text_w >= tw or text_h >= th):
            break
        else:
            font_size = font_size + 1
            font = pygame.font.Font(None, font_size)
            text_w, text_h = font.size(s)
    return(font_size)


# #initialize
pygame.init()
screen = pygame.display.set_mode((1500,1500))
background = pygame.image.load("background.png").convert()

# first string
input_string = sys.argv[1]
input_string = input_string.upper()
string = input_string.rsplit(' ', 1)[0]
last_word = input_string.rsplit(' ', 1)[-1]
img1 = pygame.image.load("img1.png")
img2 = pygame.image.load("img2.png")

# second string
second_string = sys.argv[2]
second_string = second_string.upper()


first_space = "      "
second_space = "  "
third_space= "     "


# First Line
string_1 = string + "%s" % (first_space)
font = initialize_font(136, string_1, 577, 94)
text = font.render(string_1, 1, (10, 10, 10))
background.blit(text, (223,65))
text = font.render(last_word, 1, (10, 10, 10))
background.blit(text, (1028,65))

# generator for next 6
string_2 = string + "%s" % (second_space)
string_gen(background, font, string_2, last_word, 7)

# img 1
background.blit(pygame.transform.scale(img1, (605,425)), (305,447))

# last line of first string 
string_3 = string + "%s" % (third_space)
font = initialize_font(136, string_1, 577, 94)
text = font.render(string_3, 1, (10, 10, 10))
background.blit(text, (222,875))
text = font.render(last_word, 1, (10, 10, 10))
background.blit(text, (966,875))

# second string start
font = initialize_font(54, second_string, 241, 38)

# generator for next 11
string_gen2(background, font, second_string, 11)

background.blit(pygame.transform.scale(img2, (415,352)), (662,1044))
pygame.image.save(background, "output.png")

