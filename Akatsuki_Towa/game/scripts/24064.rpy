label avg24064(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_050
$ update_narrator('c7573')
window show
with trans
get_char('c7573') '[convertstrid(1200258)]' (**arg(1, 1200258))
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1200259)]' (**arg(2, 1200259))
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
get_char('c7573') '[convertstrid(1200260)]' (**arg(3, 1200260))
return "avg24064"