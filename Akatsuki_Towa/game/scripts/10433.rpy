label avg10433:
stop music

play music "ed7526.ogg"
scene avg_bg_036
window show
with fade_in
$ update_portrait('oc004_01 4', 'p4', [r_entrance(-5), light], 5)
c43 '[textdict[1141497]]'
hide p4
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 5)
c43 '[textdict[1141498]]'
$ update_portrait('oc004_01 11', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1141499]]'
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc005_01 4', 'p5', [r_exit(-6), light], 5)
play sfxvoice "avg_vocal_ji11.ogg"
c53 '[textdict[1141500]]'
hide p5
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 4', 'p2', [r(-3), r_shake, light], 5)
play sfxvoice "avg_vocal_ch13.ogg"
c23 '[textdict[1141501]]'
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 5)
c13 '[textdict[1141502]]'
hide p3
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1141503]]'
hide p1
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[1141504]]'
hide p3
hide p2
c0 '[textdict[1141505]]'
return