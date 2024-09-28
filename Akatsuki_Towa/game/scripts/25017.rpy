label avg25017:
stop music

scene placeholderbackground
with fade
show oc002_01 9 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210036]]'
play sfx2 "other_7079.ogg"
hide c2portrait
show oc001_01 9 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210037]]'
hide c1portrait
show oc002_01 4 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1210038]]'
menu:
    "[textdict[1214998]]":
        call avg25027
    "[textdict[1215000]]":
        call avg25026
return