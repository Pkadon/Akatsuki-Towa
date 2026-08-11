label avg101204(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1220670)]' (**arg(1, 1220670))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc004_01 2', 'p12', [l(-12), light, flip], 6)
get_char('c121') '[convertstrid(1220671)]' (**arg(2, 1220671))
$ update_portrait('sc004_01 2', 'p12', [l(-12), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1220672)]' (**arg(3, 1220672))
menu:
    extend ""
    '[convertstrid(1220673)]':
        call avg101205
    '[convertstrid(1220674)]':
        call avg101206
    '[convertstrid(1220675)]':
        call avg101207
return _return