label avg1021(trans=fade_in):

$ play_music("ed7150.ogg")
scene avg_bg_014
$ update_narrator('c0')
window show
with trans
get_char('c0') '[convertstrid(2100402)]' (**arg(1, 2100402))
$ update_portrait('oc002_01 10', 'p2', [l_entrance(-3), light, flip], 6)
get_char('c21') '[convertstrid(2100403)]' (**arg(2, 2100403))
$ update_portrait('oc002_01 21', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch31.ogg"
get_char('c21') '[convertstrid(2100404)]' (**arg(3, 2100404))
$ update_portrait('oc002_01 14', 'p2', [l(-3), l_shake, light, flip], 6)
get_char('c21') '[convertstrid(2100405)]' (**arg(4, 2100405))
$ update_portrait('oc002_01 17', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2100406)]' (**arg(5, 2100406))
$ update_portrait('oc002_01 17', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(2100407)]' (**arg(6, 2100407))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 16', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2100408)]' (**arg(7, 2100408))
hide p2
$ update_portrait('oc004_01 7', 'p4', [l_entrance(-5), light, flip], 6)
get_char('c41') '[convertstrid(2100409)]' (**arg(8, 2100409))
hide p1
$ update_portrait('oc004_01 7', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100410)]' (**arg(9, 2100410))
hide p4
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l_entrance(9), light, flip], 6)
get_char('c231') '[convertstrid(2100411)]' (**arg(10, 2100411))
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100412)]' (**arg(11, 2100412))
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
get_char('c43') '[convertstrid(2100413)]' (**arg(12, 2100413))
$ update_portrait('oc004_01 1', 'p4', [r_exit(-5), light], 6)
get_char('c43') '[convertstrid(2100414)]' (**arg(13, 2100414))
hide p4
hide p23
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(2100415)]' (**arg(14, 2100415))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(2100416)]' (**arg(15, 2100416))
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100417)]' (**arg(16, 2100417))
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100418)]' (**arg(17, 2100418))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100419)]' (**arg(18, 2100419))
hide p1
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100420)]' (**arg(19, 2100420))
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100421)]' (**arg(20, 2100421))
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100422)]' (**arg(21, 2100422))
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 5)
$ update_portrait('oc002_01 14', 'p2', [r(-3), light], 6)
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(2100423)]' (**arg(22, 2100423))
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100424)]' (**arg(23, 2100424))
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(2100425)]' (**arg(24, 2100425))
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100426)]' (**arg(25, 2100426))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(2100427)]' (**arg(26, 2100427))
hide p1
$ update_portrait('oc002_01 16', 'p2', [r(-3), r_shake, light], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c23') '[convertstrid(2100428)]' (**arg(27, 2100428))
$ update_portrait('oc002_01 16', 'p2', [r(-3), dark], 5)
$ update_portrait('sc015_01 2', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100429)]' (**arg(28, 2100429))
$ update_portrait('sc015_01 2', 'p23', [l(9), dark, flip], 5)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(2100430)]' (**arg(29, 2100430))
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na04_b.ogg"
get_char('c13') '[convertstrid(2100431)]' (**arg(30, 2100431))
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
get_char('c231') '[convertstrid(2100432)]' (**arg(31, 2100432))
return "avg1021"