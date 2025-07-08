label avg25121:
stop music

scene placeholderbackground
window show
with fade_in
play sfx2 "fight_6030.ogg"
c6123 '[textdict[1210356]]'
show oc002_01 12 as p2 at mid(-3), light, zorder 5
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1210357]]'
hide p2
show oc001_01 15 as p1 at mid(-2), light, zorder 5
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[textdict[1210358]]'
return