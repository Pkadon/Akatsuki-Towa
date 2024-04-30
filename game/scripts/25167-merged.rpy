label avg25167:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210547)]]'
menu:
    "[textdict[str(1214997)]]":
        call avg25168
    "[textdict[str(1214996)]]":
        call avg25026
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
play sfxvoice "avg_vocal_ch12.ogg"
show oc002_01 17 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210548)]]'
hide c2portrait
show oc001_01 12 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210549)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
play sfxvoice "avg_vocal_na07.ogg"
show oc001_01 19 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210550)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 4)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7092.ogg"
play sfxvoice "avg_vocal_na04.ogg"
show oc001_01 8 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210551)]]'
hide c1portrait
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210552)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 5)"
stop music

scene placeholderbackground
with fade
play sfx2 "common_35rewardholy.ogg"
show oc001_01 6 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210553)]]'
return