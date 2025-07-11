label avg12638:

play music "ed7203.ogg"
scene avg_bg_070
$ update_portrait('oc002_01 3', 'p2', [r(-3), light], 5)
window show
with fade_in
play sfx2 "fight_6019.ogg"
c23 '[textdict[1162984]]'
$ update_portrait('oc002_01 3', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1162985]]'
hide p2
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
c33 '[textdict[1162986]]'
hide p4
$ update_portrait('oc003_01 4', 'p3', [r(-6), dark], 5)
c13251 '[textdict[1162987]]'
return