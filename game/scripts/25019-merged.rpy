label avg25019:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
c20080 '[textdict[str(1210042)]]'
c20090 '[textdict[str(1210043)]]'
play sfxvoice "avg_vocal_ch12.ogg"
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210044)]]'
hide c2portrait
c20080 '[textdict[str(1210045)]]'
c20090 '[textdict[str(1210046)]]'
menu:
    "[textdict[str(1214999)]]":
        call avg25020
    "[textdict[str(1215000)]]":
        call avg25026
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210048)]]'
hide c1portrait
show oc002_01 1 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210049)]]'
hide c2portrait
show oc001_01 1 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210050)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7079.ogg"
c20100 '[textdict[str(1210051)]]'
c20100 '[textdict[str(1210052)]]'
play sfxvoice "bcv_oc001_sc01_01.ogg"
show oc001_01 20 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210053)]]'
play sfxvoice "avg_vocal_ch06.ogg"
hide c1portrait
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210054)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 4)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7086.ogg"
show oc002_01 1 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210055)]]'
hide c2portrait
c20100 '[textdict[str(1210056)]]'
show oc002_01 13 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210057)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 5)"
stop music

scene placeholderbackground
with fade
c20100 '[textdict[str(1210058)]]'
c20100 '[textdict[str(1210059)]]'
c20080 '[textdict[str(1210060)]]'
c20100 '[textdict[str(1210061)]]'
c20090 '[textdict[str(1210062)]]'
play sfxvoice "avg_vocal_ch05.ogg"
show oc002_01 13 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210063)]]'
play sfx2 "common_35rewardholy.ogg"
hide c2portrait
c20100 '[textdict[str(1210064)]]'
return