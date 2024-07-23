from UtilTestcases import test_number_to_pair,test_pair_to_number #renamed 
from ConsoleOutputDisplay import display_output
from ColorGuide import build_color_guide

if __name__ == '__main__':
  test_number_to_pair(4, 'White', 'Brown')
  test_number_to_pair(5, 'White', 'Slate')
  test_pair_to_number('Black', 'Orange', 12)
  test_pair_to_number('Violet', 'Slate', 25)
  test_pair_to_number('Red', 'Orange', 7)
  display_output('Done :)')
  manual=build_color_guide()
  display_output(manual)
