label avg102804:

stop music
scene placeholderbackground
$ update_portrait('sc020_01 1', 'p28', [l(-10), light, flip], 6)
$ update_narrator('c281')
window show
with fade_in
c281 '[convertstrid(1219724)]'
$ update_portrait('sc020_01 1', 'p28', [l(-10), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1219725)]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc020_01 4', 'p28', [l(-10), light, flip], 6)
c281 '[convertstrid(1219726)]'
menu:
    extend ""
    "[textdict[1219727]]":
        call avg102805
    "[textdict[1219728]]":
        call avg102806
    "[textdict[1219729]]":
        call avg102807
return