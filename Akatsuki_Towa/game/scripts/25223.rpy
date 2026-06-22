label avg25223:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7076.ogg"
play sfxvoice "bcv_oc001_hurt_02.ogg"
get_char('c13') '[convertstrid(1210780)]' (**arg(1, 1210780))
hide p1
$ update_portrait('oc002_01 21', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch25.ogg"
get_char('c23') '[convertstrid(1210781)]' (**arg(2, 1210781))
hide p2
get_char('c20183') '[convertstrid(1210782)]' (**arg(3, 1210782))
play sfx2 "other_7086.ogg"
get_char('c0') '[convertstrid(1210783)]' (**arg(4, 1210783))
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
play sfx2 "other_7088.ogg"
get_char('c23') '[convertstrid(1210784)]' (**arg(5, 1210784))
hide p2
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 6)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_na19.ogg"
get_char('c13') '[convertstrid(1210785)]' (**arg(6, 1210785))
return