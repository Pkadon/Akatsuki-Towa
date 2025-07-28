label avg25271:

stop music
scene placeholderbackground
$ update_narrator('c20143')
window show
with fade_in
c20143 '[convertstrid(1211021)]'
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1211022)]'
hide p1
c20143 '[convertstrid(1211023)]'
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 6)
play sfxvoice "bcv_oc002_arts_03.ogg"
c23 '[convertstrid(1211024)]'
hide p2
c20143 '[convertstrid(1211025)]'
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na10.ogg"
c13 '[convertstrid(1211026)]'
hide p1
c20143 '[convertstrid(1211027)]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[convertstrid(1211028)]'
hide p2
play sfx2 "common_core.ogg"
c20143 '[convertstrid(1211029)]'
play sfx2 "other_7086.ogg"
c0 '[convertstrid(1211030)]'
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfx2 "common_36rewardsp.ogg"
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1211031)]'
return