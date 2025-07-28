label avg1096:

play music "ed7200.ogg"
scene avg_bg_010
$ update_portrait('sc050_01 1', 'p57', [l(-19), light, flip], 6)
$ update_narrator('c571')
window show
with fade_in
c571 '[convertstrid(2102201)]'
$ update_portrait('sc050_01 1', 'p57', [l(-19), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2102202)]'
$ update_portrait('oc001_01 5', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2102203)]'
hide p57
$ update_portrait('oc001_01 5', 'p1', [r(-2), dark], 5)
c10931 '[convertstrid(2102204)]'
c10931 '[convertstrid(2102205)]' with shake
$ update_portrait('oc001_01 7', 'p1', [r(-2), r_shake, light], 6)
c13 '[convertstrid(2102206)]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
c10931 '[convertstrid(2102207)]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2102208)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2102209)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc050_01 1', 'p57', [l(-19), light, flip], 6)
c571 '[convertstrid(2102210)]'
hide p57
c10931 '[convertstrid(2102211)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[convertstrid(2102212)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
c10931 '[convertstrid(2102213)]'
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na21.ogg"
c13 '[convertstrid(2102214)]'
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
c10931 '[convertstrid(2102215)]'
hide p1
play sfx2 "other_7013.ogg"
c0 '[convertstrid(2102216)]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2102217)]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc050_01 1', 'p57', [l(-19), light, flip], 6)
c571 '[convertstrid(2102218)]'
$ update_portrait('sc050_01 5', 'p57', [l(-19), light, flip], 6)
c571 '[convertstrid(2102219)]'
$ update_portrait('sc050_01 5', 'p57', [l(-19), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2102220)]'
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
c13 '[convertstrid(2102221)]'
return