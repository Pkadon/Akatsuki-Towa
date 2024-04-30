label avg25150:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
show uc001_02 2 as c2014portrait at centerpos(6), zorder 5
c20142 '[textdict[str(1210478)]]'
menu:
    "[textdict[str(1214999)]]":
        call avg25151
    "[textdict[str(1214996)]]":
        call avg25026
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
play sfx2 "other_7086.ogg"
play sfxvoice "avg_vocal_na15.ogg"
show oc001_01 1 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210481)]]'
hide c1portrait
show oc002_01 2 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210482)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
play sfx2 "fight_6022.ogg"
play sfxvoice "avg_vocal_na03.ogg"
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210483)]]'
hide c1portrait
show oc002_01 1 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210484)]]'
hide c2portrait
show oc001_01 1 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210485)]]'
scene placeholderbackground
with fade
stop music
nobody "(Scene 4)"
stop music

scene placeholderbackground
with fade
show oc001_01 6 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210486)]]'
hide c1portrait
show uc001_02 1 as c2014portrait at centerpos(6), zorder 5
c20142 '[textdict[str(1210487)]]'
play sfxvoice "avg_vocal_ch05.ogg"
hide c2014portrait
show oc002_01 15 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210488)]]'
play sfx2 "common_35rewardholy.ogg"
hide c2portrait
show uc001_02 1 as c2014portrait at centerpos(6), zorder 5
c20142 '[textdict[str(1210489)]]'
return