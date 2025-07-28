label avg22021:

play music "ed7105.ogg"
scene placeholderbackground
$ update_portrait('sc049_01 5', 'p56', [mid(-8), light], 6)
$ update_narrator('c563')
window show
with fade_in
c563 '[convertstrid(1120002)]'
hide p56
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1120003)]'
hide p1
$ update_portrait('sc049_01 1', 'p56', [mid(-8), light], 6)
play sfx2 "other_7091.ogg"
c563 '[convertstrid(1120004)]'
hide p56
$ update_portrait('sc050_01 1', 'p57', [mid(-19), light], 6)
c573 '[convertstrid(1120005)]'
hide p57
$ update_portrait('sc052_01 5', 'p59', [mid(-25), light], 6)
c593 '[convertstrid(1120006)]'
hide p59
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1120007)]'
menu:
    extend ""
    "[textdict[1120008]]":
        call avg22022
    "[textdict[1120009]]":
        call avg22023
return