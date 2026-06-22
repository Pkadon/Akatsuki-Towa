label avg106008:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1219067)]' (**arg(1, 1219067))
$ update_portrait('oc001_01 16', 'p1', [r(-2), dark], 5)
$ update_portrait('sc053_01 1', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(1219068)]' (**arg(2, 1219068))
$ update_portrait('sc053_01 1', 'p60', [l(-32), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1219069)]' (**arg(3, 1219069))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc053_01 5', 'p60', [l(-32), light, flip], 6)
get_char('c601') '[convertstrid(1219070)]' (**arg(4, 1219070))
menu:
    extend ""
    '[convertstrid(1219071)]':
        call avg106009
    '[convertstrid(1219072)]':
        call avg106010
    '[convertstrid(1219073)]':
        call avg106011
return