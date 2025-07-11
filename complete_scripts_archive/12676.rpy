label avg12676:

play music "ed6564.ogg"
scene avg_bg_004
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1166914]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1166915]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 5)
c43 '[textdict[1166916]]'
hide p2
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1166917]]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 17', 'p4', [r(-5), light], 5)
c43 '[textdict[1166918]]'
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 5)
c43 '[textdict[1166919]]'
hide p3
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1166920]]'
stop music
hide p2
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1166921]]'
play music "ed7511.ogg"
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1166922]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
play sfx2 "other_7080.ogg"
c31 '[textdict[1166923]]'
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 5)
play sfx2 "other_7079.ogg"
c43 '[textdict[1166924]]'
hide p3
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
play sfx2 "fight_6019.ogg"
c21 '[textdict[1166925]]'
hide p4
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 5)
play sfx2 "fight_6024.ogg"
c13 '[textdict[1166926]]'
return