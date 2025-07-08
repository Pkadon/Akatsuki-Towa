label avg10346:
stop music

play music "ed7544.ogg"
scene avg_bg_031
window show
with fade_in
show oc001_01 12 as p1 at r_entrance(-2), light, zorder 5
play sfxvoice "avg_vocal_na21.ogg"
c13 '[textdict[1131270]]'
hide p1
show oc001_01 12 as p1 at r(-2), dark, zorder 5
show oc002_01 12 as p2 at l(-3), light, flip, zorder 6
play sfxvoice "avg_vocal_ch11.ogg"
c21 '[textdict[1131271]]'
hide p2
hide p1
show oc001_01 12 as p1 at r(-2), dark, zorder 5
show oc004_01 9 as p4 at l(-5), light, flip, zorder 6
c41 '[textdict[1131272]]'
hide p4
hide p1
show oc001_01 12 as p1 at r(-2), dark, zorder 5
show oc003_01 5 as p3 at l(-6), light, flip, zorder 6
c31 '[textdict[1131273]]'
hide p3
hide p1
show oc001_01 12 as p1 at r(-2), dark, zorder 5
show sc046_01 3 as p1004 at l_midback(-5), light, flip, zorder 6
play sfx2 "fight_6024.ogg"
c10041 '[textdict[1131274]]' (what_size=(gui.text_size*1.2))
hide p1
hide p1004
show sc046_01 3 as p1004 at l(-5), dark, flip, zorder 6
play sfx2 "other_7085.ogg"
c10233 '[textdict[1131275]]'
hide p1004
show sc046_01 3 as p1004 at l(-5), dark, flip, zorder 6
c10243 '[textdict[1131276]]'
hide p1004
with fade
show oc001_01 12 as p1 at r_entrance(-2), r_shake, light, zorder 5
play sfxvoice "avg_vocal_na21.ogg"
c13 '[textdict[1131277]]' (what_size=(gui.text_size*1.2))
hide p1
show oc001_01 12 as p1 at r(-2), dark, zorder 5
show oc002_01 12 as p2 at l(-3), light, flip, zorder 6
c21 '[textdict[1131278]]'
hide p2
hide p1
with fade
play sfx2 "other_7085.ogg"
c10253 '[textdict[1131279]]'
c10263 '[textdict[1131280]]' (what_size=(gui.text_size*1.4))
show sc046_01 4 as p1004 at l_midback(-5), light, flip, zorder 6
play sfx2 "other_7091.ogg"
c10041 '[textdict[1131281]]' (what_size=(gui.text_size*1.2))
return