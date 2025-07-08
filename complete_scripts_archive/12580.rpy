label avg12580:
stop music

play music "ED6523.ogg"
scene avg_bg_080
$ update_portrait('oc001_01 14', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1155388]]'
hide p1
$ update_portrait('oc001_01 14', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1155389]]'
hide p2
hide p1
$ update_portrait('oc001_01 14', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 20', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1155390]]'
hide p3
hide p1
$ update_portrait('oc001_01 14', 'p1', [r(-2), dark], 5)
$ update_portrait('sc021_01 1', 'p29', [l_entrance(-17), light, flip], 6)
c291 '[textdict[1155391]]'
hide p1
hide p29
$ update_portrait('sc021_01 1', 'p29', [l(-17), dark, flip], 6)
$ update_portrait('oc004_01 20', 'p4', [r(-5), light], 5)
c43 '[textdict[1155392]]'
hide p29
hide p4
$ update_portrait('oc004_01 20', 'p4', [r(-5), dark], 5)
$ update_portrait('sc021_01 1', 'p29', [l(-17), light, flip], 6)
c291 '[textdict[1155393]]'
hide p4
hide p29
$ update_portrait('sc021_01 1', 'p29', [l(-17), dark, flip], 6)
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 5)
c23 '[textdict[1155394]]'
hide p2
hide p29
$ update_portrait('sc021_01 1', 'p29', [l(-17), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1155395]]'
hide p29
hide p1
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1155396]]'
return