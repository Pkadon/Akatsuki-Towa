label avg1002:

play music "ed7106.ogg"
scene avg_bg_023
$ update_narrator('c0')
window show
with fade_in
c0 '[textdict[2100030]]'
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[2100031]]'
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[2100032]]'
$ update_portrait('sc049_01 1', 'p56', [l(-8), light, flip], 6)
c561 '[textdict[2100033]]'
menu:
    extend ""
    "[textdict[2100034]]":
        call avg1003
    "[textdict[2100035]]":
        call avg1004
    "[textdict[2100036]]":
        call avg1005
return