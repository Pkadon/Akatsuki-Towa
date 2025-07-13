label avg10661:

play music "ed9999.ogg"
scene avg_bg_070
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7018.ogg"
c0 '[textdict[1165584]]'
scene avg_bg_001
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
$ update_narrator('c161')
with fade
c161 '[textdict[1165585]]'
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
c161 '[textdict[1165586]]'
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1165587]]'
hide p16
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1165588]]'
hide p2
hide p1
c0 '[textdict[1165589]]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 5)
c43 '[textdict[1165590]]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1165591]]'
hide p4
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1165592]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1165593]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1165594]]'
hide p2
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 5)
c13043 '[textdict[1165595]]'
return