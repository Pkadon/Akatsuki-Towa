label avg20040:
stop music

play music "ed7151.ogg"
scene placeholderbackground
with fade
show sc027_01 1 as p35 at r_exit(-10), light, zorder 5
play sfx2 "other_7085.ogg"
c353 '[textdict[1002424]]'
hide p35
show oc003_01 4 as p3 at l(-6), light, zorder 6
c31 '[textdict[1002425]]'
hide p3
show oc003_01 4 as p3 at l(-6), dark, zorder 6
show oc001_01 4 as p1 at r_entrance(-2), light, zorder 5
c13 '[textdict[1002426]]'
hide p3
hide p1
show oc001_01 4 as p1 at r(-2), dark, zorder 5
show oc002_01 4 as p2 at l(-3), l_shake, light, zorder 6
c21 '[textdict[1002427]]'
return