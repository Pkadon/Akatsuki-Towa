label avg12611:
stop music

play music "ed7111.ogg"
scene avg_bg_012
window show
with fade_in
c0 '[textdict[1161439]]'
$ update_portrait('oc003_01 13', 'p3', [r_entrance(-6), light], 5)
play sfx2 "other_7046.ogg"
c33 '[textdict[1161440]]'
hide p3
$ update_portrait('oc003_01 13', 'p3', [r(-6), dark], 5)
$ update_portrait('st051_01 1', 'p709', [l(-9), light, flip], 6)
c7091 '[textdict[1161441]]'
hide p3
hide p709
$ update_portrait('st051_01 1', 'p709', [l(-9), dark, flip], 6)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 5)
c33 '[textdict[1161442]]'
hide p3
hide p709
$ update_portrait('st051_01 1', 'p709', [l(-9), dark, flip], 6)
$ update_portrait('oc003_01 13', 'p3', [r(-6), light], 5)
c33 '[textdict[1161443]]'
hide p709
hide p3
$ update_portrait('oc003_01 13', 'p3', [r(-6), dark], 5)
$ update_portrait('st051_01 1', 'p709', [l(-9), light, flip], 6)
c7091 '[textdict[1161444]]'
hide p3
hide p709
$ update_portrait('st051_01 1', 'p709', [l(-9), dark, flip], 6)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 5)
c33 '[textdict[1161445]]'
hide p3
hide p709
$ update_portrait('st051_01 1', 'p709', [l(-9), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1161446]]'
hide p709
hide p1
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 13', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1161447]]'
return