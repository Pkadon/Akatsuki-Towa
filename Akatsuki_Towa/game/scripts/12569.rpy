label avg12569:
stop music

play music "ED6200.ogg"
scene avg_bg_010
with fade
play sfxvoice "avg_vocal_li07.ogg"
show oc004_01 5 as p4 at l(-5), l_shake, light, zorder 5
c41 '[textdict[1155140]]'
hide p4
show oc004_01 5 as p4 at l(-5), dark, zorder 6
show oc002_01 16 as p2 at r(-3), light, zorder 5
c23 '[textdict[1155141]]'
play sfxvoice "avg_vocal_ch09.ogg"
hide p2
hide p4
show oc004_01 5 as p4 at l(-5), dark, zorder 6
show oc002_01 14 as p2 at r(-3), r_shake, light, zorder 5
c23 '[textdict[1155142]]'
hide p4
hide p2
show oc002_01 14 as p2 at r(-3), dark, zorder 5
show oc003_01 17 as p3 at l(-6), light, zorder 5
c31 '[textdict[1155143]]'
play sfxvoice "avg_vocal_na20.ogg"
hide p2
hide p3
show oc003_01 17 as p3 at l(-6), dark, zorder 6
show oc001_01 10 as p1 at r(-2), light, zorder 5
c13 '[textdict[1155144]]'
return