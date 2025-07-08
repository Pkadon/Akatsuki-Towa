label avg20130:
stop music

scene avg_bg_071
window show
with fade_in
show oc001_01 4 as p1 at l_entrance(-2), light, flip, zorder 6
play sfxvoice "avg_vocal_na10.ogg"
c11 '[textdict[1006633]]'
hide p1
show oc001_01 4 as p1 at l(-2), dark, flip, zorder 6
show oc002_01 17 as p2 at r(-3), light, zorder 5
play sfxvoice "avg_vocal_ch21.ogg"
c23 '[textdict[1006634]]'
hide p1
hide p2
show oc002_01 17 as p2 at r(-3), dark, zorder 5
show oc004_01 8 as p4 at l(-5), light, flip, zorder 6
play sfxvoice "avg_vocal_li18.ogg"
c41 '[textdict[1006635]]'
hide p2
hide p4
show oc004_01 8 as p4 at l(-5), dark, flip, zorder 6
show oc003_01 4 as p3 at r(-6), light, zorder 5
play sfxvoice "avg_vocal_ro19.ogg"
c33 '[textdict[1006636]]'
hide p3
hide p4
show oc004_01 8 as p4 at l(-5), dark, flip, zorder 6
show oc003_01 5 as p3 at r(-6), light, zorder 5
play sfx2 "other_7071.ogg"
play sfxvoice "avg_vocal_ro05.ogg"
c33 '[textdict[1006637]]'
hide p4
hide p3
show oc003_01 5 as p3 at r(-6), dark, zorder 5
play sfx2 "other_7072.ogg"
play sfxvoice "avg_vocal_ji05.ogg"
c7011 '[textdict[1006638]]'
hide p3
show oc003_01 5 as p3 at r(-6), dark, zorder 5
c7011 '[textdict[1006639]]'
hide p3
show oc003_01 5 as p3 at r(-6), dark, zorder 5
c7011 '[textdict[1006640]]'
return