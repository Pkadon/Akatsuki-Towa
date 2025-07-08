label avg12407:
stop music

play music "ed7100.ogg"
scene avg_bg_023
window show
with fade_in
$ update_portrait('oc001_01 4', 'p1', [r_entrance(-2), light], 5)
c13 '[textdict[1140242]]'
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 7', 'p3', [l_entrance(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro14.ogg"
c31 '[textdict[1140243]]'
hide p1
hide p3
$ update_portrait('oc003_01 7', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
play sfx2 "other_7004.ogg"
c13 '[textdict[1140244]]'
hide p3
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 7', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li19.ogg"
c41 '[textdict[1140245]]'
hide p1
hide p4
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 5)
c23 '[textdict[1140246]]'
hide p4
hide p2
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 10', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1140247]]'
hide p4
hide p2
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1140248]]'
hide p4
hide p2
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
c31 '[textdict[1140249]]'
hide p2
hide p3
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 5)
c23 '[textdict[1140250]]'
return