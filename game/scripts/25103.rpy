label avg25103:
stop music

scene placeholderbackground
with fade
play sfx2 "common_select.ogg"
play sfxvoice "bcv_oc002_c02_01.ogg"
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210290)]]'
play sfxvoice "avg_vocal_na02.ogg"
hide c2portrait
show oc001_01 7 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210291)]]'
hide c1portrait
show oc001_01 21 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210292)]]'
hide c1portrait
c20070 '[textdict[str(1210293)]]'
return