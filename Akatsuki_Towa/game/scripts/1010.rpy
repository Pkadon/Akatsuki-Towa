label avg1010:

play music "ed7106.ogg"
scene avg_bg_023
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
$ update_narrator('c561')
window show
with fade_in
c561 '[textdict[2100125]]'
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[2100126]]'
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[2100127]]'
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[2100128]]'
menu:
    extend ""
    "[textdict[2100129]]":
        call avg1011
    "[textdict[2100130]]":
        call avg1012
    "[textdict[2100131]]":
        call avg1013
return