label avg25028:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
show uc001_01 3 as c2000portrait at centerpos(-2), zorder 5
c20002 '[textdict[str(1210068)]]'
hide c2000portrait
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210069)]]'
hide c1portrait
show uc001_01 1 as c2000portrait at centerpos(-2), zorder 5
c20002 '[textdict[str(1210070)]]'
menu:
    "[textdict[str(1214999)]]":
        call avg25029
    "[textdict[str(1215000)]]":
        call avg25000
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210074)]]'
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210075)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
show oc002_01 8 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210076)]]'
play sfx2 "other_7079.ogg"
play sfxvoice "avg_vocal_na23.ogg"
hide c2portrait
show oc001_01 20 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210077)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 4)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7086.ogg"
play sfxvoice "avg_vocal_na05.ogg"
show oc001_01 8 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210078)]]'
play sfx2 "fight_6025.ogg"
hide c1portrait
show oc002_01 4 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210079)]]'
play sfx2 "other_7034.ogg"
hide c2portrait
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210080)]]'
play sfxvoice "avg_vocal_ch07.ogg"
hide c2portrait
show oc002_01 5 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210081)]]'
hide c2portrait
show oc001_01 1 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210082)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 5)"
stop music

scene placeholderbackground
with fade
show oc001_01 6 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210083)]]'
hide c1portrait
show uc001_01 1 as c2000portrait at centerpos(-2), zorder 5
c20002 '[textdict[str(1210084)]]'
hide c2000portrait
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210085)]]'
play sfx2 "common_35rewardholy.ogg"
hide c1portrait
show uc001_01 1 as c2000portrait at centerpos(-2), zorder 5
c20002 '[textdict[str(1210086)]]'
return