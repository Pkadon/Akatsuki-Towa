label avg24063(trans=fade_in):

$ play_music("ed7105.ogg")
scene avg_bg_050
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with trans
get_char('c11') '[convertstrid(1200255)]' (**arg(1, 1200255))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
get_char('c7573') '[convertstrid(1200256)]' (**arg(2, 1200256))
$ update_portrait('oc001_01 5', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200257)]' (**arg(3, 1200257))
return "avg24063"