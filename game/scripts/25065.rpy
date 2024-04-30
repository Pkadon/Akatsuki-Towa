label avg25065:
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6025.ogg"
play sfxvoice "avg_vocal_ch20.ogg"
show oc002_01 17 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210195)]]'
play sfx2 "fight_6016.ogg"
play sfxvoice "avg_vocal_ch27.ogg"
hide c2portrait
c00 '[textdict[str(1210196)]]'
play sfxvoice "avg_vocal_ch21.ogg"
show oc002_01 20 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210198)]]'
hide c2portrait
show oc001_01 8 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210199)]]'
hide c1portrait
show oc002_01 19 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210200)]]'
play sfxvoice "avg_vocal_na05.ogg"
hide c2portrait
show oc001_01 7 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210201)]]'
return