label avg102125:

stop music
scene placeholderbackground
$ update_portrait('sc013_01 3', 'p21', [l(-12), light, flip], 6)
$ update_narrator('c211')
window show
with fade_in
c211 '[convertstrid(1218879)]'
$ update_portrait('sc013_01 3', 'p21', [l(-12), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[convertstrid(1218880)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc013_01 1', 'p21', [l(-12), light, flip], 6)
c211 '[convertstrid(1218881)]'
menu:
    extend ""
    "[textdict[1218882]]":
        call avg102126
    "[textdict[1218883]]":
        call avg102127
    "[textdict[1218884]]":
        call avg102128
return