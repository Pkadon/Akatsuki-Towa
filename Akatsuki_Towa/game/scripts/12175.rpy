label avg12175:
stop music

play music "ED6505.ogg"
scene avg_bg_027
with fade
play sfxvoice "avg_vocal_na04_b.ogg"
show oc001_01 8 as p1 at r(-2), light, zorder 5
c13 '[textdict[1120523]]'
hide p1
show oc001_01 8 as p1 at r(-2), dark, zorder 5
show oc003_01 5 as p3 at l(-6), light, zorder 5
c31 '[textdict[1120524]]'
play sfxvoice "avg_vocal_ch08.ogg"
hide p1
hide p3
show oc003_01 5 as p3 at l(-6), dark, zorder 6
show oc002_01 6 as p2 at r(-3), light, zorder 5
c23 '[textdict[1120525]]'
hide p3
hide p2
show oc002_01 6 as p2 at r(-3), dark, zorder 5
show oc003_01 14 as p3 at l(-6), light, zorder 5
c31 '[textdict[1120526]]'
hide p2
hide p3
show oc003_01 14 as p3 at l(-6), dark, zorder 6
show oc002_01 17 as p2 at r(-3), light, zorder 5
c23 '[textdict[1120527]]'
play sfxvoice "avg_vocal_na02.ogg"
hide p3
hide p2
show oc002_01 17 as p2 at r(-3), dark, zorder 5
show oc001_01 7 as p1 at l(-2), light, zorder 5
c11 '[textdict[1120528]]'
return