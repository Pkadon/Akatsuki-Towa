label avg25028:
stop music

scene placeholderbackground
show uc001_01 3 as p2000 at mid(-2), light, zorder 5
window show
with fade_out
c20003 '[textdict[1210068]]'
hide p2000
show oc001_01 2 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210069]]'
hide p1
show uc001_01 1 as p2000 at mid(-2), light, zorder 5
c20003 '[textdict[1210070]]'
menu:
    extend ""
    "[textdict[1214999]]":
        call avg25029
    "[textdict[1215000]]":
        call avg25000
return