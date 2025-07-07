label avg101721:
stop music

scene placeholderbackground
show oc001_01 1 as p1 at r(-2), light, zorder 5
with fade
c13 '[textdict[1221932]]'
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
show sc009_01 1 as p17 at l(-13), light, zorder 6
c171 '[textdict[1221933]]'
hide p1
hide p17
show sc009_01 1 as p17 at l(-13), dark, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1221934]]'
menu:
    extend ""
    "[textdict[1221935]]":
        call avg101722
    "[textdict[1221936]]":
        call avg101723
    "[textdict[1221937]]":
        call avg101724
return