label avg101908:
stop music

stop music
scene placeholderbackground
with fade
show sc011_01 4 as p19 at l(-1), light, zorder 5
c191 '[textdict[1218343]]'
stop music
hide p19
show sc011_01 4 as p19 at l(-1), dark, zorder 6
show oc001_01 10 as p1 at r(-2), light, zorder 5
c13 '[textdict[1218344]]'
stop music
hide p19
hide p1
show oc001_01 10 as p1 at r(-2), dark, zorder 5
show sc011_01 2 as p19 at l(-1), light, zorder 5
c191 '[textdict[1218345]]'
menu:
    extend ""
    "[textdict[1218346]]":
        call avg101909
    "[textdict[1218347]]":
        call avg101910
    "[textdict[1218348]]":
        call avg101911
return