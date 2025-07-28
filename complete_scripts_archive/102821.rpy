label avg102821:

stop music
scene placeholderbackground
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
$ update_narrator('c281')
window show
with fade_in
c281 '[convertstrid(1219777)]'
$ update_portrait('sc020_01 1', 'p28', [l(-10), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1219778)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
c281 '[convertstrid(1219779)]'
$ update_portrait('sc020_01 4', 'p28', [l(-10), light, flip], 6)
c281 '[convertstrid(1219780)]'
menu:
    extend ""
    "[textdict[1219781]]":
        call avg102822
    "[textdict[1219782]]":
        call avg102823
    "[textdict[1219783]]":
        call avg102824
return