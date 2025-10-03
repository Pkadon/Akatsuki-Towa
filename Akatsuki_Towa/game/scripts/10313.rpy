label avg10313:

$ play_music("ed7105.ogg")
scene avg_bg_022
$ update_portrait('oc001_01 6', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
play sfx2 "common_select.ogg"
c11 '[convertstrid(1130317)]'
$ update_portrait('oc001_01 6', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('st053_01 5', 'p1007', [r(-12), light], 6)
c10073 '[convertstrid(1130318)]'
return