label avg10312:
stop music

play music "ed7105.ogg"
scene avg_bg_022
show st053_01 1 as p1007 at r(-12), light, zorder 5
with fade
c10073 '[textdict[1130302]]'
hide p1007
show st053_01 1 as p1007 at r(-12), dark, zorder 5
show oc001_01 1 as p1 at l(-2), light, zorder 6
c11 '[textdict[1130303]]'
hide p1007
hide p1
show oc001_01 1 as p1 at l(-2), dark, zorder 6
show oc002_01 5 as p2 at r(-3), light, zorder 5
c23 '[textdict[1130304]]'
hide p1
hide p2
show oc002_01 5 as p2 at r(-3), dark, zorder 5
show oc003_01 1 as p3 at l(-6), light, zorder 6
c31 '[textdict[1130305]]'
hide p2
hide p3
show oc003_01 1 as p3 at l(-6), dark, zorder 6
show st053_01 2 as p1007 at r(-12), light, zorder 5
c10073 '[textdict[1130306]]'
hide p3
hide p1007
show st053_01 2 as p1007 at r(-12), dark, zorder 5
show oc004_01 1 as p4 at l(-5), light, zorder 6
c41 '[textdict[1130307]]'
hide p1007
hide p4
show oc004_01 1 as p4 at l(-5), dark, zorder 6
show st053_01 4 as p1007 at r(-12), light, zorder 5
c10073 '[textdict[1130308]]'
hide p1007
hide p4
show oc004_01 1 as p4 at l(-5), dark, zorder 6
show st053_01 1 as p1007 at r(-12), light, zorder 5
c10073 '[textdict[1130309]]'
hide p1007
hide p4
show oc004_01 1 as p4 at l(-5), dark, zorder 6
show st053_01 1 as p1007 at r(-12), light, zorder 5
c10073 '[textdict[1130310]]'
hide p4
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