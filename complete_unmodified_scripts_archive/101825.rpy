label avg101825(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1222226)]' (**arg(1, 1222226))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc010_01 4', 'p18', [l(-10), light, flip], 6)
get_char('c181') '[convertstrid(1222227)]' (**arg(2, 1222227))
$ update_portrait('sc010_01 4', 'p18', [l(-10), light, flip], 6)
get_char('c181') '[convertstrid(1222228)]' (**arg(3, 1222228))
menu:
    extend ""
    '[convertstrid(1222229)]':
        call avg101826
    '[convertstrid(1222230)]':
        call avg101827
    '[convertstrid(1222231)]':
        call avg101828
return _return