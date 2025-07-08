label avg24086:
stop music

play music "ed7105.ogg"
scene placeholderbackground
$ update_portrait('st044_01 2', 'p243', [l(10), light, flip], 6)
window show
with fade_in
c2431 '[textdict[1200317]]'
hide p243
$ update_portrait('st044_01 2', 'p243', [l(10), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1200318]]'
return