label avg25040:
stop music

scene placeholderbackground
with fade
show uc001_02 3 as c2001portrait at centerpos(6), zorder 5
c20013 '[textdict[1210102]]'
hide c2001portrait
show oc001_01 2 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1210103]]'
hide c1portrait
show uc001_02 2 as c2001portrait at centerpos(6), zorder 5
c20013 '[textdict[1210104]]'
menu:
    extend ""
    "[textdict[1214999]]":
        call avg25041
    "[textdict[1215000]]":
        call avg25000
return