label avg10403(trans=fade_in):

$ play_music("ED6518.ogg")
scene avg_bg_001
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1140280)]' (**arg(1, 1140280))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1140282)]' (**arg(2, 1140282))
menu:
    extend ""
    '[convertstrid(1140283)]':
        call avg10404
    '[convertstrid(1140284)]':
        call avg10405
return _return