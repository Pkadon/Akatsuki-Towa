label avg12640:

play music "ed7203.ogg"
scene avg_bg_070
$ update_narrator('c13251')
window show
with fade_in
play sfx2 "fight_6027.ogg"
c13251 '[textdict[1162998]]'
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 5)
c13 '[textdict[1162999]]'
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1163000]]'
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1163001]]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1163002]]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1163003]]'
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 5)
c13 '[textdict[1163004]]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [r(-2), dark], 5)
c13251 '[textdict[1163005]]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1163006]]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 5)
c13 '[textdict[1163007]]'
hide p1
$ update_portrait('oc002_01 23', 'p2', [r(-3), light], 5)
c23 '[textdict[1163008]]'
hide p3
$ update_portrait('oc002_01 23', 'p2', [r(-3), dark], 5)
c13251 '[textdict[1163009]]'
return