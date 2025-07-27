label avg25154:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1210486)]'
hide p1
$ update_portrait('uc001_02 1', 'p2014', [mid(6), light], 5)
c20143 '[convertstrid(1210487)]'
hide p2014
$ update_portrait('oc002_01 15', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch05.ogg"
c23 '[convertstrid(1210488)]'
hide p2
$ update_portrait('uc001_02 1', 'p2014', [mid(6), light], 5)
play sfx2 "common_35rewardholy.ogg"
c20143 '[convertstrid(1210489)]'
return