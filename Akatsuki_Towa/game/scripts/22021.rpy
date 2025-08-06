label avg22021:

play music "ed7105.ogg"
scene avg_bg_023
$ update_narrator('c561')
$ update_portrait('sc049_01 5', 'p56', [l(-8), light, flip], 6)
window show
with fade_in
$ update_portrait('sc049_01 5', 'p56', [l_midback(-8), light, flip], 6)
c561 '[convertstrid(1120002)]'
$ update_portrait('sc049_01 5', 'p56', [l(-8), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1120003)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
play sfx2 "other_7091.ogg"
c561 '[convertstrid(1120004)]'
hide p56
$ update_portrait('sc050_01 1', 'p57', [l(-19), light, flip], 6)
c571 '[convertstrid(1120005)]'
hide p57
$ update_portrait('sc052_01 5', 'p59', [l(-25), light, flip], 6)
c591 '[convertstrid(1120006)]'
hide p1
$ update_portrait('sc052_01 5', 'p59', [l(-25), dark, flip], 5)
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1120007)]'
menu:
    extend ""
    "[textdict[1120008]]":
        call avg22022
    "[textdict[1120009]]":
        call avg22023
return