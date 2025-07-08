label avg12567:
stop music

play music "ED6102.ogg"
scene avg_bg_023
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
window show
with fade_in
c23 '[textdict[1155091]]'
hide p2
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
c12321 '[textdict[1155092]]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1155093]]'
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1155094]]'
hide p1
hide p3
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
c23 '[textdict[1155095]]'
hide p3
hide p2
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li30.ogg"
c41 '[textdict[1155096]]'
hide p2
hide p4
$ update_portrait('oc004_01 5', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1155097]]'
hide p2
hide p4
$ update_portrait('oc004_01 5', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[1155098]]'
hide p4
hide p1
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1155099]]'
hide p3
hide p1
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
c12321 '[textdict[1155100]]'
return