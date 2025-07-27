label avg12029:

play music "ed7150.ogg"
scene avg_bg_014
$ update_narrator('c9693')
window show
with fade_in
play sfx2 "other_7046.ogg"
c9693 '[convertstrid(1120114)]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1120115)]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 6)
c9693 '[convertstrid(1120116)]'
hide p1
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1120117)]'
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 6)
c9693 '[convertstrid(1120118)]'
hide p2
c0 '[convertstrid(1120119)]'
c9691 '[convertstrid(1120120)]'
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na21.ogg"
c13 '[convertstrid(1120121)]'
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
c21 '[convertstrid(1120122)]'
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1120123)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1120124)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c9691 '[convertstrid(1120125)]'
hide p1
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 5)
c23 '[convertstrid(1120126)]'
return