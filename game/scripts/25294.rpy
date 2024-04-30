label avg25294:
stop music

scene placeholderbackground
with fade
play sfx2 "common_select.ogg"
play sfxvoice "avg_vocal_ch12.ogg"
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211120)]]'
play sfxvoice "avg_vocal_na03.ogg"
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211121)]]'
hide c1portrait
c20150 '[textdict[str(1211122)]]'
c20150 '[textdict[str(1211123)]]'
play sfx2 "other_7085.ogg"
play sfxvoice "bcv_oc002_c02_01.ogg"
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211124)]]'
return