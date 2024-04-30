label avg25312:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7007.ogg"
play sfxvoice "bcv_oc002_hurt_02.ogg"
show oc002_01 20 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211199)]]'
play sfx2 "other_7057.ogg"
hide c2portrait
c00 '[textdict[str(1211200)]]'
c20150 '[textdict[str(1211201)]]'
menu:
    "[textdict[str(1214995)]]":
        call avg25313
    "[textdict[str(1214996)]]":
        call avg25026
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7027.ogg"
play sfxvoice "avg_vocal_na03.ogg"
show oc001_01 16 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211206)]]'
hide c1portrait
c20150 '[textdict[str(1211207)]]'
play sfxvoice "avg_vocal_na05.ogg"
show oc001_01 8 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211208)]]'
hide c1portrait
show oc002_01 1 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211209)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7051.ogg"
play sfxvoice "avg_vocal_ch06.ogg"
show oc002_01 14 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211210)]]'
play sfxvoice "avg_vocal_na16.ogg"
hide c2portrait
show oc001_01 6 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211211)]]'
hide c1portrait
show oc002_01 8 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211212)]]'
play sfx2 "other_7093.ogg"
hide c2portrait
c20150 '[textdict[str(1211213)]]'
play sfxvoice "avg_vocal_na18.ogg"
show oc001_01 22 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211214)]]'
hide c1portrait
c20150 '[textdict[str(1211215)]]'
play sfxvoice "avg_vocal_ch07.ogg"
show oc002_01 5 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211216)]]'
hide c2portrait
c20150 '[textdict[str(1211217)]]'
play sfx2 "other_7086.ogg"
c00 '[textdict[str(1211218)]]'
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_na02.ogg"
show oc001_01 7 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211219)]]'
return