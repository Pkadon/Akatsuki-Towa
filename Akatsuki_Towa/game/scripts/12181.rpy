label avg12181:
stop music

play music "ED6104.ogg"
scene avg_bg_010
window show
with fade_out
c0 '[textdict[1007707]]'
show oc001_01 1 as p1 at r(-2), light, zorder 5
c13 '[textdict[1120600]]'
hide p1
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1120601]]'
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show oc002_01 2 as p2 at l(-3), l_shake, light, flip, zorder 6
c21 '[textdict[1120602]]'
hide p2
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show oc002_01 6 as p2 at l(-3), light, flip, zorder 6
c21 '[textdict[1120603]]'
hide p2
hide p1
show sc022_01 2 as p500 at l(-9), light, flip, zorder 6
with fade
c5001 '[textdict[1120604]]'
hide p500
show sc022_01 2 as p500 at l(-9), dark, flip, zorder 6
show oc002_01 6 as p2 at r_entrance(-3), light, zorder 5
play sfxvoice "avg_vocal_ch05.ogg"
c23 '[textdict[1120605]]'
hide p2
hide p500
show sc022_01 2 as p500 at l(-9), dark, flip, zorder 6
show oc002_01 12 as p2 at r(-3), light, zorder 5
c23 '[textdict[1120606]]'
hide p500
hide p2
show oc002_01 12 as p2 at r(-3), dark, zorder 5
show sc022_01 1 as p30 at l(-9), l_shake, light, flip, zorder 6
c301 '[textdict[1120607]]'
hide p2
hide p30
show sc022_01 1 as p30 at l(-9), dark, flip, zorder 6
show oc002_01 12 as p2 at r(-3), light, zorder 5
c23 '[textdict[1120608]]'
hide p30
hide p2
c0 '[textdict[1120609]]'
show sc022_01 1 as p30 at l(-9), light, flip, zorder 6
c301 '[textdict[1120610]]'
hide p30
show sc022_01 1 as p30 at l(-9), dark, flip, zorder 6
show oc001_01 1 as p1 at r_exit(-2), light, zorder 5
c13 '[textdict[1120611]]'
hide p1
hide p30
show sc022_01 4 as p30 at l(-9), light, flip, zorder 6
c301 '[textdict[1120612]]'
hide p30
play sfx2 "other_7004.ogg"
c0 '[textdict[1120613]]'
show sc022_01 4 as p30 at l(-9), light, flip, zorder 6
c301 '[textdict[1120614]]'
hide p30
show sc022_01 4 as p30 at l(-9), light, flip, zorder 6
c301 '[textdict[1120615]]'
hide p30
show sc022_01 1 as p30 at l(-9), light, flip, zorder 6
c301 '[textdict[1120616]]'
return