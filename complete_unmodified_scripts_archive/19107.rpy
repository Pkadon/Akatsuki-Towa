label avg19107(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_071
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1218031)]' (**arg(1, 1218031, size=(0.9)))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc001_01 1', 'p9', [l(-11), light, flip], 6)
get_char('c91') '[convertstrid(1218032)]' (**arg(2, 1218032, size=(0.9)))
$ update_portrait('sc001_01 1', 'p9', [l(-11), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1218033)]' (**arg(3, 1218033, size=(0.9)))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc001_01 1', 'p9', [l(-11), light, flip], 6)
get_char('c91') '[convertstrid(1218034)]' (**arg(4, 1218034, size=(0.9)))
$ update_portrait('sc001_01 5', 'p9', [l(-11), light, flip], 6)
get_char('c91') '[convertstrid(1218035)]' (**arg(5, 1218035, size=(0.9)))
$ update_portrait('sc001_01 5', 'p9', [l(-11), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1218036)]' (**arg(6, 1218036, size=(0.9)))
menu:
    extend ""
    '[convertstrid(1218037)]':
        call avg19108
    '[convertstrid(1218038)]':
        call avg19109
    '[convertstrid(1218039)]':
        call avg19110
return _return