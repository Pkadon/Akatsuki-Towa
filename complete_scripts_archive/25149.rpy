label avg25149:

stop music
scene placeholderbackground
$ update_portrait('uc001_02 1', 'p2014', [mid(6), light], 5)
$ update_narrator('c20143')
window show
with fade_in
c20143 '[convertstrid(1210472)]'
hide p2014
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[convertstrid(1210473)]'
hide p2
$ update_portrait('uc001_02 1', 'p2014', [mid(6), light], 5)
c20143 '[convertstrid(1210474)]'
hide p2014
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1210475)]'
hide p1
$ update_portrait('uc001_02 1', 'p2014', [mid(6), light], 5)
play sfx2 "common_36rewardsp.ogg"
c20143 '[convertstrid(1210476)]'
return