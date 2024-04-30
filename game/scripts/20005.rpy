label avg20005:
stop music

play music "ed9997.ogg"
scene placeholderbackground
with fade
play sfxvoice "bcv_oc001_hurt_02.ogg"
show oc001_01 19 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1000224)]]'
hide c1portrait
show oc002_01 5 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1000225)]]'
hide c2portrait
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1000226)]]'
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1000227)]]'
play sfxvoice "avg_vocal_ch31.ogg"
hide c1portrait
show oc002_01 20 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1000228)]]'
play sfx2 "common_remind.ogg"
hide c2portrait
c00 '[textdict[str(1000229)]]'
c00 '[textdict[str(1000230)]]'
return