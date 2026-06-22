label avg25207:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
get_char('c23') '[convertstrid(1210707)]' (**arg(1, 1210707))
hide p2
play sfx2 "other_7088.ogg"
get_char('c20153') '[convertstrid(1210708)]' (**arg(2, 1210708))
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na22.ogg"
get_char('c13') '[convertstrid(1210709)]' (**arg(3, 1210709))
hide p1
get_char('c20153') '[convertstrid(1210710)]' (**arg(4, 1210710))
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_arts_03.ogg"
get_char('c23') '[convertstrid(1210711)]' (**arg(5, 1210711))
hide p2
get_char('c20153') '[convertstrid(1210712)]' (**arg(6, 1210712))
play sfx2 "other_7086.ogg"
get_char('c0') '[convertstrid(1210713)]' (**arg(7, 1210713))
$ update_portrait('oc002_01 17', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch20.ogg"
get_char('c23') '[convertstrid(1210714)]' (**arg(8, 1210714))
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210715)]' (**arg(9, 1210715))
hide p1
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 6)
play sfx2 "common_35rewardholy.ogg"
play sfxvoice "avg_vocal_ch17.ogg"
get_char('c23') '[convertstrid(1210716)]' (**arg(10, 1210716))
return