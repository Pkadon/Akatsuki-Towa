label avg12639:

play music "ed7203.ogg"
scene avg_bg_070
$ update_narrator('c13251')
window show
with fade_in
c13251 '[textdict[1162989]]'
c13251 '[textdict[1162990]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1162991]]'
hide p1
c0 '[textdict[1162992]]'
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1162993]]'
play music "ed7511.ogg"
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), r_shake, light], 5)
c13 '[textdict[1162994]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
play sfx2 "other_7034.ogg"
c5001 '[textdict[1162995]]' with shake
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 5)
c13 '[textdict[1162996]]'
return