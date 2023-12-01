import os

import pygame
from pygame import font

import config


def draw_text(text: str, x: int, y: int, surface: pygame.Surface, color: (int, int, int) = (0, 0, 0), size: int = 30):
    """
    Zeichnet einen Text auf einen Untergrund
    :return:
    """

    # Wir nutzen Arial, das auf Linux, Mac und Windows vorhanden ist.
    writer = font.SysFont(config.FONT, size)
    text_obj = writer.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)


def get_highscore_from_file() -> [(str, int)]:
    """
    Lädt die lokal gespeicherten Highscores und stellt sie als Liste dar
    """
    csv_file = os.path.join("Highscore.csv")

    highscore_list: [(str, int)] = []

    try:
        highscore_file = open(csv_file, "r")
    except:
        highscore_file = None

    if not highscore_file is None:
        for line in highscore_file:
            score = line.split(";")
            highscore_list.append((score[0], int(score[1])))

        highscore_file.close()

    return highscore_list


def get_persistent_highscore() -> int:
    """
    Lädt die lokal gespeicherten Highscores und gibt den höchsten Wert zurück.
    """
    highscores = get_highscore_from_file()

    highest_score = 0
    for score in highscores:
        if score[1] > highest_score:
            highest_score = score[1]

    return highest_score


def build_highscore_list() -> [(str, int)]:
    """
    Diese Funktion lädt die Highscores aus der Datei und stellt sie als Liste dar. In Vorbereitung auf eine weltweite
    Highscoreliste, verfügt sie bereits über eine Abfrage, ob die Highscoreliste lokal oder global geladen werden soll.
    Derzeit ist dies jedoch immer lokal.
    """
    use_internet_highscore = False
    highscore_list = []

    if use_internet_highscore:
        # to be done
        pass
    else:
        highscore_list = get_highscore_from_file()

    # Highscore liste absteigend sortieren
    highscore_list.sort(key=lambda x: x[1], reverse=True)

    return highscore_list


def write_highscore_to_file(player_name, player_score):
    """
    Schreibt den Highscore in die Datei Highscore.csv
    """
    # Name und Punktezahl wird an die Highscoredatei angehängt
    file_name = "Highscore.csv"
    highscore_file = open(file_name, "a")
    highscore_file.write(player_name + ";" + player_score + "\n")
    highscore_file.close()

    return True


def check_input_char(e: pygame.event.Event) -> bool:
    """
    Prüft für ein Event, ob es sich um eine erlaubte Taste handelt.
    """
    return e.key in range(pygame.K_a, pygame.K_z + 1) or e.key in range(pygame.K_0,
                                                                        pygame.K_9 + 1) or e.key == pygame.K_SPACE
