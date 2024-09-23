label avg25067:
stop music

scene placeholderbackground
with fade
show oc002_01 4 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210202]]'
play sfx2 "fight_6025.ogg"
hide c2portrait
show oc001_01 12 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210203]]'
play sfx2 "fight_6028.ogg"
play sfxvoice "bcv_oc002_hurt_02.ogg"
hide c1portrait
c00 '[textdict[1210204]]'
play sfxvoice "avg_vocal_ch25.ogg"
show oc002_01 21 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210205]]'
hide c2portrait
show oc001_01 8 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210206]]'
play sfxvoice "bcv_oc002_atk_01.ogg"
hide c1portrait
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210207]]'
play sfxvoice "avg_vocal_na02.ogg"
hide c2portrait
show oc001_01 7 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210208]]'
return