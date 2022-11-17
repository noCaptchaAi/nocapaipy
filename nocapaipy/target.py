def get_target(frame):
    target_element = frame.find('div', class_='prompt-text')
    if not target_element:
        raise Exception('getTarget: no target found')

    return target_element.text