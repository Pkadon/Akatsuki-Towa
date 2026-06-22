label avg25154:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
get_char('c13') '[convertstrid(1210486)]' (**arg(1, 1210486))
hide p1
$ update_portrait('uc001_02 1', 'p2014', [mid(6), light], 6)
get_char('c20143') '[convertstrid(1210487)]' (**arg(2, 1210487))
hide p2014
$ update_portrait('oc002_01 15', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch05.ogg"
get_char('c23') '[convertstrid(1210488)]' (**arg(3, 1210488))
hide p2
$ update_portrait('uc001_02 1', 'p2014', [mid(6), light], 6)
play sfx2 "common_35rewardholy.ogg"
get_char('c20143') '[convertstrid(1210489)]' (**arg(4, 1210489))
return