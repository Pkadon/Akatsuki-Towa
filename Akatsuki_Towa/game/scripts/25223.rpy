label avg25223:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7076.ogg"
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[convertstrid(1210780)]'
hide p1
$ update_portrait('oc002_01 21', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch25.ogg"
c23 '[convertstrid(1210781)]'
hide p2
c20183 '[convertstrid(1210782)]'
play sfx2 "other_7086.ogg"
c0 '[convertstrid(1210783)]'
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 5)
play sfx2 "other_7088.ogg"
c23 '[convertstrid(1210784)]'
hide p2
$ update_portrait('oc001_01 5', 'p1', [mid(-2), light], 5)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_na19.ogg"
c13 '[convertstrid(1210785)]'
return