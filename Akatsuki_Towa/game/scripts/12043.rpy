label avg12043(trans=fade_in):

$ play_music("ed7117.ogg")
scene avg_bg_017
$ update_portrait('uc002_01 3', 'p5001', [r(2), light], 6)
$ update_narrator('c50013')
window show
with trans
play sfx2 "other_7057.ogg"
get_char('c50013') '[convertstrid(1121378)]' (**arg(1, 1121378))
$ update_portrait('uc002_01 3', 'p5001', [r(2), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
play sfx2 "fight_6024.ogg"
get_char('c11') '[convertstrid(1121379)]' (**arg(2, 1121379))
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('uc002_01 4', 'p5001', [r_exit(2), light], 6)
play sfx2 "other_7086.ogg"
get_char('c50013') '[convertstrid(1121380)]' (**arg(3, 1121380))
hide p5001
hide p1
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121381)]' (**arg(4, 1121381))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1121382)]' (**arg(5, 1121382))
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1121383)]' (**arg(6, 1121383))
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1121384)]' (**arg(7, 1121384))
hide p2
$ update_portrait('sc068_01 6', 'p72', [l(-17), light, flip], 6)
play sfx2 "other_7020.ogg"
get_char('c721') '[convertstrid(1120383)]' (**arg(8, 1120383))
$ update_portrait('sc068_01 6', 'p72', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 3', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1120384)]' (**arg(9, 1120384))
hide p72
$ update_portrait('oc001_01 3', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120385)]' (**arg(10, 1120385))
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120386)]' (**arg(11, 1120386))
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 9', 'p1', [r(-2), r_shake, light], 6)
get_char('c13') '[convertstrid(1120387)]' (**arg(12, 1120387))
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 7', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch31.ogg"
get_char('c21') '[convertstrid(1120388)]' (**arg(13, 1120388))
hide p2
hide p1
get_char('c0') '[convertstrid(1121537)]' (**arg(14, 1121537))
return "avg12043"