label avg25015:

stop music
scene placeholderbackground
$ update_portrait('uc001_01 1', 'p587', [mid(-2), light], 6)
$ update_narrator('c5873')
window show
with fade_in
c5873 '[convertstrid(1210030)]'
hide p587
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210031)]'
hide p1
$ update_portrait('uc001_01 1', 'p587', [mid(-2), light], 6)
play sfx2 "common_sephi2.ogg"
c5873 '[convertstrid(1210032)]'
return