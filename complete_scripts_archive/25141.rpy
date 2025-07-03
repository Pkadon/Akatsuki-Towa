label avg25141:
stop music

scene placeholderbackground
with fade
play sfxvoice "avg_vocal_na06.ogg"
show oc001_01 18 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210438]]'
play sfxvoice "bcv_oc002_atk_01.ogg"
hide p1
show oc002_01 9 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1210439]]'
hide p2
show oc001_01 2 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210440]]'
play sfx2 "other_7004.ogg"
hide p1
c0 '[textdict[1210441]]'
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na05.ogg"
show oc001_01 7 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210442]]'
return