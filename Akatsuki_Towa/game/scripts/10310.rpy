label avg10310:
stop music

play music "ed7124.ogg"
scene avg_bg_059
show oc001_01 8 as p1 at r(-2), light, zorder 5
window show
with fade_out
play sfx2 "common_cancel.ogg"
c13 '[textdict[1130291]]'
hide p1
c10063 '[textdict[1130292]]'
show oc004_01 8 as p4 at l(-5), light, flip, zorder 6
play sfxvoice "avg_vocal_li18.ogg"
c41 '[textdict[1130293]]'
hide p4
show oc004_01 8 as p4 at l(-5), dark, flip, zorder 6
show oc001_01 7 as p1 at r(-2), light, zorder 5
c13 '[textdict[1130294]]'
return