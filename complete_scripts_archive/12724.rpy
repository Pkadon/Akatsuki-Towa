label avg12724:

play music "ED6301.ogg"
scene avg_bg_070
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1171763)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
c13041 '[convertstrid(1171764)]'
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1171765)]'
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1171766)]'
return