label avg12841:

play music "ed7302.ogg"
scene avg_bg_074
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1186240)]'
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1186241)]'
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('st061_01 4', 'p1304', [r(-2), light], 5)
c13043 '[convertstrid(1186242)]'
hide p3
hide p1304
$ update_narrator('c0')
with fade
c0 '[convertstrid(1186243)]'
scene avg_bg_038
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
with fade
c13 '[convertstrid(1186244)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1186245)]'
hide p4
c15301 '[convertstrid(1186246)]'
c15291 '[convertstrid(1186247)]'
hide p1
play sfx2 "other_7016.ogg"
c0 '[convertstrid(1186248)]'
$ update_portrait('oc003_01 9', 'p3', [r_midback(-6), light], 5)
c33 '[convertstrid(1186249)]'
$ update_portrait('oc003_01 9', 'p3', [r(-6), dark], 5)
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
c13041 '[convertstrid(1186250)]'
hide p3
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1186251)]'
hide p1304
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1186252)]'
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 9', 'p1', [r(-2), r_shake, light], 5)
c13 '[convertstrid(1186253)]'
hide p2
hide p1
play sfx2 "other_7045.ogg"
c0 '[convertstrid(1186254)]' with shake
return