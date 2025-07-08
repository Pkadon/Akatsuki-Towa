label avg10314:
stop music

play music "ed7105.ogg"
scene avg_bg_022
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
window show
with fade_in
play sfx2 "common_cancel.ogg"
c11 '[textdict[1130319]]'
hide p1
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('st053_01 2', 'p1007', [r(-12), light], 5)
c10073 '[textdict[1130320]]'
return