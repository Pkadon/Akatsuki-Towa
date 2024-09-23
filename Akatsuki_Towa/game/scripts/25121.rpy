label avg25121:
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6030.ogg"
c6120 '[textdict[1210356]]'
play sfxvoice "avg_vocal_ch11.ogg"
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210357]]'
play sfxvoice "bcv_oc001_hurt_02.ogg"
hide c2portrait
show oc001_01 15 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210358]]'
return