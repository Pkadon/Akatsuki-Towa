label avg12174:
stop music

play music "ed7105.ogg"
scene avg_bg_028
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1128560]]'
hide p1
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
c9651 '[textdict[1128561]]'
hide p1
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
c9651 '[textdict[1128562]]'
hide p1
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
c9651 '[textdict[1128563]]'
hide p1
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch08.ogg"
c21 '[textdict[1128564]]'
hide p1
hide p2
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1128565]]'
hide p2
hide p1
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1128567]]'
return