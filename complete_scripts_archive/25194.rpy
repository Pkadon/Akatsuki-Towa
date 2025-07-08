label avg25194:
stop music

scene placeholderbackground
show oc001_01 6 as p1 at mid(-2), light, zorder 5
window show
with fade_in
play sfx2 "fight_6025.ogg"
c13 '[textdict[1210652]]'
hide p1
show oc002_01 13 as p2 at mid(-3), light, zorder 5
play sfxvoice "avg_vocal_ch05.ogg"
c23 '[textdict[1210653]]'
hide p2
show oc001_01 7 as p1 at mid(-2), light, zorder 5
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1210654]]'
return