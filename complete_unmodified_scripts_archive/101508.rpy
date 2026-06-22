label avg101508:

stop music
scene placeholderbackground
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
$ update_narrator('c151')
window show
with fade_in
get_char('c151') '[convertstrid(1221281)]' (**arg(1, 1221281))
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1221282)]' (**arg(2, 1221282))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 5', 'p15', [l(-17), light, flip], 6)
get_char('c151') '[convertstrid(1221283)]' (**arg(3, 1221283))
$ update_portrait('sc007_01 5', 'p15', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1221284)]' (**arg(4, 1221284))
menu:
    extend ""
    '[convertstrid(1221285)]':
        call avg101509
    '[convertstrid(1221286)]':
        call avg101510
    '[convertstrid(1221287)]':
        call avg101511
return