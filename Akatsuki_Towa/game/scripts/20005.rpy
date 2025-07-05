label avg20005:
stop music

play music "ed9997.ogg"
scene placeholderbackground
with fade
play sfxvoice "bcv_oc001_hurt_02.ogg"
show oc001_01 19 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1000224]]'
hide p1
show oc002_01 5 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1000225]]'
hide p2
show oc002_01 9 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1000226]]'
hide p2
show oc001_01 4 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1000227]]'
play sfxvoice "avg_vocal_ch31.ogg"
hide p1
show oc002_01 20 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1000228]]'
hide p2
play sfx2 "common_remind.ogg"
c0 '[textdict[1000229]]'
c0 '[textdict[1000230]]'
return