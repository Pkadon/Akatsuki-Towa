label avg25149:

stop music
scene placeholderbackground
$ update_portrait('uc001_02 1', 'p2014', [mid(6), light], 6)
$ update_narrator('c20143')
window show
with fade_in
get_char('c20143') '[convertstrid(1210472)]' (**arg(1, 1210472))
hide p2014
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
get_char('c23') '[convertstrid(1210473)]' (**arg(2, 1210473))
hide p2
$ update_portrait('uc001_02 1', 'p2014', [mid(6), light], 6)
get_char('c20143') '[convertstrid(1210474)]' (**arg(3, 1210474))
hide p2014
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
get_char('c13') '[convertstrid(1210475)]' (**arg(4, 1210475))
hide p1
$ update_portrait('uc001_02 1', 'p2014', [mid(6), light], 6)
play sfx2 "common_36rewardsp.ogg"
get_char('c20143') '[convertstrid(1210476)]' (**arg(5, 1210476))
return