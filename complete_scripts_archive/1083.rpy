label avg1083:

play music "ed7202.ogg"
scene avg_bg_036
window show
with fade_in
c0 '[textdict[2101824]]'
c0 '[textdict[2101825]]'
c0 '[textdict[2101826]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[2101827]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch24.ogg"
c21 '[textdict[2101828]]'
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[2101829]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[2101830]]'
hide p1
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 5)
c43 '[textdict[2101831]]'
hide p4
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na16.ogg"
c13 '[textdict[2101832]]'
hide p3
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[2101833]]'
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 5)
c13 '[textdict[2101834]]'
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 22', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[2101835]]'
hide p4
$ update_portrait('oc001_01 17', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[2101836]]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r_exit(-2), light], 5)
c13 '[textdict[2101837]]'
hide p1
hide p2
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[2101838]]'
return