label avg10413:

play music "ed7151.ogg"
scene avg_bg_020
$ update_narrator('c21')
window show
with fade_in
$ update_portrait('oc002_01 17', 'p2', [l_entrance(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch19.ogg"
c21 '[convertstrid(1140683)]'
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1140684)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1140685)]'
scene avg_bg_070
$ update_portrait('oc004_01 11', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
with fade
c41 '[convertstrid(1140686)]'
scene avg_bg_020
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
with fade
c31 '[convertstrid(1140687)]'
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[convertstrid(1140688)]'
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1140689)]'
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1140690)]'
hide p3
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1140691)]'
scene avg_bg_070
$ update_narrator('c0')
with fade
c0 '[convertstrid(1140692)]'
scene avg_bg_020
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
with fade
play sfxvoice "avg_vocal_na06.ogg"
c13 '[convertstrid(1140693)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1140694)]'
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1140695)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1140696)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1140697)]'
return