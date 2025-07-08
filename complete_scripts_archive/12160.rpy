label avg12160:
stop music

play music "ed7104.ogg"
scene avg_bg_027
window show
with fade_out
c9621 '[textdict[1128430]]'
show oc001_01 8 as p1 at r(-2), light, zorder 5
c13 '[textdict[1128431]]'
hide p1
show oc001_01 8 as p1 at r(-2), dark, zorder 5
c9621 '[textdict[1128432]]'
scene avg_bg_028
show oc002_01 8 as p2 at l(-3), light, flip, zorder 6
with fade
play sfx2 "other_7021.ogg"
play sfxvoice "avg_vocal_ch08.ogg"
c21 '[textdict[1128433]]'
hide p2
show oc002_01 8 as p2 at l(-3), dark, flip, zorder 6
show oc003_01 14 as p3 at r(-6), light, zorder 5
c33 '[textdict[1128434]]'
hide p3
hide p2
show oc002_01 8 as p2 at l(-3), dark, flip, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1128436]]'
hide p2
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show oc002_01 6 as p2 at l(-3), light, flip, zorder 6
c21 '[textdict[1128437]]'
hide p2
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show oc002_01 16 as p2 at l(-3), light, flip, zorder 6
play sfxvoice "avg_vocal_ch25.ogg"
c21 '[textdict[1128438]]'
hide p1
hide p2
show oc002_01 16 as p2 at l(-3), dark, flip, zorder 6
show oc001_01 10 as p1 at r(-2), light, zorder 5
play sfxvoice "avg_vocal_na20.ogg"
c13 '[textdict[1128439]]'
return