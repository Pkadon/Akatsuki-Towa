label avg103004:

stop music
scene placeholderbackground
$ update_portrait('sc022_01 1', 'p30', [l(-9), light, flip], 6)
$ update_narrator('c301')
window show
with fade_in
c301 '[convertstrid(1222419)]'
$ update_portrait('sc022_01 1', 'p30', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1222420)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc022_01 4', 'p30', [l(-9), light, flip], 6)
c301 '[convertstrid(1222421)]'
$ update_portrait('sc022_01 4', 'p30', [l(-9), dark, flip], 5)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1222422)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1222423)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc022_01 5', 'p30', [l(-9), light, flip], 6)
c301 '[convertstrid(1222424)]'
menu:
    extend ""
    "[textdict[1222425]]":
        call avg103005
    "[textdict[1222426]]":
        call avg103006
    "[textdict[1222427]]":
        call avg103007
return