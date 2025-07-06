label avg105225:
stop music

scene placeholderbackground
with fade
show sc052_01 6 as p59 at l(-25), light, zorder 6
c591 '[textdict[1219319]]'
hide p59
show sc052_01 4 as p59 at l(-25), light, zorder 6
c591 '[textdict[1219320]]'
hide p59
show sc052_01 4 as p59 at l(-25), dark, zorder 6
show oc001_01 10 as p1 at r(-2), light, zorder 5
c13 '[textdict[1219321]]'
hide p59
hide p1
show oc001_01 10 as p1 at r(-2), dark, zorder 5
show sc052_01 5 as p59 at l(-25), light, zorder 6
c591 '[textdict[1219322]]'
menu:
    extend ""
    "[textdict[1219323]]":
        call avg105226
    "[textdict[1219324]]":
        call avg105227
    "[textdict[1219325]]":
        call avg105228
return