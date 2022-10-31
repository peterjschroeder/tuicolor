#!/usr/bin/python3
from xdg.BaseDirectory import *
import configparser

os.makedirs(os.path.join(xdg_config_home, "asciimatics"), exist_ok=True)

colors = {
        'default': -1,
        'black': 0,
        'red': 1,
        'green': 2,
        'yellow': 3,
        'blue': 4,
        'magenta': 5,
        'cyan': 6,
        'white': 7
        }

attributes = {
        'bold': 1,
        'normal': 2,
        'reverse': 3,
        'underline': 4
        }

config_defaults_pallette = {
        'background': 'white,normal,blue',
        'borders': 'black,bold,blue',
        'button': 'white,normal,blue',
        'control': 'yellow,normal,blue',
        'disabled': 'black,bold,blue',
        'edit_text': 'white,normal,blue',
        'field': 'white,normal,blue',
        'focus_button': 'white,bold,cyan',
        'focus_control': 'yellow,normal,blue',
        'focus_edit_text': 'white,bold,cyan',
        'focus_field': 'white,normal,blue',
        'focus_readonly': 'black,bold,cyan',
        'invalid': 'yellow,bold,red',
        'label': 'green,bold,blue',
        'readonly': 'black,bold,blue',
        'scroll': 'cyan,normal,blue',
        'selected_control': 'yellow,bold,blue',
        'selected_field': 'yellow,bold,blue',
        'selected_focus_control': 'yellow,bold,cyan',
        'selected_focus_field': 'white,bold,cyan',
        'title': 'white,bold,blue'
        }

config = configparser.ConfigParser()

def config_create():
    config.add_section('pallette')

    for i in config_defaults_pallette:
        config['pallette'][i] = config_defaults_pallette[i]

    with open(os.path.join(xdg_config_home, 'color'), 'w') as configfile:
        config.write(configfile)

if not os.path.exists(os.path.join(xdg_config_home, 'color')):
    config_create()

