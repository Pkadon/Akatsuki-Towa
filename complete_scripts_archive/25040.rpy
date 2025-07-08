label avg25040:
stop music

scene placeholderbackground
show uc001_02 3 as p2001 at mid(6), light, zorder 5
window show
with fade_in
c20013 '[textdict[1210102]]'
hide p2001
show oc001_01 2 as p1 at mid(-2), light, zorder 5
c13 '[textdict[1210103]]'
hide p1
show uc001_02 2 as p2001 at mid(6), light, zorder 5
c20013 '[textdict[1210104]]'
menu:
    extend ""
    "[textdict[1214999]]":
        call avg25041
    "[textdict[1215000]]":
        call avg25000
return