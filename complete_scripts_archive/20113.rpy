label avg20113:

$ play_music("ed7150.ogg")
scene avg_bg_038
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
c23 '[convertstrid(1005447)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1001032)]'
menu:
    extend ""
    "[textdict[1005449]]":
        call avg10093
    "[textdict[1005450]]":
        call avg10095
return