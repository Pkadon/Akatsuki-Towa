label avg25017:
stop music

scene placeholderbackground
with fade
show oc002_01 9 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1210036]]'
hide p2
show oc001_01 9 as p1 at mid(-2), light, zorder 5
play sfx2 "other_7079.ogg"
c13 '[textdict[1210037]]'
hide p1
show oc002_01 4 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1210038]]'
menu:
    extend ""
    "[textdict[1214998]]":
        call avg25027
    "[textdict[1215000]]":
        call avg25026
return