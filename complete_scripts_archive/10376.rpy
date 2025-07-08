label avg10376:
stop music

play music "ed7151.ogg"
scene avg_bg_023
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1132156]]'
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc048_01 1', 'p55', [l(-7), light, flip], 6)
c551 '[textdict[1132157]]'
hide p1
hide p55
$ update_portrait('sc048_01 1', 'p55', [l(-7), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1132158]]'
hide p55
hide p1
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1132159]]'
return