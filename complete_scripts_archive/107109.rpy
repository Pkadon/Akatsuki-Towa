label avg107109:

play music "ed7544.ogg"
scene avg_bg_003
$ update_portrait('oc004_01 21', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with fade_in
c41 '[convertstrid(1180056)]'
$ update_portrait('oc004_01 21', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc005_01 4', 'p5', [r(-6), light], 6)
c53 '[convertstrid(1180057)]'
$ update_portrait('oc005_01 7', 'p5', [r(-6), light], 6)
c53 '[convertstrid(1180058)]'
hide p5
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1180059)]'
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 19', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1180060)]'
hide p1
$ update_portrait('oc004_01 19', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 9', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1180061)]'
$ update_portrait('oc003_01 9', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 21', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1180062)]'
hide p3
$ update_portrait('oc004_01 21', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('st061_01 4', 'p1304', [r(-2), light], 6)
c13043 '[convertstrid(1180063)]'
hide p1304
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1180064)]'
stop music
$ update_portrait('oc002_01 15', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 13', 'p4', [l(-5), light, flip], 6)
c41 '[convertstrid(1180065)]' with shake
hide p4
$ update_portrait('oc003_01 12', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1180066)]'
hide p2
$ update_portrait('oc003_01 12', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1180067)]'
$ update_portrait('oc001_01 3', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1180068)]'
play music "ed7551.ogg"
scene avg_bg_507
$ update_narrator('c0')
with fade
c0 '[convertstrid(1180069)]'
c0 '[convertstrid(1180070)]'
c0 '[convertstrid(1180071)]'
return