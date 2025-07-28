label avg10404:

play music "ED6518.ogg"
scene avg_bg_001
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "common_select.ogg"
c13 '[convertstrid(1140286)]'
return