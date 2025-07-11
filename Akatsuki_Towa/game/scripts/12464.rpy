label avg12464:

play music "ed7116.ogg"
scene avg_bg_020
window show
with fade_in
c0 '[textdict[1143858]]'
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1143859]]'
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1143860]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1143861]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1143862]]'
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[1143863]]'
hide p3
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1143864]]'
hide p4
hide p2
c0 '[textdict[1143865]]'
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[1143866]]'
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1143867]]'
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 5)
play sfxvoice "avg_vocal_li15.ogg"
c43 '[textdict[1143868]]'
return