def config_load(tui):
    config.read(os.path.join(xdg_config_home, 'color'))

    # Check for missing keys
    for i in config_defaults_pallette:
        if not config.has_option('pallette', i):
            config['pallette'][i] = config_defaults_pallette[i]
    with open(os.path.join(xdg_config_home, 'color'), 'w') as configfile:
        config.write(configfile)

    if tui == 'asciimatics':
        from asciimatics.widgets.utilities import THEMES

        THEMES.update({
            "default": {
                'background': (colors[config['pallette']['background'].split(',')[0]], attributes[config['pallette']['background'].split(',')[1]], colors[config['pallette']['background'].split(',')[2]]),
                'borders': (colors[config['pallette']['borders'].split(',')[0]], attributes[config['pallette']['borders'].split(',')[1]], colors[config['pallette']['borders'].split(',')[2]]),
                'button': (colors[config['pallette']['button'].split(',')[0]], attributes[config['pallette']['button'].split(',')[1]], colors[config['pallette']['button'].split(',')[2]]),
                'control': (colors[config['pallette']['control'].split(',')[0]], attributes[config['pallette']['control'].split(',')[1]], colors[config['pallette']['control'].split(',')[2]]),
                'disabled':(colors[config['pallette']['disabled'].split(',')[0]], attributes[config['pallette']['disabled'].split(',')[1]], colors[config['pallette']['disabled'].split(',')[2]]),
                'edit_text': (colors[config['pallette']['edit_text'].split(',')[0]], attributes[config['pallette']['edit_text'].split(',')[1]], colors[config['pallette']['edit_text'].split(',')[2]]),
                'field': (colors[config['pallette']['field'].split(',')[0]], attributes[config['pallette']['field'].split(',')[1]], colors[config['pallette']['field'].split(',')[2]]),
                'focus_edit_text': (colors[config['pallette']['focus_edit_text'].split(',')[0]], attributes[config['pallette']['focus_edit_text'].split(',')[1]], colors[config['pallette']['focus_edit_text'].split(',')[2]]),
                'focus_button':(colors[config['pallette']['focus_button'].split(',')[0]], attributes[config['pallette']['focus_button'].split(',')[1]], colors[config['pallette']['focus_button'].split(',')[2]]),
                'focus_field': (colors[config['pallette']['focus_field'].split(',')[0]], attributes[config['pallette']['focus_field'].split(',')[1]], colors[config['pallette']['focus_field'].split(',')[2]]),
                'focus_readonly':(colors[config['pallette']['focus_readonly'].split(',')[0]], attributes[config['pallette']['focus_readonly'].split(',')[1]], colors[config['pallette']['focus_readonly'].split(',')[2]]),
                'invalid': (colors[config['pallette']['invalid'].split(',')[0]], attributes[config['pallette']['invalid'].split(',')[1]], colors[config['pallette']['invalid'].split(',')[2]]),
                'label': (colors[config['pallette']['label'].split(',')[0]], attributes[config['pallette']['label'].split(',')[1]], colors[config['pallette']['label'].split(',')[2]]),
                'readonly': (colors[config['pallette']['readonly'].split(',')[0]], attributes[config['pallette']['readonly'].split(',')[1]], colors[config['pallette']['readonly'].split(',')[2]]),
                'scroll': (colors[config['pallette']['scroll'].split(',')[0]], attributes[config['pallette']['scroll'].split(',')[1]], colors[config['pallette']['scroll'].split(',')[2]]),
                'selected_field': (colors[config['pallette']['selected_field'].split(',')[0]], attributes[config['pallette']['selected_field'].split(',')[1]], colors[config['pallette']['selected_field'].split(',')[2]]),
                'selected_focus_control': (colors[config['pallette']['selected_focus_control'].split(',')[0]], attributes[config['pallette']['selected_focus_control'].split(',')[1]], colors[config['pallette']['selected_focus_control'].split(',')[2]]),
                'selected_focus_field': (colors[config['pallette']['selected_focus_field'].split(',')[0]], attributes[config['pallette']['selected_focus_field'].split(',')[1]], colors[config['pallette']['selected_focus_field'].split(',')[2]]),
                'title': (colors[config['pallette']['title'].split(',')[0]], attributes[config['pallette']['title'].split(',')[1]], colors[config['pallette']['title'].split(',')[2]])
        }})
    elif tui == 'urwid':
        return [
        #(['background']+[config['pallette']['background'].split(',')[0], config['pallette']['background'].split(',')[2], '' if config['pallette']['background'].split(',')[1] == 'normal' else config['pallette']['background'].split(',')[1]]),
        (['background']+['0', 'bold', '1']),
#        (['borders']+config['pallette']['borders'].split(',')),
#        (['button']+config['pallette']['button'].split(',')),
#        (['control']+config['pallette']['control'].split(',')),
#        (['disabled']+config['pallette']['disabled'].split(',')),
#        (['edit_text']+config['pallette']['edit_text'].split(',')),
#        (['field']+config['pallette']['field'].split(',')),
#        (['focus_edit_text']+config['pallette']['focus_edit_text'].split(',')),
#        (['focus_button']+config['pallette']['focus_button'].split(',')),
#        (['focus_field']+config['pallette']['focus_field'].split(',')),
#        (['focus_readonly']+config['pallette']['focus_readonly'].split(',')),
#        (['invalid']+config['pallette']['invalid'].split(',')),
#        (['label']+config['pallette']['label'].split(',')),
#        (['readonly']+config['pallette']['readonly'].split(',')),
#        (['scroll']+config['pallette']['scroll'].split(',')),
#        (['selected_field']+config['pallette']['selected_field'].split(',')),
#        (['selected_focus_control']+config['pallette']['selected_focus_control'].split(',')),
#        (['selected_focus_field']+config['pallette']['selected_focus_field'].split(',')),
#        (['title']+config['pallette']['title'].split(','))
        ]

