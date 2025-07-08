label avg101921:
stop music

scene placeholderbackground
show sc011_01 2 as p19 at l(-1), light, flip, zorder 6
window show
with fade_out
c191 '[textdict[1218383]]'
hide p19
show sc011_01 2 as p19 at l(-1), dark, flip, zorder 6
show oc001_01 23 as p1 at r(-2), light, zorder 5
c13 '[textdict[1218384]]'
hide p19
hide p1
show oc001_01 23 as p1 at r(-2), dark, zorder 5
show sc011_01 4 as p19 at l(-1), light, flip, zorder 6
c191 '[textdict[1218385]]'
menu:
    extend ""
    "[textdict[1218386]]":
        call avg101922
    "[textdict[1218387]]":
        call avg101923
    "[textdict[1218388]]":
        call avg101924
return