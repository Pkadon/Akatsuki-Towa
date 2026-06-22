label avg25243:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "common_select.ogg"
get_char('c13') '[convertstrid(1210881)]' (**arg(1, 1210881))
hide p1
get_char('c20243') '[convertstrid(1210882)]' (**arg(2, 1210882))
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch04.ogg"
get_char('c23') '[convertstrid(1210883)]' (**arg(3, 1210883))
hide p2
get_char('c20243') '[convertstrid(1210884)]' (**arg(4, 1210884))
return