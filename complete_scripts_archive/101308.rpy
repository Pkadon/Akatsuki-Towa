label avg101308:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1220970)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1220971)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
c131 '[convertstrid(1220972)]'
$ update_portrait('sc005_01 1', 'p13', [l(-17), dark, flip], 5)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1220973)]'
menu:
    extend ""
    "[textdict[1220974]]":
        call avg101309
    "[textdict[1220975]]":
        call avg101310
    "[textdict[1220976]]":
        call avg101311
return