import pgzrun
# pgzero

WIDTH = 600  # Ширина окна
HEIGHT = 300  # Высота окна

TITLE = "Инопланетный раннер"  # Заголовок окна игры
FPS = 30  # Количество кадров в секунду

# Объекты
alien = Actor('alien', (50, 240))
fon = Actor("fon")
box = Actor('box', (550, 265))
bee = Actor('bee', (850, 175))  # Пчела


def draw():
    fon.draw()
    alien.draw()
    box.draw()
    bee.draw()


def update(dt):
    # Движение пчелы
    if bee.x > -20:
        bee.x = bee.x - 5
    else:
        bee.x = WIDTH + 20

    # Движение коробки
    if box.x > -20:
        box.x = box.x - 5
        box.angle = box.angle + 5
    else:
        box.x = WIDTH + 20

    # Управление
    if keyboard.left or keyboard.a and alien.x > 20:
        alien.x = alien.x - 5
        alien.image = 'left'
    elif keyboard.right or keyboard.d and alien.x < 580:
        alien.x = alien.x + 5
        alien.image = 'right'
    elif keyboard.down or keyboard.s:
        alien.image = 'duck'
        alien.y = 250
    else:
        alien.image = 'alien'
        if alien.y > 240:
            alien.y = 240


def on_key_down(key):
    # Прыжок
    if keyboard.space or keyboard.up or keyboard.w:
        alien.y = 100
        animate(alien, tween='bounce_end', duration=2, y=240)

pgzrun.go()

