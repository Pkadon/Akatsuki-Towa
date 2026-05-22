label avg20131:

stop music
scene avg_bg_071
$ update_portrait('oc001_01 20', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
play sfx2 "other_7054.ogg"
c11 '[convertstrid(1006648)]'
$ update_portrait('oc001_01 20', 'p1', [l(-2), dark, flip], 5)
c7013 '[convertstrid(1006649)]'
play sfxvoice "avg_vocal_ji05.ogg"
c7013 '[convertstrid(1006650)]'
hide p1
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1006651)]'
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 5)
c7013 '[convertstrid(1006652)]'
$ update_portrait('oc003_01 2', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1000335)]'
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 5)
c7013 '[convertstrid(1006654)]'
$ update_portrait('oc003_01 15', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro05.ogg"
c31 '[convertstrid(1006655)]'
$ update_portrait('oc003_01 15', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('sc044_01 3', 'p51', [r(-7), light], 6)
c513 '[convertstrid(1006656)]'
hide p3
$ update_portrait('sc044_01 3', 'p51', [r(-7), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li19.ogg"
c41 '[convertstrid(1006657)]'
hide p51
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1006658)]'
hide p4
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 5', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1006659)]'
return