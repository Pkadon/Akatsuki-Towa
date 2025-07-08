label avg25044:
stop music

scene placeholderbackground
show oc001_01 2 as p1 at mid(-2), light, zorder 5
window show
with fade_in
c13 '[textdict[1210111]]'
hide p1
show oc002_01 4 as p2 at mid(-3), light, zorder 5
play sfxvoice "avg_vocal_ch10.ogg"
c23 '[textdict[1210112]]'
hide p2
show oc001_01 19 as p1 at mid(-2), light, zorder 5
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc001_com_01.ogg"
c13 '[textdict[1210113]]'
return