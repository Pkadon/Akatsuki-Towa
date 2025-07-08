label avg1009:
stop music

play music "ed7106.ogg"
scene avg_bg_023
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
window show
with fade_in
c21 '[textdict[2100117]]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 5)
c13 '[textdict[2100118]]'
hide p2
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
play sfx2 "other_7036.ogg"
c561 '[textdict[2100119]]'
hide p56
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[2100120]]'
hide p56
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 7', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[2100121]]'
hide p56
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[2100122]]'
hide p1
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[2100123]]'
return