label avg12413:
stop music

play music "ed7565.ogg"
scene avg_bg_023
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
window show
with fade_in
c41 '[textdict[1140252]]'
$ update_portrait('oc004_01 2', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 6', 'p2', [r(-3), r_shake, light], 5)
play sfxvoice "avg_vocal_ch08.ogg"
c23 '[textdict[1140253]]'
hide p2
$ update_portrait('oc004_01 2', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 5)
c13 '[textdict[1140254]]'
hide p4
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch15.ogg"
c21 '[textdict[1140255]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1140256]]'
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 5)
play sfxvoice "avg_vocal_li19.ogg"
c43 '[textdict[1140257]]'
hide p4
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1140258]]'
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[textdict[1140259]]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l_exit(-5), light, flip], 6)
c41 '[textdict[1140260]]'
hide p4
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 5)
c13 '[textdict[1140261]]'
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l_entrance(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
c31 '[textdict[1140262]]'
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 5)
c13 '[textdict[1140263]]'
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1140264]]'
return