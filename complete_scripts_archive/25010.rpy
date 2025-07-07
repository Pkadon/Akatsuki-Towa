label avg25010:
stop music

scene placeholderbackground
show uc001_01 1 as p587 at mid(-2), light, zorder 5
with fade
c5873 '[textdict[1210016]]'
hide p587
show oc001_01 2 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210017]]'
hide p1
show uc001_01 1 as p587 at mid(-2), light, zorder 5
c5873 '[textdict[1210018]]'
menu:
    extend ""
    "[textdict[1214999]]":
        call avg25011
    "[textdict[1215000]]":
        call avg25000
return