label avg12541:
stop music

play music "ED6200.ogg"
scene avg_bg_010
with fade
c0 '[textdict[1152919]]'
show oc003_01 4 as p3 at l(-6), light, zorder 6
c31 '[textdict[1152920]]'
play sfxvoice "avg_vocal_ch19.ogg"
hide p3
show oc003_01 4 as p3 at l(-6), dark, zorder 6
show oc002_01 10 as p2 at r(-3), light, zorder 5
c23 '[textdict[1152921]]'
hide p3
hide p2
show oc002_01 10 as p2 at r(-3), dark, zorder 5
show oc004_01 4 as p4 at l(-5), light, zorder 6
c41 '[textdict[1152922]]'
return