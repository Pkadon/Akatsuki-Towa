label avg12831(trans=fade_in):

$ play_music("ed7511.ogg")
scene avg_bg_004
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1185406)]' (**arg(1, 1185406))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc008_01 4', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1185407)]' (**arg(2, 1185407))
hide p1
$ update_portrait('sc008_01 4', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc004_01 7', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1185408)]' (**arg(3, 1185408))
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1185409)]' (**arg(4, 1185409))
hide p16
$ update_portrait('oc004_01 9', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 16', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1185410)]' (**arg(5, 1185410))
return "avg12831"