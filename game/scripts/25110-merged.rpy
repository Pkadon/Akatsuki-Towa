label avg25110:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
play sfx2 "elc_5006.ogg"
play sfxvoice "bcv_oc001_hurt_01.ogg"
show oc001_01 12 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210326)]]'
play sfxvoice "avg_vocal_ch06.ogg"
hide c1portrait
show oc002_01 14 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210327)]]'
play sfxvoice "avg_vocal_na02.ogg"
hide c2portrait
show oc001_01 7 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210328)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
play sfx2 "elc_5002.ogg"
play sfxvoice "bcv_oc002_hurt_01.ogg"
show oc002_01 3 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210329)]]'
hide c2portrait
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210330)]]'
play sfxvoice "avg_vocal_ch31.ogg"
hide c1portrait
show oc002_01 7 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210331)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7092.ogg"
show oc001_01 6 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210332)]]'
hide c1portrait
show oc002_01 8 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210333)]]'
play sfxvoice "avg_vocal_na05.ogg"
hide c2portrait
show oc001_01 7 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210334)]]'
hide c1portrait
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210335)]]'
play sfx2 "common_35rewardholy.ogg"
hide c2portrait
show oc001_01 11 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210336)]]'
return