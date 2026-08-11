label avg105925(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc052_01 6', 'p59', [l(-25), light, flip], 6)
$ update_narrator('c591')
window show
with trans
get_char('c591') '[convertstrid(1219319)]' (**arg(1, 1219319))
$ update_portrait('sc052_01 4', 'p59', [l(-25), light, flip], 6)
get_char('c591') '[convertstrid(1219320)]' (**arg(2, 1219320))
$ update_portrait('sc052_01 4', 'p59', [l(-25), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1219321)]' (**arg(3, 1219321))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc052_01 5', 'p59', [l(-25), light, flip], 6)
get_char('c591') '[convertstrid(1219322)]' (**arg(4, 1219322))
menu:
    extend ""
    '[convertstrid(1219323)]':
        call avg105926
    '[convertstrid(1219324)]':
        call avg105927
    '[convertstrid(1219325)]':
        call avg105928
return _return