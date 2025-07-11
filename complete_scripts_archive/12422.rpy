label avg12422:

play music "ed7103.ogg"
scene avg_bg_023
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
window show
with fade_in
play sfxvoice "avg_vocal_ch11.ogg"
c21 '[textdict[1140266]]'
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1140267]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro02.ogg"
c31 '[textdict[1140268]]'
hide p3
$ update_portrait('oc004_01 1', 'p4', [l_entrance(-5), light, flip], 6)
c41 '[textdict[1140269]]'
$ update_portrait('oc004_01 4', 'p4', [l(-5), l_shake, light, flip], 6)
c41 '[textdict[1140270]]'
hide p1
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 5)
play sfxvoice "avg_vocal_ch10.ogg"
c23 '[textdict[1140271]]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1140272]]'
hide p4
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1140273]]'
hide p3
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1140274]]'
$ update_portrait('oc002_01 15', 'p2', [l_exit(-3), light, flip], 6)
c21 '[textdict[1140275]]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), r_shake, light], 5)
c13 '[textdict[1140276]]'
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 5)
c13 '[textdict[1140277]]'
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 5)
c13 '[textdict[1140278]]'
return