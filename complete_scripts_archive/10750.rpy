label avg10750:
stop music

play music "ed7566.ogg"
scene avg_bg_036
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1173783]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st057_01 4', 'p1453', [l(-16), light, flip], 6)
c14531 '[textdict[1173784]]'
hide p1
$ update_portrait('st057_01 4', 'p1453', [l(-16), dark, flip], 6)
c14543 '[textdict[1173785]]'
$ update_portrait('st057_01 4', 'p1453', [l(-16), dark, flip], 6)
c14553 '[textdict[1173786]]'
hide p1453
$ update_portrait('st057_01 4', 'p1453', [l(-16), light, flip], 6)
c14531 '[textdict[1173787]]'
hide p1453
$ update_portrait('st057_01 3', 'p1453', [l(-16), light, flip], 6)
c14531 '[textdict[1173788]]'
hide p1453
$ update_portrait('oc003_01 10', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1173789]]'
$ update_portrait('oc003_01 10', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 5)
c13 '[textdict[1173790]]'
hide p3
hide p1
play sfx2 "other_7080.ogg"
c0 '[textdict[1173791]]' with shake
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1173792]]'
return