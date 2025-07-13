label avg102921:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[textdict[1219954]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc021_01 1', 'p29', [l(-17), light, flip], 6)
c291 '[textdict[1219955]]'
$ update_portrait('sc021_01 1', 'p29', [l(-17), light, flip], 6)
c291 '[textdict[1219956]]'
menu:
    extend ""
    "[textdict[1219957]]":
        call avg102922
    "[textdict[1219958]]":
        call avg102923
    "[textdict[1219959]]":
        call avg102924
return