label avg12007:

$ play_music("ed7101.ogg")
scene avg_bg_020
$ update_narrator('c23')
window show
with fade_in
$ update_portrait('oc002_01 2', 'p2', [r_entrance(-3), light], 6)
play sfx2 "other_7020.ogg"
get_char('c23') '[convertstrid(1007143)]' (**arg(1, 1007143))
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007144)]' (**arg(2, 1007144))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 1', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1007145)]' (**arg(3, 1007145))
hide p1
$ update_portrait('oc002_01 1', 'p2', [r(-3), dark], 5)
$ update_portrait('sc068_01 2', 'p72', [l(-17), light, flip], 6)
get_char('c721') '[convertstrid(1007146)]' (**arg(4, 1007146))
$ update_portrait('sc068_01 2', 'p72', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1007147)]' (**arg(5, 1007147))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc068_01 2', 'p72', [l(-17), light, flip], 6)
get_char('c721') '[convertstrid(1007148)]' (**arg(6, 1007148))
$ update_portrait('sc068_01 2', 'p72', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c23') '[convertstrid(1007149)]' (**arg(7, 1007149))
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
$ update_portrait('sc068_01 1', 'p72', [l(-17), light, flip], 6)
get_char('c721') '[convertstrid(1007150)]' (**arg(8, 1007150))
hide p2
$ update_portrait('sc068_01 1', 'p72', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007151)]' (**arg(9, 1007151))
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007152)]' (**arg(10, 1007152))
hide p72
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
get_char('c7161') '[convertstrid(1007153)]' (**arg(11, 1007153))
hide p1
get_char('c7173') '[convertstrid(1007154)]' (**arg(12, 1007154))
get_char('c7161') '[convertstrid(1007155)]' (**arg(13, 1007155))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na04.ogg"
get_char('c13') '[convertstrid(1007156)]' (**arg(14, 1007156))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1007157)]' (**arg(15, 1007157))
hide p1
get_char('c0') '[convertstrid(1007158)]' (**arg(16, 1007158))
$ update_portrait('sc068_01 2', 'p72', [l(-17), light, flip], 6)
get_char('c721') '[convertstrid(1007159)]' (**arg(17, 1007159))
$ update_portrait('sc068_01 2', 'p72', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 4', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1007160)]' (**arg(18, 1007160))
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1007161)]' (**arg(19, 1007161))
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfx2 "other_7088.ogg"
get_char('c13') '[convertstrid(1007162)]' (**arg(20, 1007162))
hide p1
$ update_portrait('oc002_01 12', 'p2', [r(-3), r_shake, light], 6)
play sfx2 "bat_craft_wind_01.ogg"
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1007163)]' (**arg(21, 1007163))
$ update_portrait('oc002_01 12', 'p2', [r(-3), dark], 5)
$ update_portrait('sc068_01 4', 'p72', [l(-17), light, flip], 6)
get_char('c721') '[convertstrid(1007164)]' (**arg(22, 1007164))
$ update_portrait('sc068_01 1', 'p72', [l_exit(-17), light, flip], 6)
play sfx2 "bat_utility_jump.ogg"
get_char('c721') '[convertstrid(1007165)]' (**arg(23, 1007165))
hide p72
hide p2
$ update_portrait('oc001_01 12', 'p1', [r(-2), r_shake, light], 6)
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1007166)]' (**arg(24, 1007166))
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc068_01 1', 'p72', [l_entrance(-17), light, flip], 6)
play sfx2 "bat_utility_landing.ogg"
get_char('c721') '[convertstrid(1007167)]' (**arg(25, 1007167))
hide p72
hide p1
play sfx2 "other_7002.ogg"
get_char('c0') '[convertstrid(1007250)]' (**arg(26, 1007250))
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(1007168)]' (**arg(27, 1007168))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('sc068_01 2', 'p72', [l(-17), light, flip], 6)
get_char('c721') '[convertstrid(1007169)]' (**arg(28, 1007169))
hide p2
$ update_portrait('sc068_01 2', 'p72', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 19', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1007170)]' (**arg(29, 1007170))
$ update_portrait('oc001_01 19', 'p1', [r(-2), dark], 5)
$ update_portrait('sc068_01 6', 'p72', [l(-17), light, flip], 6)
get_char('c721') '[convertstrid(1007171)]' (**arg(30, 1007171))
hide p1
$ update_portrait('sc068_01 6', 'p72', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1007172)]' (**arg(31, 1007172))
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('sc068_01 1', 'p72', [l(-17), light, flip], 6)
get_char('c721') '[convertstrid(1007178)]' (**arg(32, 1007178))
$ update_portrait('sc068_01 1', 'p72', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1007179)]' (**arg(33, 1007179))
hide p72
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007180)]' (**arg(34, 1007180))
return