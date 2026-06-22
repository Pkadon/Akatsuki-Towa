label avg20100:

$ play_music("ed7104.ogg")
scene avg_bg_037
$ update_narrator('c21')
window show
with fade_in
$ update_portrait('oc002_01 2', 'p2', [l_entrance(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c21') '[convertstrid(1004850)]' (**arg(1, 1004850))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
play sfx2 "other_7044.ogg"
get_char('c13') '[convertstrid(1004851)]' (**arg(2, 1004851))
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
play sfx2 "other_7047.ogg"
get_char('c6871') '[convertstrid(1004852)]' (**arg(3, 1004852))
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
get_char('c13') '[convertstrid(1004853)]' (**arg(4, 1004853))
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
play sfx2 "other_7004.ogg"
get_char('c6871') '[convertstrid(1004854)]' (**arg(5, 1004854))
hide p1
play sfx2 "other_7064.ogg"
get_char('c0') '[convertstrid(1004855)]' (**arg(6, 1004855))
get_char('c6881') '[convertstrid(1004856)]' (**arg(7, 1004856))
get_char('c6881') '[convertstrid(1004857)]' (**arg(8, 1004857))
get_char('c5053') '[convertstrid(1004858)]' (**arg(9, 1004858))
play sfx2 "other_7085.ogg"
get_char('c6883') '[convertstrid(1004859)]' (**arg(10, 1004859))
$ update_narrator('c6871')
with fade
get_char('c6871') '[convertstrid(1004860)]' (**arg(11, 1004860))
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 6)
get_char('c13') '[convertstrid(1004861)]' (**arg(12, 1004861))
return