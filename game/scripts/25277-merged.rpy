label avg25277:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
c20150 '[textdict[str(1211052)]]'
menu:
    "[textdict[str(1214995)]]":
        call avg25278
    "[textdict[str(1214996)]]":
        call avg25026
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
play sfx2 "common_tag_2.ogg"
play sfxvoice "bcv_oc001_arts_02.ogg"
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211060)]]'
hide c1portrait
show oc002_01 1 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211061)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
play sfx2 "common_tag_2.ogg"
play sfxvoice "avg_vocal_ch08.ogg"
show oc002_01 6 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211062)]]'
hide c2portrait
show oc001_01 11 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211063)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 4)"
stop music

scene placeholderbackground
with fade
play sfx2 "common_tag_2.ogg"
show oc001_01 18 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211064)]]'
play sfxvoice "avg_vocal_ch20.ogg"
hide c1portrait
show oc002_01 10 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211065)]]'
hide c2portrait
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211066)]]'
hide c1portrait
show oc002_01 21 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211067)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 5)"
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6025.ogg"
show oc001_01 1 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211068)]]'
hide c1portrait
c20150 '[textdict[str(1211069)]]'
play sfx2 "fight_6010.ogg"
play sfxvoice "bcv_oc002_atk_01.ogg"
show oc002_01 19 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211070)]]'
play sfx2 "other_7057.ogg"
hide c2portrait
c20150 '[textdict[str(1211071)]]'
play sfxvoice "avg_vocal_ch25.ogg"
show oc002_01 21 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211072)]]'
hide c2portrait
c20150 '[textdict[str(1211073)]]'
play sfx2 "other_7086.ogg"
c00 '[textdict[str(1211074)]]'
play sfxvoice "avg_vocal_na05.ogg"
show oc001_01 8 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211075)]]'
return