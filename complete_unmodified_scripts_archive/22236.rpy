label avg22236:

$ play_music("ed7202.ogg")
scene placeholderbackground
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1121169)]' (**arg(1, 1121169))
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1121170)]' (**arg(2, 1121170))
hide p2
$ update_portrait('oc004_01 2', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1121171)]' (**arg(3, 1121171))
hide p4
$ update_portrait('oc002_01 19', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1121172)]' (**arg(4, 1121172))
hide p2
play sfx2 "other_7013.ogg"
get_char('c0') '[convertstrid(1121173)]' (**arg(5, 1121173))
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na07.ogg"
get_char('c13') '[convertstrid(1121174)]' (**arg(6, 1121174))
hide p1
get_char('c0') '[convertstrid(1121175)]' (**arg(7, 1121175))
play sfx2 "bat_craft_wind_01.ogg"
get_char('c0') '[convertstrid(1121176)]' (**arg(8, 1121176))
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na04_b.ogg"
get_char('c13') '[convertstrid(1121177)]' (**arg(9, 1121177))
hide p1
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c23') '[convertstrid(1121178)]' (**arg(10, 1121178))
hide p2
$ update_portrait('oc004_01 23', 'p4', [mid(-5), light], 6)
play sfxvoice "avg_vocal_li09.ogg"
get_char('c43') '[convertstrid(1121179)]' (**arg(11, 1121179))
hide p4
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1121180)]' (**arg(12, 1121180))
hide p1
$ update_portrait('oc004_01 2', 'p4', [mid(-5), light], 6)
get_char('c43') '[convertstrid(1121181)]' (**arg(13, 1121181))
hide p4
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1121182)]' (**arg(14, 1121182))
return