label avg25016:
stop music

scene placeholderbackground
show oc001_01 4 as p1 at mid(-2), light, zorder 5
with fade
c13 '[textdict[1210033]]'
hide p1
show oc002_01 4 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1210034]]'
hide p2
show oc001_01 4 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210035]]'
menu:
    extend ""
    "[textdict[1214999]]":
        call avg25025
    "[textdict[1215000]]":
        call avg25026
return