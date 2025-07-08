label avg22367:
stop music

play music "ed7202.ogg"
scene placeholderbackground
show oc001_01 2 as p1 at r(-2), light, zorder 5
window show
with fade_out
c13 '[textdict[1133821]]'
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show oc002_01 8 as p2 at l(-3), light, flip, zorder 6
c21 '[textdict[1133822]]'
hide p1
hide p2
show oc002_01 8 as p2 at l(-3), dark, flip, zorder 6
show oc001_01 1 as p1 at r_exit(-2), light, zorder 5
c13 '[textdict[1133823]]'
hide p1
scene avg_bg_070
show oc002_01 6 as p2 at l(-3), light, flip, zorder 6
with fade
play sfx2 "other_7050.ogg"
c21 '[textdict[1133824]]'
scene placeholderbackground
with fade
show oc001_01 2 as p1 at r_entrance(-2), light, zorder 5
c13 '[textdict[1133825]]'
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show oc002_01 8 as p2 at l(-3), l_shake, light, flip, zorder 6
play sfxvoice "avg_vocal_ch06.ogg"
c21 '[textdict[1133826]]'
hide p1
hide p2
show oc002_01 8 as p2 at l(-3), dark, flip, zorder 6
show oc001_01 5 as p1 at r(-2), light, zorder 5
c13 '[textdict[1133827]]'
hide p2
hide p1
play sfx2 "other_7092.ogg"
c0 '[textdict[1133828]]'
show oc002_01 2 as p2 at l(-3), light, flip, zorder 6
c21 '[textdict[1133829]]'
hide p2
show oc002_01 2 as p2 at l(-3), dark, flip, zorder 6
show oc001_01 1 as p1 at r(-2), light, zorder 5
c13 '[textdict[1133830]]'
return