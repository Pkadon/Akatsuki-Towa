label avg12123:
stop music

play music "ED6104.ogg"
scene avg_bg_038
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
window show
with fade_in
play sfx2 "common_select.ogg"
c13 '[textdict[1128233]]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
c23 '[textdict[1128234]]'
hide p2
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
c9591 '[textdict[1128235]]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[textdict[1128236]]'
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
c9591 '[textdict[1128237]]'
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
c9591 '[textdict[1128238]]'
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
c9591 '[textdict[1128239]]'
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
c9591 '[textdict[1128240]]'
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
c9591 '[textdict[1128241]]'
hide p1
play sfx2 "common_tag_2.ogg"
c0 '[textdict[1128242]]'
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 5)
c33 '[textdict[1128243]]'
hide p3
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
c9591 '[textdict[1128244]]'
hide p3
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
c9591 '[textdict[1128245]]'
hide p3
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
play sfx2 "common_quest.ogg"
c9591 '[textdict[1128246]]'
return