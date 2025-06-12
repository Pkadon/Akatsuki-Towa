label avg25218:
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6020.ogg"
play sfxvoice "bcv_oc002_hurt_02.ogg"
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210755]]'
hide c2portrait
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210756]]'
play sfxvoice "avg_vocal_ch25.ogg"
hide c1portrait
show oc002_01 21 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210757]]'
play sfxvoice "avg_vocal_na04.ogg"
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210758]]'
return