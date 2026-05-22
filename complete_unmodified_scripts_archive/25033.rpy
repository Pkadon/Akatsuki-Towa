label avg25033:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1210083)]'
hide p1
$ update_portrait('uc001_01 1', 'p2000', [mid(-2), light], 6)
c20003 '[convertstrid(1210084)]'
hide p2000
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210085)]'
hide p1
$ update_portrait('uc001_01 1', 'p2000', [mid(-2), light], 6)
play sfx2 "common_35rewardholy.ogg"
c20003 '[convertstrid(1210086)]'
return