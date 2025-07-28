label avg12567:

play music "ED6102.ogg"
scene avg_bg_023
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
c23 '[convertstrid(1155091)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
c12321 '[convertstrid(1155092)]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1155093)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1155094)]'
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1155095)]'
hide p3
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li30.ogg"
c41 '[convertstrid(1155096)]'
$ update_portrait('oc004_01 5', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[convertstrid(1155097)]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1155098)]'
hide p4
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1155099)]'
hide p3
c12321 '[convertstrid(1155100)]'
return