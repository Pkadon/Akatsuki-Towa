label avg12407:
stop music

play music "ed7100.ogg"
scene avg_bg_023
window show
with fade_out
show oc001_01 4 as p1 at r_entrance(-2), light, zorder 5
c13 '[textdict[1140242]]'
hide p1
show oc001_01 4 as p1 at r(-2), dark, zorder 5
show oc003_01 7 as p3 at l_entrance(-6), light, flip, zorder 6
play sfxvoice "avg_vocal_ro14.ogg"
c31 '[textdict[1140243]]'
hide p1
hide p3
show oc003_01 7 as p3 at l(-6), dark, flip, zorder 6
show oc001_01 4 as p1 at r(-2), light, zorder 5
play sfx2 "other_7004.ogg"
c13 '[textdict[1140244]]'
hide p3
hide p1
show oc001_01 4 as p1 at r(-2), dark, zorder 5
show oc004_01 7 as p4 at l(-5), light, flip, zorder 6
play sfxvoice "avg_vocal_li19.ogg"
c41 '[textdict[1140245]]'
hide p1
hide p4
show oc004_01 7 as p4 at l(-5), dark, flip, zorder 6
show oc002_01 1 as p2 at r(-3), light, zorder 5
c23 '[textdict[1140246]]'
hide p4
hide p2
show oc002_01 1 as p2 at r(-3), dark, zorder 5
show oc004_01 10 as p4 at l(-5), light, flip, zorder 6
c41 '[textdict[1140247]]'
hide p4
hide p2
show oc002_01 1 as p2 at r(-3), dark, zorder 5
show oc004_01 4 as p4 at l(-5), light, flip, zorder 6
c41 '[textdict[1140248]]'
hide p4
hide p2
show oc002_01 1 as p2 at r(-3), dark, zorder 5
show oc003_01 8 as p3 at l(-6), light, flip, zorder 6
play sfxvoice "avg_vocal_ro13.ogg"
c31 '[textdict[1140249]]'
hide p2
hide p3
show oc003_01 8 as p3 at l(-6), dark, flip, zorder 6
show oc002_01 5 as p2 at r(-3), light, zorder 5
c23 '[textdict[1140250]]'
return