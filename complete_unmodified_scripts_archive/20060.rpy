label avg20060(trans=fade_in):

$ play_music("ed7151.ogg")
scene placeholderbackground
$ update_narrator('c4973')
window show
with trans
play sfx2 "other_7071.ogg"
get_char('c4973') '[convertstrid(1002996)]' (**arg(1, 1002996))
get_char('c4973') '[convertstrid(1002997)]' (**arg(2, 1002997))
$ update_portrait('oc001_01 9', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1002998)]' (**arg(3, 1002998))
hide p1
get_char('c4973') '[convertstrid(1002999)]' (**arg(4, 1002999))
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
play sfx2 "other_7073.ogg"
get_char('c13') '[convertstrid(1003000)]' (**arg(5, 1003000))
$ update_portrait('oc001_01 3', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1003001)]' (**arg(6, 1003001))
return "avg20060"