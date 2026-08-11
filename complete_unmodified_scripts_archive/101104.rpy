label avg101104(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
get_char('c13') '[convertstrid(1220399)]' (**arg(1, 1220399))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc003_01 6', 'p11', [l(-4), light, flip], 6)
get_char('c111') '[convertstrid(1220400)]' (**arg(2, 1220400))
$ update_portrait('sc003_01 6', 'p11', [l(-4), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1220401)]' (**arg(3, 1220401))
menu:
    extend ""
    '[convertstrid(1220402)]':
        call avg101105
    '[convertstrid(1220403)]':
        call avg101106
    '[convertstrid(1220404)]':
        call avg101107
return _return