label avg20074:

play music "ed7150.ogg"
scene avg_bg_022
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
c11 '[textdict[1003943]]'
scene avg_bg_070
$ update_narrator('c0')
with fade
play sfx2 "other_7045.ogg"
c0 '[textdict[1003944]]'
scene avg_bg_022
$ update_narrator('c31')
with fade
$ update_portrait('oc003_01 2', 'p3', [l_entrance(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro10.ogg"
c31 '[textdict[1003945]]'
$ update_portrait('oc003_01 2', 'p3', [l(-6), dark, flip], 6)
c5413 '[textdict[1003946]]'
hide p3
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1003947]]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
c5423 '[textdict[1003948]]'
hide p2
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1003949]]'
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 6)
c5413 '[textdict[1003950]]'
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1003951]]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1003952]]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 6)
c5413 '[textdict[1003953]]'
c5413 '[textdict[1003954]]'
c5413 '[textdict[1003955]]'
c5423 '[textdict[1003956]]'
hide p1
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1003957]]'
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1003958]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1003959]]'
return