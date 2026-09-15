label avg22236(trans=fade_in):

$ play_music("ed7202.ogg")
scene avg_bg_218
$ update_narrator('c13')
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
window show
with trans
$ update_portrait('oc001_01 20', 'p1', [r(-2), l_shake, light], 6)
get_char('c13') '[convertstrid(1121169)]' (**arg(1, 1121169))
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), r_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c21') '[convertstrid(1121170)]' (**arg(2, 1121170))
hide p1
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1121171)]' (**arg(3, 1121171))
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 19', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121172)]' (**arg(4, 1121172))
hide p2
hide p4
play sfx2 "other_7013.ogg"
get_char('c0') '[convertstrid(1121173)]' (**arg(5, 1121173))
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na07.ogg"
get_char('c13') '[convertstrid(1121174)]' (**arg(6, 1121174))
hide p1
get_char('c0') '[convertstrid(1121175)]' (**arg(7, 1121175))
play sfx2 "bat_craft_wind_01.ogg"
get_char('c0') '[convertstrid(1121176)]' (**arg(8, 1121176))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na04_b.ogg"
get_char('c13') '[convertstrid(1121177)]' (**arg(9, 1121177))
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c21') '[convertstrid(1121178)]' (**arg(10, 1121178))
hide p1
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 23', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li09.ogg"
get_char('c43') '[convertstrid(1121179)]' (**arg(11, 1121179))
hide p2
$ update_portrait('oc004_01 23', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121180)]' (**arg(12, 1121180))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(1121181)]' (**arg(13, 1121181))
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 18', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1121182)]' (**arg(14, 1121182))
return "avg22236"