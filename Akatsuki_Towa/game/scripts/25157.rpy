label avg25157(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with trans
play sfx2 "other_7092.ogg"
play sfxvoice "avg_vocal_na18.ogg"
get_char('c13') '[convertstrid(1210499)]' (**arg(1, 1210499))
hide p1
get_char('c6123') '[convertstrid(1210500)]' (**arg(2, 1210500))
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfx2 "elc_5004.ogg"
get_char('c23') '[convertstrid(1210501)]' (**arg(3, 1210501))
return "avg25157"