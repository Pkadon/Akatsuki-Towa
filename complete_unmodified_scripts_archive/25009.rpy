label avg25009:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1210014)]'
hide p1
$ update_portrait('uc001_01 1', 'p587', [mid(-2), light], 6)
play sfx2 "common_36rewardsp.ogg"
c5873 '[convertstrid(1210015)]'
return