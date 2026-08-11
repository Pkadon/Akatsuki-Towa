label avg20014(trans=fade_in):

$ play_music("ED6518.ogg")
scene avg_bg_014
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1000941)]' (**arg(1, 1000941))
hide p1
$ update_portrait('oc002_01 8', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1000942)]' (**arg(2, 1000942))
hide p2
get_char('c5173') '[convertstrid(1000943)]' (**arg(3, 1000943))
get_char('c5173') '[convertstrid(1000944)]' (**arg(4, 1000944))
get_char('c5173') '[convertstrid(1000945)]' (**arg(5, 1000945))
menu:
    extend ""
    '[convertstrid(1000946)]':
        call avg20015
    '[convertstrid(1000947)]':
        call avg20016
return _return