label avg1008:
stop music

play music "ed7106.ogg"
scene avg_bg_023
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 5)
window show
with fade_in
c23 '[textdict[2100109]]'
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
play sfx2 "other_7037.ogg"
c561 '[textdict[2100110]]'
hide p2
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[2100111]]'
hide p56
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[2100112]]'
hide p56
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 7', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[2100113]]'
hide p56
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[2100114]]'
hide p1
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[2100115]]'
return