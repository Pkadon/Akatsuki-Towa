label avg12010:

play music "ed7150.ogg"
scene avg_bg_023
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "other_7048.ogg"
c23 '[textdict[1007229]]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('sc049_01 2', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1007230]]'
hide p2
$ update_portrait('sc049_01 2', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[1007231]]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1007232]]'
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1007233]]'
$ update_portrait('sc049_01 10', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1007234]]'
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1007235]]'
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1007236]]'
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1007237]]'
$ update_portrait('sc049_01 1', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1007238]]'
$ update_portrait('oc001_01 7', 'p1', [r(-2), r_shake, light], 5)
c13 '[textdict[1007239]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[textdict[1007240]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1007241]]'
$ update_portrait('sc049_01 4', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1007242]]'
$ update_portrait('sc049_01 4', 'p56', [l(-8), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1007243]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[1007244]]'
hide p56
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[textdict[1007245]]'
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1007246]]'
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1007247]]'
return