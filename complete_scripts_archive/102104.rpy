label avg102104:
stop music

scene placeholderbackground
show sc013_01 1 as p21 at l(-12), light, flip, zorder 6
window show
with fade_out
c211 '[textdict[1218820]]'
hide p21
show sc013_01 4 as p21 at l(-12), light, flip, zorder 6
c211 '[textdict[1218821]]'
hide p21
show sc013_01 4 as p21 at l(-12), dark, flip, zorder 6
show oc001_01 10 as p1 at r(-2), light, zorder 5
c13 '[textdict[1218822]]'
menu:
    extend ""
    "[textdict[1218823]]":
        call avg102105
    "[textdict[1218824]]":
        call avg102106
    "[textdict[1218825]]":
        call avg102107
return