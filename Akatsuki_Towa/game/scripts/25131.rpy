label avg25131:

stop music
scene placeholderbackground
$ update_portrait('uc002_01 2', 'p2012', [mid(2), light], 6)
$ update_narrator('c20123')
window show
with fade_in
play sfx2 "other_7088.ogg"
c20123 '[convertstrid(1210391)]'
hide p2012
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[convertstrid(1210392)]'
hide p2
$ update_portrait('uc002_01 1', 'p2012', [mid(2), light], 6)
c20123 '[convertstrid(1210393)]'
hide p2012
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210394)]'
hide p1
play sfx2 "other_7004.ogg"
c0 '[convertstrid(1210395)]'
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1210396)]'
hide p1
$ update_portrait('uc002_01 1', 'p2012', [mid(2), light], 6)
play sfx2 "common_36rewardsp.ogg"
c20123 '[convertstrid(1210397)]'
return