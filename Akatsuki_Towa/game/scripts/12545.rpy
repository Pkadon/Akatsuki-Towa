label avg12545:

play music "ED6105.ogg"
scene avg_bg_010
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
window show
with fade_in
play sfxvoice "avg_vocal_ro09.ogg"
c31 '[convertstrid(1152953)]'
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 23', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1152954)]'
hide p4
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1152955)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1152956)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1152957)]'
return