label avg105208:
stop music

scene placeholderbackground
show sc052_01 3 as p59 at l(-25), light, flip, zorder 6
window show
with fade_in
c591 '[textdict[1219268]]'
hide p59
show sc052_01 3 as p59 at l(-25), dark, flip, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1219269]]'
hide p59
hide p1
show oc001_01 2 as p1 at r(-2), dark, zorder 5
show sc052_01 5 as p59 at l(-25), light, flip, zorder 6
c591 '[textdict[1219270]]'
hide p1
hide p59
show sc052_01 5 as p59 at l(-25), dark, flip, zorder 6
show oc001_01 1 as p1 at r(-2), light, zorder 5
c13 '[textdict[1219271]]'
menu:
    extend ""
    "[textdict[1219272]]":
        call avg105209
    "[textdict[1219273]]":
        call avg105210
    "[textdict[1219274]]":
        call avg105211
return