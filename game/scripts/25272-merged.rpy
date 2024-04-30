label avg25272:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7092.ogg"
c00 '[textdict[str(1211033)]]'
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211034)]]'
play sfxvoice "avg_vocal_ch08.ogg"
hide c1portrait
show oc002_01 6 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211035)]]'
play sfx2 "other_7080.ogg"
hide c2portrait
c00 '[textdict[str(1211036)]]'
play sfxvoice "avg_vocal_na05.ogg"
show oc001_01 7 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211037)]]'
play sfxvoice "bcv_oc002_atk_01.ogg"
hide c1portrait
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211038)]]'
play sfxvoice "avg_vocal_na03.ogg"
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211039)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7079.ogg"
show oc001_01 19 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211040)]]'
play sfx2 "other_7077.ogg"
play sfxvoice "avg_vocal_ch11.ogg"
hide c1portrait
show oc002_01 12 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211041)]]'
hide c2portrait
show oc001_01 18 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211042)]]'
menu:
    "[textdict[str(1214998)]]":
        call avg25274
    "[textdict[str(1214996)]]":
        call avg25275
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7077.ogg"
c20200 '[textdict[str(1211045)]]'
play sfx2 "other_7092.ogg"
c00 '[textdict[str(1211046)]]'
play sfxvoice "avg_vocal_ch08.ogg"
show oc002_01 14 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211047)]]'
play sfxvoice "avg_vocal_na17.ogg"
hide c2portrait
show oc001_01 22 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1211048)]]'
play sfx2 "other_7092.ogg"
hide c1portrait
c00 '[textdict[str(1211049)]]'
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_ch09.ogg"
show oc002_01 6 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1211050)]]'
return