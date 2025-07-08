label avg102825:
stop music

scene placeholderbackground
show sc020_01 1 as p28 at l(-10), light, flip, zorder 6
window show
with fade_in
c281 '[textdict[1219788]]'
hide p28
show sc020_01 4 as p28 at l(-10), light, flip, zorder 6
c281 '[textdict[1219789]]'
hide p28
show sc020_01 4 as p28 at l(-10), dark, flip, zorder 6
show oc001_01 17 as p1 at r(-2), light, zorder 5
c13 '[textdict[1219790]]'
menu:
    extend ""
    "[textdict[1219791]]":
        call avg102826
    "[textdict[1219792]]":
        call avg102827
    "[textdict[1219793]]":
        call avg102828
return