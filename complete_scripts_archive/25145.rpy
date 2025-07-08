label avg25145:
stop music

scene placeholderbackground
window show
with fade_in
play sfx2 "fight_6017.ogg"
c0 '[textdict[1210459]]'
show oc002_01 8 as p2 at mid(-3), light, zorder 5
play sfx2 "other_7092.ogg"
play sfxvoice "avg_vocal_ch09.ogg"
c23 '[textdict[1210460]]'
hide p2
show oc001_01 7 as p1 at mid(-2), light, zorder 5
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na03.ogg"
c13 '[textdict[1210461]]'
return