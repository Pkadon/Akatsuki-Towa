label avg12356(trans=fade_in):

$ play_music("ed9999.ogg")
scene avg_bg_074
$ update_portrait('st032_01 5', 'p231', [l(2), light, flip], 6)
$ update_narrator('c2311')
window show
with trans
play sfx2 "other_7048.ogg"
get_char('c2311') '[convertstrid(1133662)]' (**arg(1, 1133662))
$ update_portrait('st032_01 1', 'p231', [l(2), light, flip], 6)
get_char('c2311') '[convertstrid(1133663)]' (**arg(2, 1133663))
$ update_portrait('st032_01 5', 'p231', [l(2), light, flip], 6)
get_char('c2311') '[convertstrid(1133664)]' (**arg(3, 1133664))
$ update_portrait('st032_01 5', 'p231', [l(2), dark, flip], 5)
$ update_portrait('oc004_01 9', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li07.ogg"
get_char('c43') '[convertstrid(1133665)]' (**arg(4, 1133665))
hide p4
$ update_portrait('oc001_01 11', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1133666)]' (**arg(5, 1133666))
$ update_portrait('oc001_01 11', 'p1', [r(-2), dark], 5)
$ update_portrait('st032_01 6', 'p231', [l(2), light, flip], 6)
get_char('c2311') '[convertstrid(1133667)]' (**arg(6, 1133667))
hide p231
$ update_portrait('oc002_01 14', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1133668)]' (**arg(7, 1133668))
return "avg12356"