label avg12602:
stop music

play music "ED6200.ogg"
scene avg_bg_080
with fade
play sfxvoice "avg_vocal_ch19.ogg"
show oc002_01 17 as p2 at l_entrance(-3), light, zorder 6
c21 '[textdict[1161132]]'
hide p2
show oc002_01 17 as p2 at l(-3), dark, zorder 6
show oc001_01 1 as p1 at r_entrance(-2), light, zorder 5
c13 '[textdict[1161133]]'
hide p2
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
show oc002_01 1 as p2 at l(-3), light, zorder 6
c21 '[textdict[1161134]]'
hide p1
hide p2
show oc002_01 1 as p2 at l(-3), dark, zorder 6
show oc004_01 1 as p4 at r(-5), light, zorder 5
c43 '[textdict[1161135]]'
hide p2
hide p4
show oc004_01 1 as p4 at r(-5), dark, zorder 5
show oc002_01 23 as p2 at l(-3), light, zorder 6
c21 '[textdict[1161136]]'
play sfxvoice "avg_vocal_ro12.ogg"
hide p2
hide p4
show oc004_01 1 as p4 at r(-5), dark, zorder 5
show oc003_01 17 as p3 at l(-6), light, zorder 6
c31 '[textdict[1161137]]'
hide p4
hide p3
show oc003_01 17 as p3 at l(-6), dark, zorder 6
show oc001_01 8 as p1 at r(-2), light, zorder 5
c13 '[textdict[1161138]]'
hide p3
hide p1
show oc001_01 8 as p1 at r(-2), dark, zorder 5
show oc002_01 12 as p2 at l(-3), light, zorder 6
c21 '[textdict[1161139]]'
play sfx2 "fight_6025.ogg"
hide p2
hide p1
show oc001_01 8 as p1 at r(-2), dark, zorder 5
show oc003_01 5 as p3 at l(-6), light, zorder 6
c31 '[textdict[1161140]]'
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc001_com_01.ogg"
hide p1
hide p3
show oc003_01 5 as p3 at l(-6), dark, zorder 6
show oc001_01 4 as p1 at r(-2), light, zorder 5
c13 '[textdict[1161141]]'
return