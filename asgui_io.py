import adventurescript.defaultio as default
import time

import events
import res
import window

show = default.show
load_file = default.load_file

# def show(info, text):
#     window.labeltext += text.split("\n")
#     if len(window.labeltext) > 20:
#         window.labeltext = window.labeltext[-20:]

def wait(info, **kwargs):
    events.value = ""
    events.wait = True
    window.buttons["b1"].change_images(res.btn_input)
    while events.value == "" and not window.closed:
        time.sleep(1/60)
    if events.value == "q":
        info.status = "quit"
        info.showfunc(info, ">> Quit")
        return 0
    if window.closed:
        quit()
    window.buttons["b1"].change_images(res.btn_grey)
    events.wait = False

def query(info, text, choices, allow_save, **kwargs):
    if text != "":
        info.showfunc(info, "> " + text)
    c = 1
    for ch in choices:
        info.showfunc(info, f"> {c}. {ch}")
        c += 1
    
    events.value = ""
    events.choice = True
    events.max_buttons = c-1
    if allow_save:
        events.cansave = True
        window.buttons["save"].change_images(res.btn_save)
        window.buttons["restore"].change_images(res.btn_restore)
    for choice in range(c-1):
        window.buttons[f"b{choice+1}"].change_images(res.number_buttons[choice])
    while events.value == "" and not window.closed:
        time.sleep(1/60)
    if window.closed:
        quit()
    for choice in range(c-1):
        window.buttons[f"b{choice+1}"].change_images(res.btn_grey)
    window.buttons["save"].change_images(res.btn_grey)
    window.buttons["restore"].change_images(res.btn_grey)
    events.choice = False
    events.cansave = False
    if events.value == "q":
        info.status = "quit"
        info.showfunc(info, ">> Quit")
        return 0
    elif events.value == "s":
        info.showfunc(info, ">> Save")
        info.save()
        info.showfunc(info, "Saved!")
        info.pointer -= 1
        return 0
    elif events.value == "r":
        info.showfunc(info, ">> Restore save")
        try:
            info.load_save()
        except Exception as e:
            info.showfunc(info, "No save exists!")
            info.pointer -= 1
            return 0
        else:
            info.showfunc(info, "Save restored!")
            info.reload()
            return 0
    else:
        info.showfunc(info, ">> " + events.value)
        return int(events.value)

# io = default.as_io(default.show, default.wait, default.query, default.load_file)