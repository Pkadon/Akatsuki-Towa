label avg10308:
stop music

play music "ed7124.ogg"
scene avg_bg_059
window show
with fade_in
play sfx2 "other_7021.ogg"
c10063 '[textdict[1130265]]'
show oc001_01 1 as p1 at l(-2), light, flip, zorder 6
c11 '[textdict[1130266]]'
hide p1
show oc001_01 1 as p1 at l(-2), dark, flip, zorder 6
c10063 '[textdict[1130267]]'
hide p1
show oc001_01 1 as p1 at l(-2), dark, flip, zorder 6
c10063 '[textdict[1130268]]'
hide p1
show oc001_01 1 as p1 at l(-2), dark, flip, zorder 6
c10063 '[textdict[1130269]]'
hide p1
show oc004_01 1 as p4 at l(-5), light, flip, zorder 6
c41 '[textdict[1130270]]'
hide p4
show oc004_01 1 as p4 at l(-5), dark, flip, zorder 6
c10063 '[textdict[1130271]]'
hide p4
show oc004_01 2 as p4 at l(-5), light, flip, zorder 6
c41 '[textdict[1130272]]'
hide p4
show oc004_01 2 as p4 at l(-5), dark, flip, zorder 6
c10063 '[textdict[1130273]]'
hide p4
show oc004_01 2 as p4 at l(-5), dark, flip, zorder 6
c10063 '[textdict[1130274]]'
hide p4
show oc004_01 12 as p4 at l(-5), l_shake, light, flip, zorder 6
c41 '[textdict[1130275]]'
hide p4
show oc004_01 12 as p4 at l(-5), dark, flip, zorder 6
show oc001_01 2 as p1 at r(-2), light, zorder 5
c13 '[textdict[1130276]]'
hide p1
hide p4
show oc004_01 12 as p4 at l(-5), dark, flip, zorder 6
show oc002_01 2 as p2 at r(-3), light, zorder 5
c23 '[textdict[1130277]]'
hide p2
hide p4
show oc004_01 12 as p4 at l(-5), dark, flip, zorder 6
show oc003_01 5 as p3 at r(-6), light, zorder 5
play sfxvoice "avg_vocal_ro08.ogg"
c33 '[textdict[1130278]]'
hide p4
hide p3
show oc003_01 5 as p3 at r(-6), dark, zorder 5
show oc004_01 7 as p4 at l(-5), l_shake, light, flip, zorder 6
c41 '[textdict[1130279]]'
hide p3
hide p4
show oc004_01 7 as p4 at l(-5), dark, flip, zorder 6
c10063 '[textdict[1130280]]'
hide p4
show oc004_01 5 as p4 at l(-5), light, flip, zorder 6
play sfxvoice "avg_vocal_li30.ogg"
c41 '[textdict[1130281]]'
hide p4
show oc004_01 5 as p4 at l(-5), dark, flip, zorder 6
show oc001_01 8 as p1 at r(-2), light, zorder 5
c13 '[textdict[1130282]]'
menu:
    extend ""
    "[textdict[1130283]]":
        call avg10309
    "[textdict[1130284]]":
        call avg10310
return