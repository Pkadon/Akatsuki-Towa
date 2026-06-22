label avg22208:

$ play_music("ed7123.ogg")
scene avg_bg_046
$ update_narrator('c7221')
window show
with fade_in
play sfx2 "other_7042.ogg"
get_char('c7221') '[convertstrid(1128646)]' (**arg(1, 1128646))
$ update_portrait('oc002_01 14', 'p2', [r_entrance(-3), light], 6)
play sfxvoice "avg_vocal_ch03_b.ogg"
get_char('c23') '[convertstrid(1128647)]' (**arg(2, 1128647))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 11', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1128648)]' (**arg(3, 1128648))
$ update_portrait('oc001_01 11', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1128650)]' (**arg(4, 1128650))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1128651)]' (**arg(5, 1128651))
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1128652)]' (**arg(6, 1128652))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 13', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1128653)]' (**arg(7, 1128653))
$ update_portrait('oc002_01 13', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1128654)]' (**arg(8, 1128654))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1128655)]' (**arg(9, 1128655))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na15.ogg"
get_char('c11') '[convertstrid(1128656)]' (**arg(10, 1128656))
return