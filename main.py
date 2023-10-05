from termcolor import colored
from appstrings import STR as S
from database.project import Project

def prc(text, color='light_green', bold=True):
  """Available text colors:
    black, red, green, yellow, blue, magenta, cyan, white, 
    light_grey, dark_grey, light_red, light_green, light_yellow, 
    light_blue, light_magenta, light_cyan."""
  print(colored(text, color, attrs=["bold"]))

def welcome():
  prc(S.LINE)
  prc(S.WELCOME)
  prc(S.VERSION)
  prc(S.LINE)

def init():
  Project.create_table()
  


def main():
  welcome()
  init()
  n = input ('Enter your name: ')
  prc(f'Hello {n}!')



  



if __name__ == "__main__":
  main()
