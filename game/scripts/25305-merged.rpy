label avg25305:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7080.ogg"
c00 '[textdict[str(1211175)]]'
play sfxvoice "bcv_oc002_hurt_02.ogg"
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211176)]]'
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211177)]]'
play sfxvoice "bcv_oc002_arts_03.ogg"
hide c1portrait
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211178)]]'
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211179)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6015.ogg"
c00 '[textdict[str(1211180)]]'
play sfxvoice "avg_vocal_ch11.ogg"
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211181)]]'
play sfxvoice "bcv_oc001_hurt_02.ogg"
hide c2portrait
show oc001_01 19 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211182)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7079.ogg"
show oc002_01 4 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211183)]]'
hide c2portrait
show oc001_01 18 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211184)]]'
menu:
    "[textdict[str(1214998)]]":
        call avg25308
    "[textdict[str(1214996)]]":
        call avg25309
scene placeholderbackground
with fade
stop music
nobody "(Scene 4)"
stop music

scene placeholderbackground
with fade
play sfxvoice "avg_vocal_ch23.ogg"
show oc002_01 3 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211187)]]'
play sfxvoice "avg_vocal_na03.ogg"
hide c2portrait
show oc001_01 18 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211188)]]'
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "bcv_oc002_atk_01.ogg"
hide c1portrait
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211189)]]'
return