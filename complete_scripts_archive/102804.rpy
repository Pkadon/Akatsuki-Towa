label avg102804:
stop music

scene placeholderbackground
show sc020_01 1 as p28 at l(-10), light, zorder 6
window show
with fade_out
c281 '[textdict[1219724]]'
hide p28
show sc020_01 1 as p28 at l(-10), dark, zorder 6
show oc001_01 1 as p1 at r(-2), light, zorder 5
c13 '[textdict[1219725]]'
hide p28
hide p1
show oc001_01 1 as p1 at r(-2), dark, zorder 5
show sc020_01 4 as p28 at l(-10), light, zorder 6
c281 '[textdict[1219726]]'
menu:
    extend ""
    "[textdict[1219727]]":
        call avg102805
    "[textdict[1219728]]":
        call avg102806
    "[textdict[1219729]]":
        call avg102807
return