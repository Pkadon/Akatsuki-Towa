label avg25259:

stop music
scene placeholderbackground
$ update_narrator('c20183')
window show
with fade_in
play sfx2 "other_7043.ogg"
c20183 '[convertstrid(1210966)]'
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_atk_01.ogg"
c23 '[convertstrid(1210967)]'
hide p2
play sfx2 "other_7091.ogg"
c20183 '[convertstrid(1210968)]'
play sfx2 "other_7086.ogg"
c0 '[convertstrid(1210969)]'
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
play sfx2 "fight_6026.ogg"
play sfxvoice "avg_vocal_ch13.ogg"
c23 '[convertstrid(1210970)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc001_com_01.ogg"
c13 '[convertstrid(1210971)]'
return