label avg100125(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('sc001_01 2', 'p9', [mid(-11), light], 6)
$ update_narrator('c93')
window show
with trans
get_char('c93') '[convertstrid(1218088)]' (**arg(1, 1218088))
hide p9
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc002_win_02.ogg"
get_char('c13') '[convertstrid(1218089)]' (**arg(2, 1218089))
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc001_01 1', 'p9', [l(-11), light, flip], 6)
get_char('c91') '[convertstrid(1218090)]' (**arg(3, 1218090))
$ update_portrait('sc001_01 5', 'p9', [l(-11), light, flip], 6)
get_char('c91') '[convertstrid(1218091)]' (**arg(4, 1218091))
$ update_portrait('sc001_01 5', 'p9', [l(-11), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
play sfxvoice "bcv_oc002_win_02.ogg"
get_char('c13') '[convertstrid(1218092)]' (**arg(5, 1218092))
menu:
    extend ""
    '[convertstrid(1218093)]':
        call avg100126
    '[convertstrid(1218094)]':
        call avg100127
    '[convertstrid(1218095)]':
        call avg100128
return _return