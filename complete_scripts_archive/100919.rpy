label avg100919:
stop music

scene placeholderbackground
show sc001_01 4 as p9 at mid(-11), light, zorder 5
window show
with fade_out
c93 '[textdict[1218061]]'
hide p9
show oc001_01 2 as p1 at mid(-2), light, zorder 5
play sfxvoice "bcv_oc002_get_02.ogg"
c13 '[textdict[1218062]]'
hide p1
show sc001_01 1 as p9 at mid(-11), light, zorder 5
c93 '[textdict[1218063]]'
hide p9
show oc001_01 4 as p1 at mid(-2), light, zorder 5
play sfxvoice "bcv_oc002_atk_01.ogg"
c13 '[textdict[1218064]]'
hide p1
show sc001_01 1 as p9 at mid(-11), light, zorder 5
c93 '[textdict[1218065]]'
hide p9
c0 '[textdict[1218066]]'
return