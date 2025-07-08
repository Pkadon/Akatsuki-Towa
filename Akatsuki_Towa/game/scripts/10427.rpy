label avg10427:
stop music

play music "ed7511.ogg"
scene placeholderbackground
window show
with fade_in
c0 '[textdict[1141272]]'
show oc001_01 13 as p1 at r(-2), light, zorder 5
c13 '[textdict[1141273]]'
hide p1
show oc001_01 3 as p1 at r(-2), l_shake, light, zorder 5
play sfxvoice "avg_vocal_na07.ogg"
c13 '[textdict[1141274]]'
hide p1
show oc001_01 3 as p1 at r(-2), dark, zorder 5
c11091 '[textdict[1141275]]'
hide p1
show oc001_01 3 as p1 at r(-2), light, zorder 5
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[textdict[1141276]]'
hide p1
show oc001_01 3 as p1 at r(-2), dark, zorder 5
show oc002_01 9 as p2 at l_entrance(-3), light, flip, zorder 6
c21 '[textdict[1141277]]'
hide p2
hide p1
show oc001_01 3 as p1 at r(-2), dark, zorder 5
show oc004_01 12 as p4 at l_entrance(-5), light, flip, zorder 6
play sfxvoice "avg_vocal_li11.ogg"
c41 '[textdict[1141278]]'
hide p1
hide p4
show oc004_01 12 as p4 at l(-5), dark, flip, zorder 6
show oc001_01 9 as p1 at r(-2), light, zorder 5
c13 '[textdict[1141279]]'
hide p4
hide p1
show oc001_01 9 as p1 at r(-2), dark, zorder 5
show oc003_01 2 as p3 at l(-6), light, flip, zorder 6
play sfxvoice "avg_vocal_ro09.ogg"
c31 '[textdict[1141280]]'
hide p1
hide p3
show oc003_01 2 as p3 at l(-6), dark, flip, zorder 6
show oc001_01 3 as p1 at r(-2), light, zorder 5
c13 '[textdict[1141281]]'
hide p3
hide p1
show oc001_01 3 as p1 at r(-2), dark, zorder 5
play sfx2 "other_7007.ogg"
c11091 '[textdict[1141282]]' with shake
return