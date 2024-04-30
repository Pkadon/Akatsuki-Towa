label avg25072:
stop music

scene placeholderbackground
with fade
play sfx2 "elc_5005.ogg"
play sfxvoice "avg_vocal_ch12.ogg"
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210225)]]'
play sfx2 "other_7034.ogg"
hide c2portrait
show oc001_01 18 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210226)]]'
return