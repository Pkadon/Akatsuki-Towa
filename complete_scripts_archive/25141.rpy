label avg25141:
stop music

scene placeholderbackground
with fade
show oc001_01 18 as p1 at mid(-2), light, zorder 5
play sfxvoice "avg_vocal_na06.ogg"
c13 '[textdict[1210438]]'
hide p1
show oc002_01 9 as p2 at mid(-3), light, zorder 5
play sfxvoice "bcv_oc002_atk_01.ogg"
c23 '[textdict[1210439]]'
hide p2
show oc001_01 2 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210440]]'
hide p1
play sfx2 "other_7004.ogg"
c0 '[textdict[1210441]]'
show oc001_01 7 as p1 at mid(-2), light, zorder 5
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1210442]]'
return