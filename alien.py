import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from class_stats import GameStats
from scoreboard import ScoreBoard
from botton import Button
from ship import Ship
import functions as f
from al import Alien


def run_game():
	#Инициализация игры и создание экрана
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, 
									ai_settings.screen_height))
	pygame.display.set_caption("Alien War")
	play_button = Button(ai_settings, screen, "Play")
	stats = GameStats(ai_settings)
	sb = ScoreBoard(ai_settings, screen, stats)
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	f.create_fleet(ai_settings, screen, ship, aliens)
	# Назначение цвета фона
	bg_color = (100, 100, 100)
	alien = Alien(ai_settings, screen)
	while True:
		f.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			f.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			f.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
		f.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
		
run_game()
