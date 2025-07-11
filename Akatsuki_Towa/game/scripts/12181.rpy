label avg12181:

play music "ED6104.ogg"
scene avg_bg_010
window show
with fade_in
c0 '[textdict[1007707]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1120600]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1120601]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[textdict[1120602]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1120603]]'
hide p2
hide p1
$ update_portrait('sc022_01 2', 'p500', [l(-9), light, flip], 6)
with fade
c5001 '[textdict[1120604]]'
$ update_portrait('sc022_01 2', 'p500', [l(-9), dark, flip], 6)
$ update_portrait('oc002_01 6', 'p2', [r_entrance(-3), light], 5)
play sfxvoice "avg_vocal_ch05.ogg"
c23 '[textdict[1120605]]'
$ update_portrait('sc022_01 2', 'p500', [l(-9), dark, flip], 6)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 5)
c23 '[textdict[1120606]]'
hide p500
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('sc022_01 1', 'p30', [l(-9), l_shake, light, flip], 6)
c301 '[textdict[1120607]]'
$ update_portrait('sc022_01 1', 'p30', [l(-9), dark, flip], 6)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 5)
c23 '[textdict[1120608]]'
hide p30
hide p2
c0 '[textdict[1120609]]'
$ update_portrait('sc022_01 1', 'p30', [l(-9), light, flip], 6)
c301 '[textdict[1120610]]'
$ update_portrait('sc022_01 1', 'p30', [l(-9), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r_exit(-2), light], 5)
c13 '[textdict[1120611]]'
hide p1
$ update_portrait('sc022_01 4', 'p30', [l(-9), light, flip], 6)
c301 '[textdict[1120612]]'
hide p30
play sfx2 "other_7004.ogg"
c0 '[textdict[1120613]]'
$ update_portrait('sc022_01 4', 'p30', [l(-9), light, flip], 6)
c301 '[textdict[1120614]]'
$ update_portrait('sc022_01 4', 'p30', [l(-9), light, flip], 6)
c301 '[textdict[1120615]]'
$ update_portrait('sc022_01 1', 'p30', [l(-9), light, flip], 6)
c301 '[textdict[1120616]]'
return