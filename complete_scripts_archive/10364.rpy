label avg10364:
stop music

play music "ed7105.ogg"
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
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1131990]]'
return