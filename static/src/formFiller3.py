# Automatically fills in the form at autbor.com/form
import pyautogui, time
# Set these to the correct coordinates for your particular computer
name_field = (648, 319)
submit_button = (651, 817)
submit_button_color = (75, 141, 249)
submit_another_link = (760, 224)

form_data = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
            ]

pyautogui.PAUSE = 0.5

for person in form_data:
    # Give the user a chance to kill the script
    print('>>> 5 SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    time.sleep(5)

    # Wait until form page has loaded.
    while not pyautogui.pixelMatchesColor(submit_button[0], submit_button[1], submit_button_color):
        time.sleep(0.5)

    print(f'Entering {person['name']} info...')
    pyautogui.click(name_field[0], name_field[1])

    # Fill out Name field
    pyautogui.typewrite(person['name'] + '\t')

    # Fill out Greatest Fear(s) field
    pyautogui.typewrite(person['fear'] + '\t')

    # Fill out Source of Wizard Powers field
    if person['source'] == 'wand':
        pyautogui.typewrite(['down', '\t'])
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down', 'down', '\t'])
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down', 'down', 'down', '\t'])
    elif person['source'] == 'money':
        pyautogui.typewrite(['down', 'down', 'down', 'down', '\t'])

    # Fill out Robocop field
    if person['robocop'] == 1:
        pyautogui.typewrite([' ', '\t'])
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right', 'right', '\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right', 'right', '\t'])
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])

    # Fill out Additional comments
    pyautogui.typewrite(person['comments'] + '\t')

    # Click Submit
    pyautogui.press('enter')

    # Wait until form page has loaded.
    print('Clicked Submit.')
    time.sleep(5)

    # Click the "Submit another response" link
    pyautogui.click(submit_another_link[0], submit_another_link[1])
