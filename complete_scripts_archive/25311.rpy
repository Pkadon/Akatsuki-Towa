label avg25311:
stop music

scene placeholderbackground
window show
with fade_in
play sfx2 "other_7092.ogg"
c6123 '[textdict[1211191]]'
c6123 '[textdict[1211192]]'
play sfx2 "fight_6026.ogg"
c0 '[textdict[1211193]]'
show oc002_01 9 as p2 at mid(-3), light, zorder 5
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[textdict[1211194]]'
hide p2
show oc001_01 8 as p1 at mid(-2), light, zorder 5
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1211195]]'
hide p1
show oc002_01 5 as p2 at mid(-3), light, zorder 5
play sfxvoice "avg_vocal_ch07.ogg"
c23 '[textdict[1211196]]'
hide p2
show oc001_01 4 as p1 at mid(-2), light, zorder 5
play sfx2 "common_quest.ogg"
play sfxvoice "avg_vocal_na03.ogg"
c13 '[textdict[1211197]]'
return