label avg20112:
stop music

play music "ed7150.ogg"
scene avg_bg_038
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
window show
with fade_in
c23 '[textdict[1005447]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1001032]]'
menu:
    extend ""
    "[textdict[1005449]]":
        call avg10092
    "[textdict[1005450]]":
        call avg10094
return