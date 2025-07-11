label avg12658:

play music "ED6300.ogg"
scene avg_bg_070
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 5)
window show
with fade_in
c33 '[textdict[1166397]]'
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1166398]]'
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1166399]]'
hide p3
$ update_portrait('oc004_01 17', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[1166400]]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1166401]]'
hide p1
$ update_portrait('oc004_01 2', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc003_01 5', 'p3', [r(-6), light], 5)
c33 '[textdict[1166402]]'
$ update_portrait('oc003_01 5', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1166403]]'
play music "ed7511.ogg"
hide p4
play sfx2 "other_7079.ogg"
c13091 '[textdict[1166404]]' with shake
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1166405]]'
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 5)
play sfx2 "fight_6025.ogg"
c33 '[textdict[1166406]]'
return