import random

import pygame

import config
import settings
from Entities import Cat, Dog, delivery, pizza
from System import collisions
from System.sounds import SoundManager
from UI import hearts, pause_menu, restart_menu
from UI import score as score_ui


class Game:
    def __init__(self):
        """Constructor: crea la ventana, inicializa sonidos y arranca la primera partida."""
        self.playing = True
        self.clock = pygame.time.Clock()

        config.pantalla = pygame.display.set_mode(settings.WINDOW_SIZE, pygame.FULLSCREEN)
        pygame.display.set_caption(settings.TITLE)
        pygame.display.set_icon(config.icon)

        pygame.mixer.init()
        self.sounds = SoundManager()
        self.sounds.play_background_music()

        self._start_new_run()

    # ------------------------------------------------------------------
    # Ciclo de vida de una partida
    # ------------------------------------------------------------------
    def _start_new_run(self):
        """Reinicia todo el estado necesario para empezar (o reiniciar) una partida."""
        config.delivery_pos_x = settings.WINDOW_SIZE[0] / 2 - settings.DELIVERY_SIZE[0] / 2
        config.delivery_pos_y = settings.WINDOW_SIZE[1] - settings.DELIVERY_SIZE[1] - 10
        config.delivery_change_pos_x = 0
        config.delivery_change_pos_y = 0
        config.delivery_lives = settings.DELIVERY_LIVES
        config.delivery_last_hit_time = 0

        config.pizzas = []
        config.last_pizza_throw = 0

        config.score = 0
        config.game_paused = False
        config.game_over = False

        self.enemies = [Dog(), Cat()]
        self.last_extra_spawn_time = pygame.time.get_ticks()

    def run(self):
        """Bucle principal del juego: maneja eventos, actualiza y dibuja."""
        while self.playing:
            self.handle_events()
            self.update()
            self.draw()

            pygame.display.flip()
            self.clock.tick(settings.FPS)
            pygame.display.set_caption(f"{settings.TITLE} - FPS: {self.clock.get_fps():.2f}")

    # ------------------------------------------------------------------
    # Eventos
    # ------------------------------------------------------------------
    def handle_events(self):
        """Maneja las entradas de teclado y ratón para interactuar con la UI."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                continue

            if event.type == pygame.KEYDOWN:
                self._handle_keydown(event)
                continue

            if event.type == pygame.KEYUP and not config.game_paused:
                delivery.reset_delivery_movement(event.key)
                continue

            if event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_mouse_click(event)

    def _handle_keydown(self, event):
        """ESC pausa/reanuda el juego (deshabilitado en game over); si no está
        pausado, delega el movimiento del repartidor."""
        if event.key == pygame.K_ESCAPE and not config.game_over:
            config.game_paused = not config.game_paused
            return

        if not config.game_paused:
            delivery.get_delivery_movement(event.key)

    def _handle_mouse_click(self, event):
        """Redirige el click al menú que corresponda, o a la acción de jugar."""
        if config.game_over:
            self._handle_restart_menu_click(event)
        elif config.game_paused:
            self._handle_pause_menu_click(event)
        else:
            self._handle_gameplay_click(event)

    def _handle_restart_menu_click(self, event):
        """Procesa un click sobre el menú de reinicio (game over)."""
        if event.button != 1:  # solo clic izquierdo
            return

        accion = restart_menu.handle_restart_menu_click(event.pos)
        if accion == "reiniciar":
            self._start_new_run()
        elif accion == "salir":
            self.playing = False
        elif accion == "traje":
            ...  # Cambiar de traje (no implementado)

    def _handle_pause_menu_click(self, event):
        """Procesa un click sobre el menú de pausa."""
        if event.button != 1:  # solo clic izquierdo
            return

        accion = pause_menu.handle_menu_click(event.pos)
        if accion == "reanudar":
            config.game_paused = False
        elif accion == "salir":
            self.playing = False
        elif accion == "traje":
            ...  # Cambiar de traje (no implementado)

    def _handle_gameplay_click(self, event):
        """Procesa un click durante el juego: lanzar pizza o poder especial."""
        if event.button == 1:  # clic izquierdo: lanzar pizza
            pizza_lanzada = pizza.launch_pizza(event.pos)
            if pizza_lanzada:
                self.sounds.play_sound("pizza_throw")
        elif event.button == 2:  # clic central: poder especial
            ...  # Poder especial del repartidor en el suelo (no implementado)

    # ------------------------------------------------------------------
    # Update
    # ------------------------------------------------------------------
    def update(self):
        """Actualiza la lógica del juego. No hace nada si está pausado (o en game over)."""
        if config.game_paused:
            return

        delivery.delivery_restrictions()
        delivery.move_delivery()

        pizza.move_pizzas()
        pizza.remove_offscreen_pizzas()

        self._spawn_extra_enemies()
        self._update_enemies()
        self._check_game_over()

    def _spawn_extra_enemies(self):
        """
        Agrega un enemigo nuevo (perro o gato al azar) cada
        EXTRA_ENEMY_SPAWN_INTERVAL ms, hasta llegar a MAX_ENEMIES.
        No espera a que los enemigos anteriores mueran: se acumulan.
        """
        if len(self.enemies) >= settings.MAX_ENEMIES:
            return

        ahora = pygame.time.get_ticks()
        if ahora - self.last_extra_spawn_time < settings.EXTRA_ENEMY_SPAWN_INTERVAL:
            return

        self.last_extra_spawn_time = ahora
        enemigo_nuevo = random.choice([Dog, Cat])()
        self.enemies.append(enemigo_nuevo)

    def _update_enemies(self):
        """Mueve/respawnea a cada enemigo y resuelve sus colisiones."""
        for enemy in self.enemies:
            enemy.update()
            collisions.resolve_pizza_enemy_collisions(enemy, self.sounds)
            collisions.resolve_enemy_delivery_collision(enemy, self.sounds)

    def _check_game_over(self):
        """Si el repartidor se queda sin vidas, pausa el juego y activa el game over."""
        if config.delivery_lives <= 0:
            config.game_over = True
            config.game_paused = True

    # ------------------------------------------------------------------
    # Draw
    # ------------------------------------------------------------------
    def draw(self):
        """Dibuja todos los elementos del juego en la pantalla."""
        config.pantalla.blit(config.background, config.window_origin)
        delivery.draw_delivery(config.delivery_pos_x, config.delivery_pos_y)
        pizza.draw_pizzas()
        hearts.draw_hearts()
        score_ui.draw_score()

        for enemy in self.enemies:
            enemy.draw()

        if config.game_over:
            restart_menu.draw_restart_menu()
        elif config.game_paused:
            pause_menu.draw_pause_menu()

        pygame.display.update()