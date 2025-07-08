label avg12546:
stop music

play music "ED6105.ogg"
scene avg_bg_010
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 5)
window show
with fade_in
play sfxvoice "bcv_oc001_hurt_01.ogg"
c13 '[textdict[1152959]]'
hide p1
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1152960]]'
hide p2
hide p1
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1152961]]'
hide p1
hide p3
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 5)
c43 '[textdict[1152962]]'
return