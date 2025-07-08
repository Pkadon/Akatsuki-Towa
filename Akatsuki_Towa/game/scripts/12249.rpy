label avg12249:
stop music

play music "ed7111.ogg"
scene avg_bg_012
window show
with fade_in
$ update_portrait('st051_01 2', 'p709', [l_entrance(-9), light, flip], 6)
play sfx2 "other_7042.ogg"
c7091 '[textdict[1121350]]'
$ update_portrait('st051_01 2', 'p709', [l(-9), dark, flip], 6)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 5)
c33 '[textdict[1121351]]'
hide p709
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('st051_01 1', 'p709', [l(-9), light, flip], 6)
play sfx2 "other_7022.ogg"
c7091 '[textdict[1121352]]'
hide p3
$ update_portrait('st051_01 1', 'p709', [l(-9), dark, flip], 6)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 5)
c33 '[textdict[1121353]]'
hide p709
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('st051_01 2', 'p709', [l(-9), light, flip], 6)
c7091 '[textdict[1121354]]'
return