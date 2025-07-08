label avg10537:
stop music

play music "ED6301.ogg"
scene avg_bg_102
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
window show
with fade_in
c291 '[textdict[1152574]]'
hide p29
$ update_portrait('sc021_01 4', 'p29', [l(-17), dark, flip], 6)
$ update_portrait('oc002_01 4', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1152575]]'
hide p29
hide p2
$ update_portrait('oc002_01 4', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1152576]]'
hide p2
hide p4
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1152577]]'
return