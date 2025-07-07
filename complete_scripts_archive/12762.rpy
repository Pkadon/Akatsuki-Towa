label avg12762:
stop music

scene avg_bg_201
with fade
play sfx2 "other_7060.ogg"
c0 '[textdict[1174603]]'
show oc001_01 4 as p1 at r_entrance(-2), light, zorder 5
c13 '[textdict[1174604]]'
play music "ed7511.ogg"
hide p1
show oc001_01 4 as p1 at r(-2), dark, zorder 5
c14521 '[textdict[1174605]]' with shake
hide p1
show oc001_01 4 as p1 at r(-2), dark, zorder 5
show oc002_01 2 as p2 at l(-3), light, zorder 6
c21 '[textdict[1174606]]'
hide p1
hide p2
show oc002_01 2 as p2 at l(-3), dark, zorder 6
show oc001_01 4 as p1 at r(-2), light, zorder 5
c13 '[textdict[1174607]]'
hide p2
hide p1
show oc001_01 4 as p1 at r(-2), dark, zorder 5
show oc002_01 14 as p2 at l(-3), light, zorder 6
c21 '[textdict[1174608]]'
hide p1
hide p2
show oc002_01 14 as p2 at l(-3), dark, zorder 6
show st061_01 4 as p1304 at r(-2), light, zorder 5
play sfx2 "fight_6002.ogg"
c13043 '[textdict[1174609]]'
hide p2
hide p1304
show st061_01 4 as p1304 at r(-2), dark, zorder 5
show oc003_01 4 as p3 at l(-6), light, zorder 6
play sfx2 "fight_6025.ogg"
c31 '[textdict[1174610]]'
hide p1304
hide p3
show oc003_01 4 as p3 at l(-6), dark, zorder 6
show oc001_01 20 as p1 at r(-2), light, zorder 5
play sfx2 "fight_6024.ogg"
c13 '[textdict[1174611]]'
hide p3
hide p1
show oc001_01 20 as p1 at r(-2), dark, zorder 5
show oc002_01 9 as p2 at l(-3), light, zorder 6
c21 '[textdict[1174612]]'
return