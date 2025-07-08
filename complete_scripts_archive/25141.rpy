label avg25141:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfxvoice "avg_vocal_na06.ogg"
c13 '[textdict[1210438]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfxvoice "bcv_oc002_atk_01.ogg"
c23 '[textdict[1210439]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210440]]'
hide p1
play sfx2 "other_7004.ogg"
c0 '[textdict[1210441]]'
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1210442]]'
return