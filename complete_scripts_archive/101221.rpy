label avg101221:
stop music

scene placeholderbackground
show sc004_01 4 as p12 at l(-12), light, zorder 6
with fade
c121 '[textdict[1220719]]'
hide p12
show sc004_01 4 as p12 at l(-12), dark, zorder 6
show oc001_01 12 as p1 at r(-2), light, zorder 5
c13 '[textdict[1220720]]'
hide p12
hide p1
show oc001_01 12 as p1 at r(-2), dark, zorder 5
show sc004_01 3 as p12 at l(-12), light, zorder 6
c121 '[textdict[1220721]]'
hide p1
hide p12
show sc004_01 3 as p12 at l(-12), dark, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1220722]]'
menu:
    extend ""
    "[textdict[1220723]]":
        call avg101222
    "[textdict[1220724]]":
        call avg101223
    "[textdict[1220725]]":
        call avg101224
return