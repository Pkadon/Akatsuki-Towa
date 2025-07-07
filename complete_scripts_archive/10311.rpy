label avg10311:
stop music

play music "ed7105.ogg"
scene avg_bg_022
show oc002_01 2 as p2 at l(-3), light, zorder 6
window show
with fade_out
play sfx2 "other_7020.ogg"
c21 '[textdict[1130295]]'
hide p2
show oc002_01 2 as p2 at l(-3), dark, zorder 6
show st053_01 1 as p1007 at r(-12), light, zorder 5
c10073 '[textdict[1130296]]'
hide p2
hide p1007
show st053_01 1 as p1007 at r(-12), dark, zorder 5
show oc001_01 6 as p1 at l(-2), light, zorder 6
c11 '[textdict[1130297]]'
hide p1007
hide p1
show oc001_01 6 as p1 at l(-2), dark, zorder 6
show st053_01 2 as p1007 at r(-12), light, zorder 5
c10073 '[textdict[1130298]]'
hide p1
hide p1007
show st053_01 2 as p1007 at r(-12), dark, zorder 5
show oc002_01 8 as p2 at l(-3), light, zorder 6
c21 '[textdict[1130299]]'
hide p2
hide p1007
show st053_01 2 as p1007 at r(-12), dark, zorder 5
show oc001_01 1 as p1 at l(-2), light, zorder 6
c11 '[textdict[1130300]]'
hide p1007
hide p1
show oc001_01 1 as p1 at l(-2), dark, zorder 6
show st053_01 5 as p1007 at r(-12), light, zorder 5
c10073 '[textdict[1130301]]'
hide p1007
hide p1
show oc001_01 1 as p1 at l(-2), dark, zorder 6
show st053_01 1 as p1007 at r(-12), light, zorder 5
c10073 '[textdict[1130309]]'
hide p1007
hide p1
show oc001_01 1 as p1 at l(-2), dark, zorder 6
show st053_01 1 as p1007 at r(-12), light, zorder 5
c10073 '[textdict[1130310]]'
hide p1
hide p1007
show st053_01 1 as p1007 at r(-12), dark, zorder 5
show oc001_01 2 as p1 at l(-2), light, zorder 6
c11 '[textdict[1130311]]'
hide p1007
hide p1
show oc001_01 2 as p1 at l(-2), dark, zorder 6
show oc003_01 5 as p3 at r(-6), light, zorder 5
play sfxvoice "avg_vocal_ro05.ogg"
c33 '[textdict[1130312]]'
hide p1
hide p3
show oc003_01 5 as p3 at r(-6), dark, zorder 5
show oc004_01 7 as p4 at l(-5), l_shake, light, zorder 6
play sfxvoice "avg_vocal_li21.ogg"
c41 '[textdict[1130313]]'
hide p3
hide p4
show oc004_01 7 as p4 at l(-5), dark, zorder 6
show st053_01 4 as p1007 at r(-12), light, zorder 5
c10073 '[textdict[1130314]]'
menu:
    extend ""
    "[textdict[1130315]]":
        call avg10313
    "[textdict[1130316]]":
        call avg10314
return