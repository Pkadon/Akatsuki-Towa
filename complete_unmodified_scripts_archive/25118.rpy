label avg25118:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 7', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "elc_5006.ogg"
play sfxvoice "avg_vocal_ch31.ogg"
get_char('c23') '[convertstrid(1210345)]' (**arg(1, 1210345))
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
get_char('c23') '[convertstrid(1210346)]' (**arg(2, 1210346))
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 6)
play sfx2 "common_35rewardholy.ogg"
get_char('c13') '[convertstrid(1210347)]' (**arg(3, 1210347))
return