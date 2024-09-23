label avg25110:
stop music

scene placeholderbackground
with fade
play sfx2 "elc_5006.ogg"
play sfxvoice "bcv_oc001_hurt_01.ogg"
show oc001_01 12 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210326]]'
play sfxvoice "avg_vocal_ch06.ogg"
hide c1portrait
show oc002_01 14 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[1210327]]'
play sfxvoice "avg_vocal_na02.ogg"
hide c2portrait
show oc001_01 7 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[1210328]]'
return