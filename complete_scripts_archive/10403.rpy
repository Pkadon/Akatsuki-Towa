label avg10403:

play music "ED6518.ogg"
scene avg_bg_001
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1140280)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1140282)]'
menu:
    extend ""
    "[textdict[1140283]]":
        call avg10404
    "[textdict[1140284]]":
        call avg10405
return