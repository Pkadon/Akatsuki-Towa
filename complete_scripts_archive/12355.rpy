label avg12355:

play music "ed7123.ogg"
scene avg_bg_046
$ update_narrator('c10951')
window show
with fade_in
play sfx2 "other_7048.ogg"
c10951 '[convertstrid(1133650)]'
c10951 '[convertstrid(1133651)]'
c10951 '[convertstrid(1133652)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1133657)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1133658)]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1133659)]'
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 11', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch17.ogg"
c21 '[convertstrid(1133660)]'
hide p3
$ update_portrait('oc002_01 11', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1133661)]'
return