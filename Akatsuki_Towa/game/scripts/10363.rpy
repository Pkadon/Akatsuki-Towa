label avg10363:
stop music

play music "ed9999.ogg"
scene avg_bg_050
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
window show
with fade_in
c21 '[textdict[1131987]]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1131988]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 2', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1131989]]'
hide p4
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1131990]]'
hide p1
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1131991]]'
hide p3
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch08.ogg"
c21 '[textdict[1131992]]'
hide p1
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 5)
c13 '[textdict[1131993]]'
hide p2
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1131994]]'
hide p1
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 5)
c23 '[textdict[1131995]]'
hide p4
$ update_portrait('oc002_01 15', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1131996]]'
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1131997]]'
hide p3
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch20.ogg"
c21 '[textdict[1131998]]'
return