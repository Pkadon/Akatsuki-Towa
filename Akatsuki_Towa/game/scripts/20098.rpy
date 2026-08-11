label avg20098(trans=fade_in):

$ play_music("ed7104.ogg")
scene avg_bg_037
$ update_narrator('c11')
window show
with trans
$ update_portrait('oc001_01 2', 'p1', [l_entrance(-2), light, flip], 6)
play sfx2 "other_7043.ogg"
get_char('c11') '[convertstrid(1004834)]' (**arg(1, 1004834))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1004835)]' (**arg(2, 1004835))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na06.ogg"
get_char('c11') '[convertstrid(1004836)]' (**arg(3, 1004836))
return "avg20098"