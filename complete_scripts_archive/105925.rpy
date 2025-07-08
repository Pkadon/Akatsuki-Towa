label avg105925:
stop music

scene placeholderbackground
show sc052_01 6 as p59 at l(-25), light, flip, zorder 6
window show
with fade_in
c591 '[textdict[1219319]]'
hide p59
show sc052_01 4 as p59 at l(-25), light, flip, zorder 6
c591 '[textdict[1219320]]'
hide p59
show sc052_01 4 as p59 at l(-25), dark, flip, zorder 6
show oc001_01 10 as p1 at r(-2), light, zorder 5
c13 '[textdict[1219321]]'
hide p59
hide p1
show oc001_01 10 as p1 at r(-2), dark, zorder 5
show sc052_01 5 as p59 at l(-25), light, flip, zorder 6
c591 '[textdict[1219322]]'
menu:
    extend ""
    "[textdict[1219323]]":
        call avg105926
    "[textdict[1219324]]":
        call avg105927
    "[textdict[1219325]]":
        call avg105928
return