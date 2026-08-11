label avg25122(trans=fade_in):

stop music
scene placeholderbackground
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with trans
play sfxvoice "avg_vocal_ch06.ogg"
get_char('c23') '[convertstrid(1210359)]' (**arg(1, 1210359))
hide p2
$ update_portrait('uc001_02 3', 'p2011', [mid(6), light], 6)
get_char('c20113') '[convertstrid(1210360)]' (**arg(2, 1210360))
hide p2011
play sfx2 "other_7088.ogg"
get_char('c0') '[convertstrid(1210361)]' (**arg(3, 1210361))
$ update_portrait('uc001_02 1', 'p2011', [mid(6), light], 6)
get_char('c20113') '[convertstrid(1210362)]' (**arg(4, 1210362))
hide p2011
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na04.ogg"
get_char('c13') '[convertstrid(1210363)]' (**arg(5, 1210363))
hide p1
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch17.ogg"
get_char('c23') '[convertstrid(1210364)]' (**arg(6, 1210364))
hide p2
$ update_portrait('uc001_02 1', 'p2011', [mid(6), light], 6)
play sfx2 "common_36rewardsp.ogg"
get_char('c20113') '[convertstrid(1210365)]' (**arg(7, 1210365))
return "avg25122"