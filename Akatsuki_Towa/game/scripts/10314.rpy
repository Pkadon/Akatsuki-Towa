label avg10314:
stop music

play music "ed7105.ogg"
scene avg_bg_022
show oc001_01 8 as p1 at l(-2), light, flip, zorder 6
window show
with fade_out
play sfx2 "common_cancel.ogg"
c11 '[textdict[1130319]]'
hide p1
show oc001_01 8 as p1 at l(-2), dark, flip, zorder 6
show st053_01 2 as p1007 at r(-12), light, zorder 5
c10073 '[textdict[1130320]]'
return