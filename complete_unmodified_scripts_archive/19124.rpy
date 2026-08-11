label avg19124(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_071
$ update_portrait('sc001_01 2', 'p9', [l(-11), light, flip], 6)
$ update_narrator('c91')
window show
with trans
get_char('c91') '[convertstrid(1218085)]' (**arg(1, 1218085, size=(0.9)))
$ update_portrait('sc001_01 2', 'p9', [l(-11), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc002_win_02.ogg"
get_char('c13') '[convertstrid(1218086)]' (**arg(2, 1218086, size=(0.9)))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc001_01 1', 'p9', [l(-11), light, flip], 6)
get_char('c91') '[convertstrid(1218087)]' (**arg(3, 1218087, size=(0.9)))
$ update_portrait('sc001_01 5', 'p9', [l(-11), light, flip], 6)
get_char('c91') '[convertstrid(1218088)]' (**arg(4, 1218088, size=(0.9)))
$ update_portrait('sc001_01 5', 'p9', [l(-11), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc002_win_02.ogg"
get_char('c13') '[convertstrid(1218089)]' (**arg(5, 1218089, size=(0.9)))
menu:
    extend ""
    '[convertstrid(1218090)]':
        call avg19125
    '[convertstrid(1218091)]':
        call avg19126
    '[convertstrid(1218092)]':
        call avg19127
return _return