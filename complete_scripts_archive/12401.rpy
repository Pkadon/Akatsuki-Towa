label avg12401:

play music "ed7100.ogg"
scene avg_bg_023
$ update_narrator('c23')
window show
with fade_in
$ update_portrait('oc002_01 8', 'p2', [r_entrance(-3), light], 5)
c23 '[textdict[1140226]]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 2', 'p3', [l_entrance(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro09.ogg"
c31 '[textdict[1140227]]'
hide p2
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 5)
c43 '[textdict[1140228]]'
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 5)
c43 '[textdict[1140229]]'
hide p3
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1140230]]'
hide p4
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 5)
c23 '[textdict[1140231]]'
hide p1
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li19.ogg"
c41 '[textdict[1140232]]'
hide p4
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1140233]]'
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch02.ogg"
c23 '[textdict[1140234]]'
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 5)
c23 '[textdict[1140235]]'
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
c31 '[textdict[1140236]]'
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1140237]]'
hide p2
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 22', 'p4', [r(-5), light], 5)
c43 '[textdict[1140238]]'
$ update_portrait('oc004_01 22', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1140239]]'
hide p4
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1140240]]'
return