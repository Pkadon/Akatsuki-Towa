label avg12353:

play music "ed7104.ogg"
scene avg_bg_050
$ update_portrait('oc001_01 6', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7021.ogg"
c13 '[convertstrid(1133603)]'
$ update_portrait('oc001_01 6', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1133604)]'
play music "ed7110.ogg"
scene avg_bg_001
$ update_portrait('oc005_01 2', 'p5', [r(-6), light], 6)
$ update_narrator('c53')
with fade
play sfxvoice "avg_vocal_ji02.ogg"
c53 '[convertstrid(1133645)]'
$ update_portrait('oc005_01 2', 'p5', [r(-6), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1133646)]'
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 6)
c53 '[convertstrid(1133647)]'
hide p4
$ update_portrait('oc005_01 4', 'p5', [r(-6), dark], 5)
$ update_portrait('oc002_01 11', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1133648)]'
hide p5
$ update_portrait('oc002_01 11', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 6', 'p1', [r(-2), light], 6)
play sfx2 "other_7018.ogg"
c13 '[convertstrid(1133649)]'
return