label avg25090:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7080.ogg"
play sfxvoice "bcv_oc002_hurt_01.ogg"
show oc002_01 3 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210256)]]'
play sfxvoice "bcv_oc001_hurt_02.ogg"
hide c2portrait
show oc001_01 19 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210257)]]'
hide c1portrait
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210258)]]'
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210259)]]'
menu:
    "[textdict[str(1214997)]]":
        call avg25091
    "[textdict[str(1215000)]]":
        call avg25026
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
show oc002_01 4 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210261)]]'
play sfxvoice "avg_vocal_na03.ogg"
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210262)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7079.ogg"
show oc002_01 21 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210263)]]'
play sfxvoice "avg_vocal_na07.ogg"
hide c2portrait
show oc001_01 3 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210264)]]'
play sfx2 "fight_6024.ogg"
hide c1portrait
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210265)]]'
menu:
    "[textdict[str(1214998)]]":
        call avg25094
    "[textdict[str(1215000)]]":
        call avg25026
scene placeholderbackground
with fade
stop music
nobody "(Scene 4)"
stop music

scene placeholderbackground
with fade
play sfxvoice "avg_vocal_na05.ogg"
show oc001_01 8 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210267)]]'
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_ch05.ogg"
hide c1portrait
show oc002_01 13 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210268)]]'
return