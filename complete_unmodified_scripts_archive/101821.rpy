label avg101821(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1222215)]' (**arg(1, 1222215))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('sc010_01 4', 'p18', [l(-10), light, flip], 6)
get_char('c181') '[convertstrid(1222216)]' (**arg(2, 1222216))
$ update_portrait('sc010_01 1', 'p18', [l(-10), light, flip], 6)
get_char('c181') '[convertstrid(1222217)]' (**arg(3, 1222217))
menu:
    extend ""
    '[convertstrid(1222218)]':
        call avg101822
    '[convertstrid(1222219)]':
        call avg101823
    '[convertstrid(1222220)]':
        call avg101824
return _return