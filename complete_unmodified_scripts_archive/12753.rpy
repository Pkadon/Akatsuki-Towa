label avg12753(trans=fade_in):

$ play_music("ed7544.ogg")
scene avg_bg_036
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
window show
with trans
get_char('c31') '[convertstrid(1174324)]' (**arg(1, 1174324))
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1174325)]' (**arg(2, 1174325))
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('st061_01 4', 'p1304', [r(-2), light], 6)
get_char('c13043') '[convertstrid(1174326)]' (**arg(3, 1174326))
hide p1304
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1174327)]' (**arg(4, 1174327))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 4', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1174328)]' (**arg(5, 1174328))
$ update_portrait('oc003_01 4', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1174329)]' (**arg(6, 1174329))
return "avg12753"