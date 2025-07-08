label avg101104:
stop music

scene placeholderbackground
show oc001_01 10 as p1 at r(-2), light, zorder 5
window show
with fade_out
c13 '[textdict[1220399]]'
hide p1
show oc001_01 10 as p1 at r(-2), dark, zorder 5
show sc003_01 6 as p11 at l(-4), light, flip, zorder 6
c111 '[textdict[1220400]]'
hide p1
hide p11
show sc003_01 6 as p11 at l(-4), dark, flip, zorder 6
show oc001_01 18 as p1 at r(-2), light, zorder 5
c13 '[textdict[1220401]]'
menu:
    extend ""
    "[textdict[1220402]]":
        call avg101105
    "[textdict[1220403]]":
        call avg101106
    "[textdict[1220404]]":
        call avg101107
return