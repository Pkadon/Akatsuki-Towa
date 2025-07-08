label avg14101:
stop music

play music "ed7150.ogg"
scene avg_bg_023
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 5)
window show
with fade_in
play sfxvoice "bcv_oc002_c02_01.ogg"
c23 '[textdict[1202102]]'
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1202103]]'
hide p2
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1202104]]'
hide p56
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 10', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1202105]]'
hide p56
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1202106]]'
hide p56
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1202107]]'
hide p1
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1202108]]'
hide p2
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1202109]]'
hide p1
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1202110]]'
hide p56
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1202111]]'
return