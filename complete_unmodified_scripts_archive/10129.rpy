label avg10129:

$ play_music("ed7104.ogg")
scene avg_bg_019
$ update_narrator('c0')
window show
with fade_in
get_char('c0') '[convertstrid(1007286)]' (**arg(1, 1007286))
$ update_portrait('oc001_01 22', 'p1', [l_entrance(-2), light, flip], 6)
play sfx2 "other_7060.ogg"
get_char('c11') '[convertstrid(1007287)]' (**arg(2, 1007287))
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
play sfx2 "other_7020.ogg"
get_char('c11') '[convertstrid(1007288)]' (**arg(3, 1007288))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 9', 'p2', [r_entrance(-3), light], 6)
get_char('c23') '[convertstrid(1007289)]' (**arg(4, 1007289))
$ update_portrait('oc002_01 9', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 19', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007290)]' (**arg(5, 1007290))
$ update_portrait('oc001_01 19', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 19', 'p2', [r_exit(-3), light], 6)
play sfx2 "other_7085.ogg"
get_char('c23') '[convertstrid(1007291)]' (**arg(6, 1007291))
hide p2
$ update_portrait('oc001_01 12', 'p1', [l(-2), l_shake, light, flip], 6)
play sfx2 "fight_6021.ogg"
play sfxvoice "avg_vocal_na21.ogg"
get_char('c11') '[convertstrid(1007292)]' (**arg(7, 1007292))
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 10', 'p2', [r_entrance(-3), light], 6)
play sfxvoice "avg_vocal_ch18.ogg"
get_char('c23') '[convertstrid(1007293)]' (**arg(8, 1007293))
$ update_portrait('oc002_01 10', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007294)]' (**arg(9, 1007294))
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 6)
get_char('c23') '[convertstrid(1007295)]' (**arg(10, 1007295))
$ update_portrait('oc002_01 18', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1007296)]' (**arg(11, 1007296))
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 5', 'p2', [r(-3), r_shake, light], 6)
get_char('c23') '[convertstrid(1007297)]' (**arg(12, 1007297))
return