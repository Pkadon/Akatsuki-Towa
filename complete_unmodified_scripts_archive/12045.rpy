label avg12045:

$ play_music("ed7104.ogg")
scene avg_bg_015
$ update_narrator('c5113')
window show
with fade_in
get_char('c5113') '[convertstrid(1120412)]' (**arg(1, 1120412))
$ update_portrait('oc002_01 13', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch03_b.ogg"
get_char('c21') '[convertstrid(1120413)]' (**arg(2, 1120413))
hide p2
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120414)]' (**arg(3, 1120414))
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 5)
get_char('c5123') '[convertstrid(1120415)]' (**arg(4, 1120415))
hide p1
get_char('c5131') '[convertstrid(1120416)]' (**arg(5, 1120416))
get_char('c5113') '[convertstrid(1120417)]' (**arg(6, 1120417))
get_char('c5131') '[convertstrid(1120418)]' (**arg(7, 1120418))
get_char('c5123') '[convertstrid(1120419)]' (**arg(8, 1120419))
get_char('c5113') '[convertstrid(1120420)]' (**arg(9, 1120420))
get_char('c5131') '[convertstrid(1120421)]' (**arg(10, 1120421))
get_char('c5121') '[convertstrid(1120422)]' (**arg(11, 1120422))
get_char('c5113') '[convertstrid(1120423)]' (**arg(12, 1120423))
get_char('c5113') '[convertstrid(1120424)]' (**arg(13, 1120424))
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1120425)]' (**arg(14, 1120425))
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na02.ogg"
get_char('c13') '[convertstrid(1120426)]' (**arg(15, 1120426))
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 7', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch31.ogg"
get_char('c21') '[convertstrid(1120427)]' (**arg(16, 1120427))
$ update_portrait('oc002_01 7', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1120428)]' (**arg(17, 1120428))
hide p1
get_char('c5113') '[convertstrid(1120429)]' (**arg(18, 1120429))
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
play sfxvoice "bcv_oc002_c02_01.ogg"
get_char('c21') '[convertstrid(1120430)]' (**arg(19, 1120430))
hide p2
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1120431)]' (**arg(20, 1120431))
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
get_char('c5113') '[convertstrid(1120432)]' (**arg(21, 1120432))
get_char('c5133') '[convertstrid(1120433)]' (**arg(22, 1120433))
get_char('c5123') '[convertstrid(1120434)]' (**arg(23, 1120434))
return