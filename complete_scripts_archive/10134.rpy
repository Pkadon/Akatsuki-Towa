label avg10134:
stop music

play music "ed7104.ogg"
scene avg_bg_014
window show
with fade_in
c0 '[textdict[1007359]]'
show oc002_01 23 as p2 at r(-3), light, zorder 5
play sfx2 "other_7064.ogg"
c23 '[textdict[1007360]]'
hide p2
show oc002_01 23 as p2 at r(-3), dark, zorder 5
show oc001_01 22 as p1 at l(-2), light, flip, zorder 6
play sfx2 "other_7072.ogg"
c11 '[textdict[1007361]]'
hide p2
hide p1
show oc001_01 22 as p1 at l(-2), dark, flip, zorder 6
show oc002_01 19 as p2 at r_exit(-3), light, zorder 5
play sfx2 "other_7085.ogg"
c23 '[textdict[1007362]]'
hide p2
scene avg_bg_030
show st004_01 2 as p204 at l(4), light, flip, zorder 6
with fade
play sfx2 "other_7088.ogg"
c2041 '[textdict[1001637]]'
hide p204
show st004_01 2 as p204 at l(4), dark, flip, zorder 6
show sc043_01 1 as p50 at r_entrance(-20), light, zorder 5
play sfx2 "other_7079.ogg"
c503 '[textdict[1001638]]'
hide p204
hide p50
show sc043_01 1 as p50 at r(-20), dark, zorder 5
show st004_01 1 as p204 at l(4), light, flip, zorder 6
c2041 '[textdict[1001639]]'
hide p50
hide p204
show st004_01 1 as p204 at l(4), dark, flip, zorder 6
show sc043_01 4 as p50 at r(-20), light, zorder 5
play sfx2 "other_7079.ogg"
c503 '[textdict[1001640]]'
hide p204
hide p50
show sc043_01 4 as p50 at r(-20), dark, zorder 5
show st004_01 2 as p204 at l(4), light, flip, zorder 6
c2041 '[textdict[1001641]]'
hide p204
hide p50
show sc043_01 4 as p50 at r(-20), dark, zorder 5
show st004_01 5 as p204 at l(4), light, flip, zorder 6
c2041 '[textdict[1001642]]'
hide p204
hide p50
show sc043_01 4 as p50 at r(-20), dark, zorder 5
show st004_01 1 as p204 at l(4), light, flip, zorder 6
play sfx2 "other_7088.ogg"
c2041 '[textdict[1001643]]'
hide p204
hide p50
show oc002_01 2 as p2 at mid(-3), light, zorder 5
with fade
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[textdict[1001644]]'
hide p2
show oc001_01 1 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1001645]]'
return