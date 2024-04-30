label avg25293:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7007.ogg"
play sfxvoice "bcv_oc002_hurt_02.ogg"
show oc002_01 20 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211117)]]'
play sfx2 "other_7057.ogg"
hide c2portrait
c00 '[textdict[str(1211118)]]'
c20150 '[textdict[str(1211119)]]'
menu:
    "[textdict[str(1214995)]]":
        call avg25294
    "[textdict[str(1214996)]]":
        call avg25026
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7088.ogg"
play sfxvoice "bcv_oc001_hurt_01.ogg"
show oc001_01 19 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211125)]]'
play sfxvoice "bcv_oc002_com_01.ogg"
hide c1portrait
show oc002_01 4 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211126)]]'
play sfx2 "elc_5002.ogg"
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211127)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7088.ogg"
play sfxvoice "avg_vocal_ch23.ogg"
show oc002_01 3 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211128)]]'
play sfxvoice "avg_vocal_na10.ogg"
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211129)]]'
play sfxvoice "avg_vocal_ch12.ogg"
hide c1portrait
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211130)]]'
hide c2portrait
c20150 '[textdict[str(1211131)]]'
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211132)]]'
play sfx2 "other_7093.ogg"
hide c1portrait
c00 '[textdict[str(1211133)]]'
c20150 '[textdict[str(1211134)]]'
show oc002_01 4 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211135)]]'
hide c2portrait
c20150 '[textdict[str(1211136)]]'
play sfx2 "other_7086.ogg"
c00 '[textdict[str(1211137)]]'
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na05.ogg"
show oc001_01 8 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211138)]]'
return