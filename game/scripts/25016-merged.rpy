label avg25016:
scene placeholderbackground
nobody "(Scene 1)"
stop music

scene placeholderbackground
with fade
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210033)]]'
hide c1portrait
show oc002_01 4 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210034)]]'
hide c2portrait
show oc001_01 4 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210035)]]'
menu:
    "[textdict[str(1214999)]]":
        call avg25025
    "[textdict[str(1215000)]]":
        call avg25026
scene placeholderbackground
with fade
stop music
nobody "(Scene 2)"
stop music

scene placeholderbackground
with fade
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210036)]]'
play sfx2 "other_7079.ogg"
hide c2portrait
show oc001_01 9 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210037)]]'
hide c1portrait
show oc002_01 4 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210038)]]'
menu:
    "[textdict[str(1214998)]]":
        call avg25027
    "[textdict[str(1215000)]]":
        call avg25026
scene placeholderbackground
with fade
stop music
nobody "(Scene 3)"
stop music

scene placeholderbackground
with fade
show oc002_01 3 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210039)]]'
hide c2portrait
show oc001_01 3 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1210040)]]'
play sfx2 "common_36rewardsp.ogg"
hide c1portrait
show oc002_01 13 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1210041)]]'
return