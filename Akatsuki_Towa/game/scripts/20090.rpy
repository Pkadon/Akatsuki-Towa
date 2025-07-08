label avg20090:
stop music

play music "ed7117.ogg"
scene avg_bg_021
window show
with fade_out
c6781 '[textdict[1004506]]'
play sfx2 "other_7004.ogg"
c6793 '[textdict[1004507]]'
c6801 '[textdict[1004508]]'
c6793 '[textdict[1004509]]'
c6801 '[textdict[1004510]]'
c6783 '[textdict[1004511]]'
c6783 '[textdict[1004513]]'
c6801 '[textdict[1004514]]'
c6801 '[textdict[1004515]]'
show oc001_01 2 as p1 at l_entrance(-2), light, flip, zorder 6
c11 '[textdict[1004516]]'
hide p1
show oc001_01 2 as p1 at l(-2), dark, flip, zorder 6
show oc003_01 8 as p3 at r(-6), light, zorder 5
play sfxvoice "avg_vocal_ro13.ogg"
c33 '[textdict[1004517]]'
hide p1
hide p3
show oc003_01 8 as p3 at r(-6), dark, zorder 5
show oc002_01 5 as p2 at l(-3), light, flip, zorder 6
play sfxvoice "avg_vocal_ch07.ogg"
c21 '[textdict[1004518]]'
hide p3
hide p2
show oc002_01 5 as p2 at l(-3), dark, flip, zorder 6
show oc004_01 8 as p4 at r(-5), light, zorder 5
c43 '[textdict[1123027]]'
return