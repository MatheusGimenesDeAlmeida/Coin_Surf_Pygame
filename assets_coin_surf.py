import pygame
import os
from config_coin_surf import SHARPEDO_WIDTH, SHARPEDO_HEIGHT, PIKACHU_WIDTH, PIKACHU_HEIGHT, MOEDA_AMARELA_WIDTH, MOEDA_VERDE_WIDTH, MOEDA_VERMELHA_WIDTH, MOEDA_AMARELA_HEIGHT, MOEDA_VERDE_HEIGHT, MOEDA_VERMELHA_HEIGHT, IMG_DIR, WIDTH, HEIGHT, FNT_DIR, SHARPEDO_BOOST_WIDTH, SHARPEDO_BOOST_HEIGHT, PIKACHU_BOOST_WIDTH, PIKACHU_BOOST_HEIGHT

BACKGROUND = 'onda_coin_surf.jpg'
BACKGROUND2 = 'onda_tarde_coin_surf'
BACKGROUND3 = 'onda_noite__coin_surf'
SHARPEDO_IMG = 'sharpedo_coin_surf'
SHARPEDO_BOOST_IMG = 'sharpedo_boost_coin_surf'
PIKACHU_IMG = 'pikachu_coin_surf'
PIKACHU_BOOST_IMG = 'pikachu_boost_coin_surf'
MOEDA_AMARELA_IMG = 'moeda_amarela_coin_surf'
MOEDA_VERDE_IMG = 'moeda_verde_coin_surf'
MOEDA_VERMELHA_IMG = 'moeda_vermelha_coin_surf'
SCORE_FONT = 'score_font'

pygame.display.init()
pygame.font.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'onda_coin_surf.jpg')).convert()
    assets[BACKGROUND] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))
    assets[BACKGROUND2] = pygame.image.load(os.path.join(IMG_DIR, 'onda_tarde_coin_surf.jpg')).convert()
    assets[BACKGROUND2] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))
    assets[BACKGROUND3] = pygame.image.load(os.path.join(IMG_DIR, 'onda_noite__coin_surf.jpg')).convert()
    assets[BACKGROUND3] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))
    assets[SHARPEDO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'sharpedo_coin_surf.png')).convert_alpha()
    assets[SHARPEDO_IMG] = pygame.transform.scale(assets[SHARPEDO_IMG], (SHARPEDO_WIDTH, SHARPEDO_HEIGHT))
    assets[SHARPEDO_BOOST_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'sharpedo_boost_coin_surf.png')).convert_alpha()
    assets[SHARPEDO_BOOST_IMG] = pygame.transform.scale(assets[SHARPEDO_IMG], (SHARPEDO_BOOST_WIDTH, SHARPEDO_BOOST_HEIGHT))
    assets[PIKACHU_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'pikachu_coin_surf.png')).convert_alpha()
    assets[PIKACHU_IMG] = pygame.transform.scale(assets[PIKACHU_IMG], (PIKACHU_WIDTH, PIKACHU_HEIGHT))
    assets[PIKACHU_BOOST_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'pikachu_boost_coin_surf.png')).convert_alpha()
    assets[PIKACHU_BOOST_IMG] = pygame.transform.scale(assets[PIKACHU_IMG], (PIKACHU_BOOST_WIDTH, PIKACHU_BOOST_HEIGHT))
    assets[MOEDA_AMARELA_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'moeda_amarela_coin_surf.png')).convert_alpha()
    assets[MOEDA_AMARELA_IMG] = pygame.transform.scale(assets[MOEDA_AMARELA_IMG], (MOEDA_AMARELA_WIDTH, MOEDA_AMARELA_HEIGHT))
    assets[MOEDA_VERDE_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'moeda_verde_coin_surf.png')).convert_alpha()
    assets[MOEDA_VERDE_IMG] = pygame.transform.scale(assets[MOEDA_VERDE_IMG], (MOEDA_VERDE_WIDTH, MOEDA_VERDE_HEIGHT))
    assets[MOEDA_VERMELHA_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'moeda_vermelha_coin_surf.png')).convert_alpha()
    assets[MOEDA_VERMELHA_IMG] = pygame.transform.scale(assets[MOEDA_VERMELHA_IMG], (MOEDA_VERMELHA_WIDTH, MOEDA_VERMELHA_HEIGHT))
    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)
    return assets

assets = load_assets()
print(assets)