label avg22206:

$ play_music("ed7151.ogg")
scene avg_bg_036
$ update_narrator('c21')
window show
with fade_in
$ update_portrait('oc002_01 10', 'p2', [l_entrance(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch15.ogg"
c21 '[convertstrid(1128608)]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1128609)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
c5631 '[convertstrid(1128610)]'
c5621 '[convertstrid(1128611)]'
hide p1
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1128612)]'
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
c5631 '[convertstrid(1128613)]'
hide p3
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[convertstrid(1128614)]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
c5621 '[convertstrid(1128615)]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[convertstrid(1128616)]'
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
c5631 '[convertstrid(1128617)]'
hide p2
c5623 '[convertstrid(1128618)]'
c5623 '[convertstrid(1128619)]'
c5631 '[convertstrid(1128620)]'
c5631 '[convertstrid(1128621)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na04_b.ogg"
c13 '[convertstrid(1128622)]'
return