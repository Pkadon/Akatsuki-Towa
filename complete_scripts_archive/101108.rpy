label avg101108:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1220409)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc003_01 1', 'p11', [l(-4), light, flip], 6)
c111 '[convertstrid(1220410)]'
$ update_portrait('sc003_01 1', 'p11', [l(-4), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1220411)]'
menu:
    extend ""
    "[textdict[1220412]]":
        call avg101109
    "[textdict[1220413]]":
        call avg101110
    "[textdict[1220414]]":
        call avg101111
return