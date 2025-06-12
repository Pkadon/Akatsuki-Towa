label avg25141:
stop music

scene placeholderbackground
with fade
play sfxvoice "avg_vocal_na06.ogg"
show oc001_01 18 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210438]]'
play sfxvoice "bcv_oc002_atk_01.ogg"
hide c1portrait
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210439]]'
hide c2portrait
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210440]]'
play sfx2 "other_7004.ogg"
hide c1portrait
c0 '[textdict[1210441]]'
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na05.ogg"
show oc001_01 7 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210442]]'
return