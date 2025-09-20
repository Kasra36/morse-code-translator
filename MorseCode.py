from chart import ALPHA_TO_MORSE, MORSE_TO_ALPHA
import pygame
import time

pygame.mixer.init(frequency=44100)

class MorseCode():
    def __init__(self, prompt):
        self.dot = pygame.mixer.Sound("morse_dot.wav")
        self.dot.set_volume(0.2)
        self.dash = pygame.mixer.Sound("morse_dash.wav")
        self.dash.set_volume(0.2)
        self.output = ''
        self.prompt = prompt
    
    def encoder(self):
        
        for c in self.prompt:
            
            if c.isspace():
                self.output += '/ '
            elif c.upper() in ALPHA_TO_MORSE:
                self.output += ALPHA_TO_MORSE[c.upper()] + ' '
            else:
                 print(f"Warning: character '{c}' is not supported and will be skipped.")
        
        return print(f'Output: {self.output}')

    def decoder(self):
        mc_list = self.prompt.split(' ')
        for i in mc_list:
            if i == '/':
                self.output += ' '
            elif i in MORSE_TO_ALPHA:
                self.output += MORSE_TO_ALPHA[i]
            else:
                 print(f"Warning: character '{i}' is not supported and will be skipped.")
        
        return print(f'Output: {self.output}')

    def player(self):
        unit = 0.15
        for c in self.output:
            if c == '.':
                dot = self.dot.play()
                while dot.get_busy():
                    time.sleep(0.01)
                time.sleep(unit)
            elif c == '-':
                dash = self.dash.play()
                while dash.get_busy():
                    time.sleep(0.01)
                time.sleep(unit)
            elif c == ' ':
                time.sleep(unit*3)
            elif c == '/':
                time.sleep(unit*7)
