label avg20014(trans=fade_in):

$ play_music("ED6518.ogg")
scene avg_bg_008
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1000941)]' (**arg(1, 1000941))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(1000942)]' (**arg(2, 1000942))
hide p2
get_char('c5171') '[convertstrid(1000943)]' (**arg(3, 1000943))
get_char('c5171') '[convertstrid(1000944)]' (**arg(4, 1000944))
get_char('c5171') '[convertstrid(1000945)]' (**arg(5, 1000945))
menu:
    extend ""
    '[convertstrid(1000946)]':
        call avg20015
    '[convertstrid(1000947)]':
        call avg20016
return _return