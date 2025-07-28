label avg10750:

play music "ed7566.ogg"
scene avg_bg_036
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1173783)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st057_01 4', 'p1453', [l(-16), light, flip], 6)
c14531 '[convertstrid(1173784)]'
hide p1
$ update_portrait('st057_01 4', 'p1453', [l(-16), dark, flip], 5)
c14543 '[convertstrid(1173785)]'
c14553 '[convertstrid(1173786)]'
$ update_portrait('st057_01 4', 'p1453', [l(-16), light, flip], 6)
c14531 '[convertstrid(1173787)]'
$ update_portrait('st057_01 3', 'p1453', [l(-16), light, flip], 6)
c14531 '[convertstrid(1173788)]'
hide p1453
$ update_portrait('oc003_01 10', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1173789)]'
$ update_portrait('oc003_01 10', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1173790)]'
hide p3
hide p1
play sfx2 "other_7080.ogg"
c0 '[convertstrid(1173791)]' with shake
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1173792)]'
return