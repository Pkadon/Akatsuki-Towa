label avg101121:
stop music

scene placeholderbackground
show oc001_01 1 as p1 at r(-2), light, zorder 5
window show
with fade_out
c13 '[textdict[1220446]]'
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
show sc003_01 2 as p11 at l(-4), light, flip, zorder 6
c111 '[textdict[1220447]]'
hide p1
hide p11
show sc003_01 2 as p11 at l(-4), dark, flip, zorder 6
show oc001_01 10 as p1 at r(-2), light, zorder 5
c13 '[textdict[1220448]]'
menu:
    extend ""
    "[textdict[1220449]]":
        call avg101122
    "[textdict[1220450]]":
        call avg101123
    "[textdict[1220451]]":
        call avg101124
return