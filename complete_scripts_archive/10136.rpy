label avg10136:

play music "ED6505.ogg"
scene avg_bg_027
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1007379)]'
$ update_portrait('oc002_01 6', 'p2', [l_entrance(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch08.ogg"
c21 '[convertstrid(1007380)]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1007381)]'
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('uc004_02 5', 'p570', [r_entrance(-9), light], 6)
play sfx2 "other_7021.ogg"
c5703 '[convertstrid(1007382)]'
hide p1
$ update_portrait('uc004_02 5', 'p570', [r(-9), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1007383)]'
hide p570
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('uc004_02 2', 'p961', [r(-9), light], 6)
c9613 '[convertstrid(1007384)]'
hide p2
$ update_portrait('uc004_02 2', 'p961', [r(-9), dark], 5)
$ update_portrait('oc001_01 22', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1007385)]'
$ update_portrait('oc001_01 22', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('uc004_02 1', 'p961', [r(-9), light], 6)
c9613 '[convertstrid(1007386)]'
$ update_portrait('uc004_02 1', 'p961', [r(-9), dark], 5)
$ update_portrait('oc001_01 23', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1007387)]'
hide p961
$ update_portrait('oc001_01 23', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1007682)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1007683)]'
return