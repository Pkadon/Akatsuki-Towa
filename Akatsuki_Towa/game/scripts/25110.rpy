label avg25110:
stop music

scene placeholderbackground
with fade
play sfx2 "elc_5006.ogg"
play sfxvoice "bcv_oc001_hurt_01.ogg"
show oc001_01 12 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210326]]'
play sfxvoice "avg_vocal_ch06.ogg"
hide p1
show oc002_01 14 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1210327]]'
play sfxvoice "avg_vocal_na02.ogg"
hide p2
show oc001_01 7 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210328]]'
return