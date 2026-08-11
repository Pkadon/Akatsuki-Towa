label avg101621(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc008_01 3', 'p16', [l(-18), light, flip], 6)
$ update_narrator('c161')
window show
with trans
get_char('c161') '[convertstrid(1221586)]' (**arg(1, 1221586))
$ update_portrait('sc008_01 3', 'p16', [l(-18), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1221587)]' (**arg(2, 1221587))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc008_01 1', 'p16', [l(-18), light, flip], 6)
get_char('c161') '[convertstrid(1221588)]' (**arg(3, 1221588))
menu:
    extend ""
    '[convertstrid(1221589)]':
        call avg101622
    '[convertstrid(1221590)]':
        call avg101623
    '[convertstrid(1221591)]':
        call avg101624
return _return