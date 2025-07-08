label avg101904:
stop music

scene placeholderbackground
show oc001_01 6 as p1 at r(-2), light, zorder 5
window show
with fade_in
c13 '[textdict[1218333]]'
hide p1
show oc001_01 6 as p1 at r(-2), dark, zorder 5
show sc011_01 5 as p19 at l(-1), light, flip, zorder 6
c191 '[textdict[1218334]]'
hide p19
hide p1
show oc001_01 6 as p1 at r(-2), dark, zorder 5
show sc011_01 5 as p19 at l(-1), light, flip, zorder 6
c191 '[textdict[1218335]]'
menu:
    extend ""
    "[textdict[1218336]]":
        call avg101905
    "[textdict[1218337]]":
        call avg101906
    "[textdict[1218338]]":
        call avg101907
return