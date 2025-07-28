label avg102104:

stop music
scene placeholderbackground
$ update_portrait('sc013_01 1', 'p21', [l(-12), light, flip], 6)
$ update_narrator('c211')
window show
with fade_in
c211 '[convertstrid(1218820)]'
$ update_portrait('sc013_01 4', 'p21', [l(-12), light, flip], 6)
c211 '[convertstrid(1218821)]'
$ update_portrait('sc013_01 4', 'p21', [l(-12), dark, flip], 5)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1218822)]'
menu:
    extend ""
    "[textdict[1218823]]":
        call avg102105
    "[textdict[1218824]]":
        call avg102106
    "[textdict[1218825]]":
        call avg102107
return