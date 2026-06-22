label avg25163:

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
play sfx2 "common_tag_2.ogg"
get_char('c0') '[convertstrid(1210534)]' (**arg(1, 1210534))
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
play sfx2 "other_7079.ogg"
play sfxvoice "avg_vocal_na21.ogg"
get_char('c13') '[convertstrid(1210535)]' (**arg(2, 1210535))
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1210536)]' (**arg(3, 1210536))
return