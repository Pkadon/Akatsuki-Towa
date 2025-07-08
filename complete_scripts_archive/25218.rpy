label avg25218:
stop music

scene placeholderbackground
show oc002_01 12 as p2 at mid(-3), light, zorder 5
window show
with fade_in
play sfx2 "fight_6020.ogg"
play sfxvoice "bcv_oc002_hurt_02.ogg"
c23 '[textdict[1210755]]'
hide p2
show oc001_01 2 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210756]]'
hide p1
show oc002_01 21 as p2 at mid(-3), light, zorder 5
play sfxvoice "avg_vocal_ch25.ogg"
c23 '[textdict[1210757]]'
hide p2
show oc001_01 4 as p1 at mid(-2), light, zorder 5
play sfxvoice "avg_vocal_na04.ogg"
c13 '[textdict[1210758]]'
return