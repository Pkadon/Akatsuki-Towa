label avg19103(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_071
$ update_portrait('sc001_01 4', 'p9', [l(-11), light, flip], 6)
$ update_narrator('c91')
window show
with trans
get_char('c91') '[convertstrid(1218020)]' (**arg(1, 1218020))
$ update_portrait('sc001_01 1', 'p9', [l(-11), light, flip], 6)
get_char('c91') '[convertstrid(1218021)]' (**arg(2, 1218021))
$ update_portrait('sc001_01 1', 'p9', [l(-11), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1218022)]' (**arg(3, 1218022))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc001_01 4', 'p9', [l(-11), light, flip], 6)
get_char('c91') '[convertstrid(1218023)]' (**arg(4, 1218023))
menu:
    extend ""
    '[convertstrid(1218024)]':
        call avg19104
    '[convertstrid(1218025)]':
        call avg19105
    '[convertstrid(1218026)]':
        call avg19106
return _return