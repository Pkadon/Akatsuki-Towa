label avg25034:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210087)]]'
play sfxvoice "avg_vocal_ch12.ogg"
hide c1portrait
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210088)]]'
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210089)]]'
hide c1portrait
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210090)]]'
hide c2portrait
show oc001_01 18 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210091)]]'
menu:
    "[textdict[str(1214997)]]":
        call avg25035
    "[textdict[str(1215000)]]":
        call avg25026
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7080.ogg"
play sfxvoice "bcv_oc002_hurt_02.ogg"
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210093)]]'
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210094)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7079.ogg"
play sfxvoice "avg_vocal_ch11.ogg"
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210095)]]'
hide c2portrait
show oc001_01 19 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210096)]]'
play sfx2 "fight_6024.ogg"
hide c1portrait
show oc002_01 4 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210097)]]'
menu:
    "[textdict[str(1214998)]]":
        call avg25038
    "[textdict[str(1215000)]]":
        call avg25026
scene placeholderbackground
with fade
stop music
nobody "(Scene 4)"
stop music

scene placeholderbackground
with fade
show oc002_01 11 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210099)]]'
hide c2portrait
show oc001_01 8 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210100)]]'
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "bcv_oc002_win_02.ogg"
hide c1portrait
show oc002_01 8 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210101)]]'
return