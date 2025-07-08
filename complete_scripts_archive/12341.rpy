label avg12341:
stop music

play music "ed7105.ogg"
scene avg_bg_070
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
window show
with fade_in
play sfx2 "other_7048.ogg"
c11 '[textdict[1133492]]'
scene avg_bg_022
$ update_portrait('st053_01 4', 'p1007', [r(-12), light], 5)
with fade
c10073 '[textdict[1133493]]'
hide p1007
$ update_portrait('st053_01 3', 'p1007', [r(-12), light], 5)
c10073 '[textdict[1133494]]'
hide p1007
$ update_portrait('st053_01 3', 'p1007', [r(-12), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1133495]]'
hide p1007
hide p2
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('st053_01 1', 'p1007', [r(-12), light], 5)
c10073 '[textdict[1133496]]'
hide p1007
hide p2
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('st053_01 2', 'p1007', [r(-12), light], 5)
c10073 '[textdict[1133497]]'
hide p2
hide p1007
$ update_portrait('st053_01 2', 'p1007', [r(-12), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1133498]]'
hide p1007
hide p3
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('st053_01 4', 'p1007', [r(-12), light], 5)
c10073 '[textdict[1133499]]'
hide p3
hide p1007
$ update_portrait('st053_01 4', 'p1007', [r(-12), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1133500]]'
hide p1007
hide p1
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
c23 '[textdict[1133501]]'
hide p1
hide p2
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1133502]]'
hide p2
hide p3
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 5)
play sfxvoice "avg_vocal_li19.ogg"
c43 '[textdict[1133503]]'
hide p4
hide p3
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 6', 'p4', [r(-5), light], 5)
c43 '[textdict[1133504]]'
hide p3
hide p4
$ update_portrait('oc004_01 6', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na05.ogg"
c11 '[textdict[1133505]]'
return