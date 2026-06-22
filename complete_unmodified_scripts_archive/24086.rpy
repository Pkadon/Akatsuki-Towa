label avg24086:

$ play_music("ed7105.ogg")
scene placeholderbackground
$ update_portrait('st044_01 2', 'p243', [l(10), light, flip], 6)
$ update_narrator('c2431')
window show
with fade_in
get_char('c2431') '[convertstrid(1200317)]' (**arg(1, 1200317))
$ update_portrait('st044_01 2', 'p243', [l(10), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1200318)]' (**arg(2, 1200318))
return