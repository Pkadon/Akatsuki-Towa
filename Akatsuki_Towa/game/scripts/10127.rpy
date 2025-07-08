label avg10127:
stop music

play music "ed7150.ogg"
scene avg_bg_023
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
window show
with fade_in
play sfx2 "other_7004.ogg"
c23 '[textdict[1007263]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1007264]]'
hide p2
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[1007265]]'
hide p56
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 6', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1007266]]'
hide p1
$ update_portrait('sc049_01 6', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc002_01 5', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1007267]]'
hide p56
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1007268]]'
hide p2
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 5)
c13 '[textdict[1007269]]'
hide p1
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 5)
play sfxvoice "avg_vocal_ch04.ogg"
c23 '[textdict[1007270]]'
hide p2
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[textdict[1007271]]'
hide p56
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1007272]]'
hide p56
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1007273]]'
hide p1
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r_exit(-3), light], 5)
play sfx2 "other_7085.ogg"
c23 '[textdict[1007274]]'
hide p2
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 5)
c13 '[textdict[1007275]]'
return